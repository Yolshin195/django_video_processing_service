from django import forms
from django.db import transaction

from task.models import TaskFilesLink, TaskYouTubeLink
from task.models import TypeEnum
from task.models import FileTypeEnum


class FileUploadForm(forms.Form):
    file_with_user = forms.FileField()

    def save(self):
        with transaction.atomic():
            TaskFilesLink.create(
                file=self.cleaned_data["file_with_user"],
                type_file=FileTypeEnum.SOURCE,
                type_task=TypeEnum.CUSTOM,
            )


class YouTubeForm(forms.Form):
    youtube_url = forms.URLField()

    def save(self):
        with transaction.atomic():
            TaskYouTubeLink.create(url=self.cleaned_data["youtube_url"])


class TorrentFileForm(forms.Form):
    file_with_torrent = forms.FileField()

    def save(self):
        with transaction.atomic():
            TaskFilesLink.create(
                file=self.cleaned_data["file_with_torrent"],
                type_file=FileTypeEnum.TORRENT,
                type_task=TypeEnum.TORRENT,
            )
