from django.shortcuts import render, get_object_or_404

from .models import Vlog

def allvlogs(request):
    vlogs = Vlog.objects
    return render(request , 'vlog/allvlogs.html' , {'vlogs':vlogs})

def detail(request , vlog_id):
    detailvlog = get_object_or_404(Vlog , pk=vlog_id)
    return render(request ,'vlog/detail.html',{'vlog':detailvlog})
