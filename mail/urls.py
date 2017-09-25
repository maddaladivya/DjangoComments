from django.conf.urls import url, include

from mail import views
from mail.views import Comment

urlpatterns = [
    url(r'^send/$', views.send, name="send"),
    url(r'^display/$', Comment.as_view()),
    url(r'^reply/(?P<ak>[0-9]+)/$', views.reply, name="reply"),
]
