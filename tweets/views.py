from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Tweet

# Create your views here.
def home_view(req, *arg, **kargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(req, "pages/home.html", context={}, status=200)

def tweet_list_view(req, *arg, **kargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view(req, tweet_id, *arg, **kargs):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    data = {
        "id": tweet_id,
        "content": tweet.content,
        "image": tweet.image.url
    }
    return JsonResponse(data)

