from django.shortcuts import render
from .forms import PhotoForm
from . models import Photo
# Create your views here.
def index(request):
    
    all_objects = Photo.objects.all()

    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            print('form submitted')
            form.save()

        else:
            print(form.errors)
    form = PhotoForm()
    return render(request,'index.html',{'form':form,'all_objects':all_objects})


def js_trial(request):
    all_objects = Photo.objects.all()

    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            print('form submitted')
            form.save()

        else:
            print(form.errors)
    form = PhotoForm()
    return render(request,'trial.html',{'form':form,'all_objects':all_objects})


def datatable(request):
    
    return render(request,'datatable.html')