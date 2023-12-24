from django.contrib import admin

from .models import TaskTypeModel, TaskStatusModel, FileType, TaskModel, TaskFilesLink, TaskYouTubeLink

admin.site.register(TaskTypeModel)
admin.site.register(TaskStatusModel)
admin.site.register(FileType)
admin.site.register(TaskModel)
admin.site.register(TaskFilesLink)
admin.site.register(TaskYouTubeLink)
