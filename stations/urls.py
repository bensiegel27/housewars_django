from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^(?P<station_number>[0-9]+)/$', views.station_selection, name='station_selection'),
]
