#import Django's function url and all our views from the blog app
from django.conf.urls import url
from . import views

#adding first URL pattern
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
