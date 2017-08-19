from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^', include('unihackDjango.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

