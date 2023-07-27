from django import forms
from .models import Book, Categories, Concurrent

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__' # using all fields in the form

class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'

class ConcurrentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Concurrent
        fields = ['lastname', 'firstname', 'sex', 'university', 'domain', 'password']

class LoginForm(forms.Form):
    id = forms.CharField(label='ID', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

# forms.py
class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)


class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class CategoriesAdminForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'

class ConcurrentAdminForm(forms.ModelForm):
    class Meta:
        model = Concurrent
        fields = '__all__'