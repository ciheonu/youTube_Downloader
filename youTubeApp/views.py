from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from pytube import YouTube
from pytube.exceptions import VideoUnavailable


def home(request):
    if request.method == 'POST':
        url = request.POST["link"]
        try:
            my_video = YouTube(url)

            data = {
                'title': str(my_video.title),
                'thumbnail': str(my_video.thumbnail_url),
            }
            my_video = YouTube(url).streams.get_highest_resolution()
            my_video.download()
            return render(request, 'index.html', data)
        except VideoUnavailable:
            HttpResponseRedirect('home')

    else:
        data = {}

    return render(request, 'index.html')
