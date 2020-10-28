from rest_framework import serializers
from .models import *


class CurrentTaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = TaskDetail
        fields = ('id', 'is_done', 'last_code')


class CurrentTaskSerializer(serializers.ModelSerializer):
    task_detail = CurrentTaskDetailSerializer(many=True, read_only=True)

    class Meta:
        depth = 2
        model = Task
        fields = ('id', 'name', 'theory', 'mission', 'task_detail', 'languages')


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = TaskDetail
        fields = ('id', 'is_done')


class TaskSerializer(serializers.ModelSerializer):
    task_detail = TaskDetailSerializer(many=True, read_only=True)

    class Meta:
        depth = 2
        model = Task
        fields = ('id', 'name', 'task_detail')


class SprintSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        depth = 2
        model = Sprint
        fields = ('id', 'name', 'tasks')


class GradeSerializer(serializers.ModelSerializer):
    sprints = SprintSerializer(many=True, read_only=True)

    class Meta:
        depth = 2
        model = Grade
        fields = ('id', 'name', 'sprints')
