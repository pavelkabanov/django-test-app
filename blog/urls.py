from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.main, name='main'),

    url(r'^posts/$', views.posts, name='posts'),
    url(r'^users/$', views.users, name='users'),
    url(r'^comments/$', views.comments, name='comments'),

    url(r'^post/edit/(?P<pk>[0-9]+)/$', views.post_edit, name='post_edit'),
    url(r'^user/edit/(?P<pk>[0-9]+)/$', views.user_edit, name='user_edit'),
    url(r'^comment/edit/(?P<pk>[0-9]+)/$', views.comment_edit, name='comment_edit'),

    url(r'^post/delete/(?P<pk>[0-9]+)/$', views.post_delete, name='post_delete'),
    url(r'^user/delete/(?P<pk>[0-9]+)/$', views.user_delete, name='user_delete'),
    url(r'^comment/delete/(?P<pk>[0-9]+)/$', views.comment_delete, name='comment_delete'),
]
