from rest_framework import serializers
from .models import *


#
# class SnippetSerializer(serializers.Serializer):
#
#     name = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     grade_id = serializers.IntegerField(read_only=True)
#
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Sprint.objects.create(**validated_data)

# class JSONDeSerializer(serializers.ModelSerializer):
#     class Meta:
#         depth = 2
#         model = Sprint
#         fields = ('name', 'sprints')

# api/classes/id - creating new sprint
class CreateSprintSerializer(serializers.ModelSerializer):

    class Meta:
        depth = 2
        model = Sprint
        fields = ('id', 'name', 'grade')


# api/my_courses
class MyCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Grade
        fields = ('id', 'name')


# api/tasks/id
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Task
        fields = ('id', 'question', 'answer')


class CurrentTaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = TaskDetail
        fields = ('id', 'is_done', 'last_code')


class CurrentTaskSerializer(serializers.ModelSerializer):
    task_detail = CurrentTaskDetailSerializer(read_only=True, many=True)
    tests = TestSerializer(read_only=True, many=True)

    class Meta:
        depth = 2
        model = Task
        fields = ('id', 'name', 'theory', 'mission', 'task_detail', 'languages', 'tests')


# api/courses/id
class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = TaskDetail
        fields = ('id', 'is_done', 'last_code')


class TaskSerializer(serializers.ModelSerializer):
    task_detail = TaskDetailSerializer(read_only=True, many=True)

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
        # fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    sprints = SprintSerializer(many=True, read_only=True)

    class Meta:
        depth = 2
        model = Grade
        fields = ('id', 'name', 'sprints')
