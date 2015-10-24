from django.conf.urls import patterns, include, url
from django.contrib import admin
from helpothers.views import HomeView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls))
)
