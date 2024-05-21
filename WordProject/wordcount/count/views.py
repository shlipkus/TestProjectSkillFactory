from django.shortcuts import render, redirect
from .models import File
from .forms import IndexForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        if request.POST.get('action') == 'delete':
            objs = File.objects.all()
            for obj in objs:
                obj.delete()
            return redirect('index')

        form = IndexForm(request.POST, request.FILES)
        file = request.FILES['file']
        word = request.POST.get('word')
        File.objects.create(word=word, file=file).save()
        file_1 = File.objects.get(word=word)
        with open(f'media/{file_1.file}') as f:
            text = f.read().split(' ')
        c = text.count(word)
        return render(request, 'index.html', {'form': form, 'count': c, 'file': file, 'word': word})
    form = IndexForm
    return render(request, 'index.html', {'form': form})