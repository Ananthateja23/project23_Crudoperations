from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def display_topic(request):
    LOT=Topic.objects.all()
    d={'topic':LOT}
    return render(request,'display_topic.html',context=d)

def display_webpage(request):
    #LOW=Webpage.objects.all()
    #LOW=Webpage.objects.filter(topic_name='Cricket')
    #LOW=Webpage.objects.exclude(topic_name='Cricket')
    #LOW=Webpage.objects.all()[:2]
    #LOW=Webpage.objects.all()[2:]
    #LOW=Webpage.objects.all().order_by('name')
    #LOW=Webpage.objects.all().order_by('-name')
    #LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length('name').desc())
    d={'webpage':LOW}
    return render(request,'display_webpage.html',context=d)

def display_access(request):
    LOA=AccessRecord.objects.all()
    #LOA=AccessRecord.objects.filter(date__gt='2022-07-23')
    #LOA=AccessRecord.objects.filter(date__gte='2022-07-23')
    #LOA=AccessRecord.objects.filter(date__lt='2022-07-23')
    #LOA=AccessRecord.objects.filter(date__lte='2022-07-23')
    d={'access':LOA}
    return render(request,'display_access.html',context=d)