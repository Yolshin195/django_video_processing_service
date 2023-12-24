import uuid
from enum import Enum

from django.core.exceptions import ObjectDoesNotExist
from django.db import models, transaction

from file.models import FileModel


class StatusEnum(Enum):
    CREATED = "created"
    STARTED_DOWNLOADING = "started_downloading"
    FINISHED_DOWNLOADING = "finished_downloading"
    STARTED_PROCESSING = "started_processing"
    FINISHED_PROCESSING = "finished_processing"
    ERROR = "error"
    COMPLETED = "completed"


class TypeEnum(Enum):
    CUSTOM = "custom"
    YOUTUBE = "youtube"
    TORRENT = "torrent"


class FileTypeEnum(Enum):
    TORRENT = "torrent"
    SOURCE = "source"
    RESULT = "result"


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} - {self.id}"


class BaseReference(BaseModel):
    code = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} - {self.name} ({self.code})"

    @classmethod
    def get_by_code(cls, code):
        try:
            return cls.objects.get(code=code)
        except ObjectDoesNotExist:
            return None


class TaskStatusModel(BaseReference):
    pass


class TaskTypeModel(BaseReference):
    pass


class FileType(BaseReference):
    pass


class TaskModel(BaseModel):
    type = models.ForeignKey(TaskTypeModel, on_delete=models.CASCADE)
    status = models.ForeignKey(TaskStatusModel, on_delete=models.CASCADE)

    @classmethod
    def create(cls, type_enum: TypeEnum, status_enum: StatusEnum) -> "TaskModel":
        return cls.objects.create(
            type=TaskTypeModel.get_by_code(type_enum.value),
            status=TaskStatusModel.get_by_code(status_enum.value),
        )


class TaskYouTubeLink(BaseModel):
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
    url = models.URLField()

    @classmethod
    def create(cls, url: str):
        cls.objects.create(
            url=url,
            task=TaskModel.create(
                type_enum=TypeEnum.YOUTUBE, status_enum=StatusEnum.CREATED
            ),
        )


class TaskFilesLink(BaseModel):
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
    file = models.ForeignKey(FileModel, on_delete=models.CASCADE)
    type = models.ForeignKey(FileType, on_delete=models.CASCADE)

    @classmethod
    def create(cls, file, type_file: FileTypeEnum, type_task: TypeEnum):
        return cls.objects.create(
            task=TaskModel.create(type_enum=type_task, status_enum=StatusEnum.CREATED),
            file=FileModel.objects.create(file=file),
            type=FileType.get_by_code(type_file.value),
        )
