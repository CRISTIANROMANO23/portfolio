
from django.urls import path

from . import views


urlpatterns = [
    path('' , views.allvlogs , name ='allvlogs'),
    path('<int:vlog_id>/',views.detail , name='detail'), #para poder entrar a las pag de los vlogs
]
