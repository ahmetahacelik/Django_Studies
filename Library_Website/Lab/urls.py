from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^Projects/(?P<pid>[\w]+)', views.DisplaySingleProject),
    url(r'^Projects/$',views.DisplayAllProjects),
    url(r'^People/(?P<pid>[\w]+_[\w]+)', views.DisplaySinglePerson),
    url(r'^People/$', views.DisplayAllPeople),
    url(r'^Blogs/$', views.DisplayBlogs),

    url(r'^Blogs/Create', views.DisplayPost),


    url(r'^$',views.Home)

]
