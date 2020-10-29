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

class CreateSprint(mixins.CreateModelMixin,
                   generics.GenericAPIView):
    serializer_class = CreateSprintSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# class AddNewSprint(APIView):
#     def post(self, request):
#         grade_id = request.data.class_id
#         sprint_name = request.data.sprint_name


class ShowClass(APIView):
    def get(self, request, pk):

        if request.user.is_authenticated:
            data = Grade.objects.get(pk=pk)
            data_s = GradeSerializer(data, context={'request': request})
            print(data_s.data)
            user_courses = request.user.users.all()

            if data in user_courses:
                return Response(data_s.data)
                # return Response('DATA')
            else:
                return Response('GOOD AUTH BUT NO ACCESS TO THIS COURSE')
        else:
            return Response('NO AUTH')


class ShowTask(APIView):
    def get(self, request, pk):
        data = Task.objects.get(pk=pk)
        data_s = CurrentTaskSerializer(data, context={'request': request})
        return Response(data_s.data)


class ShowMyClasses(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            data = request.user.users.all()
            print(data)

            data_s = MyCoursesSerializer(data, context={'request': request}, many=True)

            if user.groups.filter(name='Учителя').exists():
                return Response(data_s.data)
            elif user.groups.filter(name='Ученики').exists():
                return Response(data_s.data)
            # user = User.objects.get(username=username)
        else:
            data = Grade.objects.all()
            data_s = MyCoursesSerializer(data, context={'request': request}, many=True)
            return Response(data_s.data)

# class CoursePage(APIView):
#     def get(self, request):
#
#         # print(request.data.get(email))
#         user = User.objects.get(email='ivanlovecats@mail.ru')
#
#         if user.groups.filter(name='Учителя').exists():
#             return Response('TEACHER')
#         elif user.groups.filter(name='Ученики').exists():
#             data =
#
#             return Response('STUDENT')
#         else:
#             return Response('USER IS NOT IN THE CLASS')

#
# class ShowUserGroup(APIView):
#
#     def get(self, request):
#
#         str_all = ''
#         for user in User.objects.all():
#             if user.groups.filter(name='Учителя').exists():
#                 str_temp = str(user) + ' - учитель   |   '
#             elif user.groups.filter(name='Ученики').exists():
#                 str_temp = str(user) + ' - ученик   |   '
#             else:
#                 str_temp = str(user) + ' - не принадлежит ни к одной из групп   |   '
#             str_all = str_all + str_temp
#
#         if str_all == '':
#             return Response('NO USERS')
#         else:
#             return Response(str_all)
