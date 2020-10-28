from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from main_app.models import User


class ShowUserGroup(APIView):

    def get(self, request):

        str_all = ''
        for user in User.objects.all():
            if user.groups.filter(name='Учителя').exists():
                str_temp = str(user) + ' - учитель   |   '
            elif user.groups.filter(name='Ученики').exists():
                str_temp = str(user) + ' - ученик   |   '
            else:
                str_temp = str(user) + ' - не принадлежит ни к одной из групп   |   '
            str_all = str_all + str_temp

        if str_all == '':
            return Response('NO USERS')
        else:
            return Response(str_all)
