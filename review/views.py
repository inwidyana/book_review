from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Book, Review

# Create your views here.


def index(request):
    books = Book.objects.order_by('id')[0:]
    return render(request, 'review/index.html', {'user': request.user.username, 'books': books})


def book(request, book_id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            bookRetrieved = Book.objects.get(pk=book_id)
            return render(request, 'review/book.html', {'book': bookRetrieved, 'user': request.user.username})
        elif request.method == 'POST':
            try:
                user = request.user
                review = Review.objects.get(user=user)
            except:
                bookRetrieved = Book.objects.get(pk=book_id)
                review = request.POST['review']

                newReview = Review(comment=review, book=bookRetrieved, user=request.user)
                newReview.save()
                return redirect('/book/' + str(book_id))
            finally:
                bookRetrieved = Book.objects.get(pk=book_id)
                return render(request, 'review/book.html', {
                    'book': bookRetrieved,
                    'user': request.user.username,
                    'error': 'You can\'t submit more than one review'
                })

    else:
        return redirect('/login')


def signin(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'review/login.html')
    elif request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('/')
        elif request.POST['username'] and request.POST['password']:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'review/login.html', {
                    'username': request.POST['username'],
                    'errors': {
                        'username': 'You entered an invalid username or password',
                        'password': 'You entered an invalid username or password',
                    },
                })
        else:
            return render(request, 'review/login.html', {
                'username': request.POST['username'],
                'errors': {
                    'username': 'You entered an invalid username or password',
                    'password': 'You entered an invalid username or password',
                },
            })


def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'review/register.html')
    elif request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('/')
        elif request.POST['username'] and request.POST['password'] and request.POST['confirm_password'] and \
                request.POST['name']:
            if User.objects.filter(username=request.POST['username']).exists():
                return render(request, 'review/register.html', {
                    'username': request.POST['username'],
                    'errors': {
                        'username': 'This username has been taken',
                    },
                })

            user = User.objects.create_user(request.POST['name'], None, request.POST['password'])
            user.username = request.POST['username']
            user.save()
            login(request, user)
            return redirect('/')
        else:
            variables = ['username', 'name', 'password', 'confirm_password']
            data = {}

            for i in variables:
                if not bool(request.POST[i]):
                    data[i] = 'Please enter a ' + ('password' if i == 'confirm_password' else i)

            if not request.POST['password'] == request.POST['confirm_password']:
                data['password'] = 'The passwords does not match'
                data['confirm_password'] = 'The passwords does not match'

            return render(request, 'review/register.html', {
                'username': request.POST['username'],
                'errors': data,
            })


def signout(request):
    user = logout(request)
    return redirect('/')
