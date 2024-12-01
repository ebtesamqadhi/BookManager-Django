from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import Bookform, Categoryform

# Create your views here.

def index(request):
    if request.method == 'POST':
        add_book = Bookform(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_category = Categoryform(request.POST)
        if add_category.is_valid():
            add_category.save()

    context = {
        'categorys': Category.objects.all(),
        'books': Book.objects.all(),
        'form' : Bookform(),
        'formcate' : Categoryform(),
        'allbook': Book.objects.filter(active=True).count(), # يجيب عدد الكتب المتاحة 
        'availblebooks': Book.objects.filter(state='availble').count(), # يجيب عدد الكتب المتوفرة 
        'soldbooks': Book.objects.filter(state='sold').count(), # يجيب عدد الكتب المبتعة 
        'rentalbooks': Book.objects.filter(state='rental').count(), # يجيب عدد الكتب المستأجرة 
    }
    return render (request, 'pages/index.html', context)

def books(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title) # ابحث بالعنوان لو اشتي بغيره اكتب الاسم اللي موجود بالمودل

    context = {
        'categorys': Category.objects.all(),
        'books': search,
        'formcate' : Categoryform(),
    }
    return render (request, 'pages/books.html', context)

def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        books_update = Bookform(request.POST, request.FILES, instance=book_id)
        if books_update.is_valid:
            books_update.save()
            return redirect('/')
    else:
        books_update = Bookform(instance=book_id)
    context = {
        'form':books_update,
    }
    return render (request, 'pages/update.html', context)

def delete(request, id):
    book_del = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_del.delete()
        return redirect('/')
    return render (request, 'pages/delete.html')