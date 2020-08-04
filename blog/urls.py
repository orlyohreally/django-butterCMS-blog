from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='blog'),
    url(r'^(?P<slug>.*)$', views.post, name='blog_post'),
]