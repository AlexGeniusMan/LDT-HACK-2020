from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from main_app.models import *
from main_app.serializers import *


# class CreateSprint(APIView):
#     def post(self, request):
#         grade_id = request.data.class_id
#         sprint_name = request.data.sprint_name
#         Sprint.objects.create(**validated_data)


class CreateTask(APIView):

    def post(self, request, *args, **kwargs):
        serializer = CreateTaskSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            task = Task(name=serializer.data['name'],
                        theory=serializer.data['theory'],
                        mission=serializer.data['mission'],
                        sprint=Sprint.objects.get(id=request.data['sprint']),
                        languages=request.data['languages'].split(','),)
            task.save()
            task.students.set(User.objects.filter(grades=request.POST.get('grade')))
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowTask(APIView):
    def get(self, request, pk):
        data = Task.objects.get(pk=pk)
        data_s = CurrentTaskSerializer(data, context={'request': request})
        return Response(data_s.data)

class DeleteTask(DestroyAPIView):
    queryset = Task.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CreateSprint(APIView):

    def post(self, request, *args, **kwargs):
        serializer = CreateSprintSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            Sprint.objects.create(grade=Grade.objects.get(id=request.data['grade']),
                                  name=serializer.data['name'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteSprint(DestroyAPIView):
    queryset = Sprint.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class AddNewSprint(APIView):
#     def post(self, request):
#         grade_id = request.data.class_id
#         sprint_name = request.data.sprint_name


class ShowClass(APIView):
    """
    Возвращает конкретный класс
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        grade = Grade.objects.get(pk=pk)
        serialized_data = GradeSerializer(grade, context={'request': request})
        user_courses = request.user.grades.all()

        if grade in user_courses:
            return Response(serialized_data.data)
        else:
            return Response(status.HTTP_403_FORBIDDEN)


class ShowMyClasses(APIView):
    """
    Возвращает классы пользователя
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = request.user.grades.all()
        serialized_data = MyCoursesSerializer(data, context={'request': request}, many=True)
        if request.user.groups.filter(name='Учителя').exists():
            return Response(serialized_data.data)
        elif request.user.groups.filter(name='Ученики').exists():
            return Response(serialized_data.data)


class CoursePage(APIView):
    """
    Возвращает статус пользователя
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.user.groups.filter(name='Учителя').exists():
            return Response('TEACHER')
        elif request.user.groups.filter(name='Ученики').exists():
            return Response('STUDENT')
        else:
            return Response('USER IS NOT IN THE GROUP')
