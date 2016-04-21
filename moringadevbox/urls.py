"""moringadevbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mdevbox import views
from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^addportfolio/', views.new_profile, name="register"),
    url(r'^$', 'mdevbox.views.home', name='home'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^get/(?P<id>\d+)/$', views.fetch_one, name="fetch_one"),
    url(r'^portfolios/$' ,views.fetch_all, name='fetch_all'),
    url(r'^sendoffer/(?P<id>\d+)/$', views.offer, name="offer"),
    url(r'^jobs/$' ,views.displayjobs, name='fetch_all'),
    url(r'^viewjob/(?P<id>\d+)/$', views.get_job, name="offer"),
    url(r'^apply/(?P<id>\d+)/$', views.applyjob, name="offer"),
    url(r'^postjob/$', views.newjob, name="post_job"),
]
