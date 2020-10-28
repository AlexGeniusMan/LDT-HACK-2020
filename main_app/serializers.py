from rest_framework import serializers
from .models import *


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = TaskDetail
        fields = ('is_done', 'id')


class TaskSerializer(serializers.ModelSerializer):
    task_detail = TaskDetailSerializer(many=True, read_only=True)

    class Meta:
        depth = 2
        model = Task
        fields = ('name', 'id', 'task_detail')


class SprintSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        depth = 2
        model = Sprint
        fields = ('name', 'id', 'tasks')


class GradeSerializer(serializers.ModelSerializer):
    sprints = SprintSerializer(many=True, read_only=True)

    class Meta:
        depth = 2
        model = Grade
        fields = ('name', 'id', 'sprints')
