from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import BookForm
from .models import Book


# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Registrar el usuario
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('books')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm(), 'error': 'El usuario ya existe'})
        return render(request, 'signup.html', {'form': UserCreationForm(), 'error': 'Las contraseñas no coinciden'})

def books(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'books.html', {'books': books})

def create_book(request):
    if request.method == 'GET':
        return render(request, 'create_book.html', {'form': BookForm})
    else:
        try:
            form = BookForm(request.POST)
            new_book = form.save(commit=False)
            new_book.user = request.user
            new_book.save()
            return redirect('books')
        except ValueError:
                return render(request, 'signup.html', {'form': BookForm(), 'error': 'Porfavor ponga datos validos'})

def book_deail(request, book_id):
    if request.method == 'GET':
        book = get_object_or_404(Book, pk=book_id,user=request.user)
        form = BookForm(instance=book)
        return render(request, 'book_detail.html', {'book': book, 'form': form})
    else:
        try:
            book = get_object_or_404(Book, pk=book_id, user=request.user)
            form = BookForm(request.POST, instance=book)
            form.save()
            return redirect('books')
        except ValueError:
            return render(request, 'book_detail.html', {'book': book, 'form': form, 'error': 'Error actualizando libro'})

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'form': AuthenticationForm(), 'error': 'El usuario o la contraseña no son incorrectos'})
        else:
            login(request, user)
            return redirect('books')


