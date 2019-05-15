from django.shortcuts import render

from .models import Job
def home(request):
    jobs = Job.objects #va a agarrar todos los objectos de la database y convertirlos en objeto de python
    return render(request ,'jobs/home.html')
