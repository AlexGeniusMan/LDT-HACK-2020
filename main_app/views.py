from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from main_app.models import *
from main_app.serializers import *


class ShowCourse(APIView):
    def get(self, request):
        data = Grade.objects.get(name='123')
        data = GradeSerializer(data, context={'request': request})
        return Response(data.data)


class ShowTask(APIView):
    def get(self, request, pk):
        data = Task.objects.get(pk=pk)
        data = CurrentTaskSerializer(data, context={'request': request})
        return Response(data.data)


class CheckUser(APIView):
    def get(self, request):
        username = request.data
        print(username)
        return Response('1')
        # user = User.objects.get(username=username)

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
