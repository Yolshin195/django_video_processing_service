import os
import uuid

from django.db import models


class FileModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=1024)
    file = models.FileField(upload_to="uploads/")

    def save(self, *args, **kwargs):
        # Проверяем, заполнено ли поле name и не является ли именем уже именем файла
        if not self.name or os.path.basename(self.file.name) != self.name:
            # Заполняем поле name исходным именем файла
            self.name = os.path.basename(self.file.name)

        # Вызываем метод save родительского класса для сохранения объекта
        super(FileModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.__class__.__name__} - {self.name}"
