"""leprojet URL Configuration."""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^classes/', include('classes.urls')),
    url(r'^courses/', include('courses.urls')),
]
