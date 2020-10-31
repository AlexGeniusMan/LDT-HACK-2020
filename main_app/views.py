from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from main_app.models import *
from main_app.serializers import *
import requests
from base64 import encodebytes
from django.http import JsonResponse
import json


class CreateTask(APIView):
    """
    Создаёт задание
    """

    def post(self, request, *args, **kwargs):
        serializer = CreateChangeTaskSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            task = Task(name=serializer.data['name'],
                        theory=serializer.data['theory'],
                        mission=serializer.data['mission'],
                        sprint=Sprint.objects.get(id=request.data['sprint']),
                        languages=request.data['languages'].split(','), )
            task.save()
            task.students.set(User.objects.filter(grades=request.POST.get('grade')))
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowTask(APIView):
    """
    Показывает задание
    """

    def get(self, request, pk):
        data = Task.objects.get(pk=pk)
        serialized_data = CurrentTaskSerializer(data, context={'request': request})
        return Response(serialized_data.data)


class DeleteTask(DestroyAPIView):
    """
    Удаляет задание
    """

    queryset = Task.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ChangeTask(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = CreateChangeTaskSerializer


class CreateBlock(APIView):
    """
    Создаёт блок
    """

    queryset = Sprint.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = CreateSprintSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            Sprint.objects.create(grade=Grade.objects.get(id=request.data['grade']),
                                  name=serializer.data['name'])
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteBlock(DestroyAPIView):
    """
    Удаляет блок
    """

    queryset = Sprint.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ChangeBlock(UpdateAPIView):
    queryset = Sprint.objects.all()
    serializer_class = ChangeBlockSerializer


class ShowClass(APIView):
    """
    Возвращает класс
    """

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

    def get(self, request):
        if request.user.groups.filter(name='Учителя').exists():
            return Response('TEACHER')
        elif request.user.groups.filter(name='Ученики').exists():
            return Response('STUDENT')
        else:
            return Response('USER_IS_NOT_IN_THE_GROUP')


class CodeChecker(APIView):
    """
    Отправляет код на проверку
    """

    def post(self, request, pk):
        key = 'kek'
        language = request.POST['language']

#         code = encodebytes('''#include <iostream>
#
# using namespace std;
#
# int main() {
# int a,b;
# cin >> a >> b;
# cout << a + b;
#
# }'''.encode()).decode('UTF-8')

        # print(request.POST['code'])
        # print(request.POST['code'].replace('↵', '\n'))
        # print(request.POST['code'].replace('\n', '↵'))

        code = encodebytes(request.POST['code'].replace('↵', '\n').encode()).decode('UTF-8')

        tests_query = Test.objects.filter(task=request.POST['task_id'])
        tests = list()
        for el in tests_query:
            temp_dict = {
                'request': el.question.replace('\r', '') + '\n',
                'answer': el.answer.replace('\r', '')
            }
            tests.append(temp_dict)

        time_limit_millis = request.POST['time_limit_millis']
        user_id = request.user.id

        ej_response = requests.post(
            'http://188.120.248.65:8065/ejapi/tasks/run',
            json={
                'key': key,
                'language': language,
                'code': code,
                'tests': [{'request': '1\n1\n', 'answer': '2'}, {'request': '2\n3\n', 'answer': '4'}],
                'time_limit_millis': time_limit_millis,
                'user_id': user_id
            }
        )

        ej_response = json.loads(ej_response.text)

        if ej_response['body'] == 'Compilation error':
            return Response(ej_response['error'])
        else:
            ej_tests = list()
            for el in ej_response['body']:
                ej_temp_dict = {
                    'test_num': el['test_num'],
                    'status': el['status'],
                    'error': el['stderr']
                }
                ej_tests.append(ej_temp_dict)

            data = {
                'status': ej_response['status'],
                'tests': ej_tests
            }
        return Response(data)
