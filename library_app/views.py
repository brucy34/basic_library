from django.shortcuts import render,redirect

# Create your views here
from django.contrib.auth.hashers import make_password, check_password
from .models import Book,Categories,Concurrent
from .forms import BookForm,CategoriesForm,ConcurrentForm,BookSearchForm,LoginForm,LoginForm
from django.db.models import Q

# display all books
def display_books(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})



# add books
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})



# search books by category,author,title and year of release
# views.py

# from django.shortcuts import render
# from .models import Book
# from .forms import 
# from django.db.models import Q

def search_books(request):
    query = request.GET.get('query')
    books = []

    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(yearOfRelease__icontains=query) |
            Q(author__icontains=query) |
            Q(id_category__title__icontains=query)
        )

    return render(request, 'search_books.html', {'books': books, 'query': query})


# add categories
def add_category(request):
    if request.method == 'POST':
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_books')
    else:
        form = CategoriesForm()
    return render(request, 'add_category.html', {'form': form})



# block a concurrent
def block_concurrent(request, concurrent_id):
    concurrent = Concurrent.objects.get(pk=concurrent_id)
    if request.method == 'POST':
        form = ConcurrentForm(request.POST, instance=concurrent)
        if form.is_valid():
            form.save()
            return redirect('display_books')
    else:
        form = ConcurrentForm(instance=concurrent)
    return render(request, 'block_concurrent.html', {'form': form, 'concurrent': concurrent})


def register_concurrent(request):
    if request.method == 'POST':
        form = ConcurrentForm(request.POST)
        if form.is_valid():
            concurrent = form.save(commit=False)
            concurrent.save()
            return redirect('login_concurrent')
    else:
        form = ConcurrentForm()
    return render(request, 'register_concurrent.html', {'form': form})

def login_concurrent(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            password = form.cleaned_data['password']
            try:
                concurrent = Concurrent.objects.get(id=id)
                if check_password(password, concurrent.password):
                    # Login successful, you can set session or other authentication here
                    return redirect('display_books')  # Replace 'home' with your home page URL
                else:
                    form.add_error(None, 'Incorrect ID or password.')
            except Concurrent.DoesNotExist:
                form.add_error(None, 'Incorrect ID or password.')
    else:
        form = LoginForm()
    return render(request, 'login_concurrent.html', {'form': form})