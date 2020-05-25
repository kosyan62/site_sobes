from django.shortcuts import render


def post_list(request):
    return render(request, 'text/post_list.html', {})

