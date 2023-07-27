from django.contrib import admin
from .models import Book,Categories,Concurrent
from .models import Categories
# Register your models here.

from .forms import BookAdminForm, CategoriesAdminForm, ConcurrentAdminForm

class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm

class CategoriesAdmin(admin.ModelAdmin):
    form = CategoriesAdminForm

class ConcurrentAdmin(admin.ModelAdmin):
    form = ConcurrentAdminForm

admin.site.register(Book, BookAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Concurrent, ConcurrentAdmin)


