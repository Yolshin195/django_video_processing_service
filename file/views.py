from django.shortcuts import render, redirect
from .forms import FileModelForm


def upload_file(request):
    if request.method == 'POST':
        form = FileModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  # Замените 'success' на имя вашего шаблона успешной загрузки
    else:
        form = FileModelForm()
    return render(request, 'file/upload_file.html', {'form': form})
