from django.shortcuts import render, redirect
from .models import Category, Photo

# Create your views here.


def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {
        'categories': categories,
        'photos': photos
    }
    return render(request, 'photo/gallery.html', context)

def addPhoto(request):
    categories = Category.objects.all()

    if request.method =='POST':
        photo = Photo.objects.create(
            category = Category.objects.get(id=request.POST['category']),
            description = request.POST['description'],
            image= request.FILES['img']
        )
        return redirect('gallery')

    context = {
        'categories': categories
    }
    return render(request, 'photo/add.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)

    context = {
        'photo': photo
    }
    return render(request, 'photo/photo.html', context)