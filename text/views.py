from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect


from .models import Text
from .forms import TextForm

def post_list(request):
    texts = Text.objects.order_by('published_date')
    return render(request, 'text/post_list.html', {'texts': texts})


def post_detail(request, pk):
    text = get_object_or_404(Text, pk=pk)
    return render(request, 'text/post_detail.html', {'text': text})


def post_new(request):

    if request.method == "POST":
        form = TextForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = TextForm()
    return render(request, 'text/post_edit.html', {'form': form})


def text_edit(request, pk):
    text = get_object_or_404(Text, pk=pk)
    if request.method == "POST":
        form = TextForm (request.POST, request.FILES, instance=text)
        if form.is_valid():
            text = form.save(commit=False)
            text.author = request.user
            text.published_date = timezone.now()
            text.save()
            return redirect('post_detail', pk=text.pk)
    else:
        form = TextForm(instance=text)
    return render(request, 'text/post_edit.html', {'form': form})
