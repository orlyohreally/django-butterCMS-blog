from django.http import Http404
from django.shortcuts import render
from butter_cms import ButterCMS
from website.settings import BUTTERCMS_TOKEN

client = ButterCMS(BUTTERCMS_TOKEN)


def home(request, page=1):
    response = client.posts.all({'page_size': 10, 'page': page})

    try:
        recent_posts = response['data']
    except:
        raise Http404('Page not found')

    return render(request, 'posts-list.html', {
        'recent_posts': recent_posts,
    })


def post(request, slug):
    try:
        response = client.posts.get(slug)
        post = response['data']
    except:
        raise Http404('Post not found')
    return render(request, 'post.html', {
        'post': post
    })


def index(request):
    return render(request, 'index.html', {
        'butterCMS_token': BUTTERCMS_TOKEN
    })
