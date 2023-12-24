from django.shortcuts import render

from .forms import FileUploadForm, YouTubeForm, TorrentFileForm


def home_page(request):
    return render(request, 'task/home.html')


def create_task(request):
    if request.method == 'POST':
        # Обработка формы загрузки файла с компьютера
        file_upload_form = FileUploadForm(request.POST, request.FILES)
        if file_upload_form.is_valid():
            file_upload_form.save()

        # Обработка формы файла с YouTube
        youtube_form = YouTubeForm(request.POST)
        if youtube_form.is_valid():
            youtube_form.save()

        # Обработка формы файла с Torrent
        torrent_form = TorrentFileForm(request.POST, request.FILES)
        if torrent_form.is_valid():
            torrent_form.save()
    else:
        # Если запрос не POST, создайте пустые формы
        file_upload_form = FileUploadForm()
        youtube_form = YouTubeForm()
        torrent_form = TorrentFileForm()

    return render(request, 'task/create_task.html', {
        'file_upload_form': file_upload_form,
        'youtube_form': youtube_form,
        'torrent_form': torrent_form,
    })
