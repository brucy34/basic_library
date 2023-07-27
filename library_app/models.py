from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Book(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    yearOfRelease = models.IntegerField()
    editions = models.IntegerField()
    pageNumber = models.IntegerField()
    id_category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Concurrent(models.Model):
    id = models.CharField(max_length=20, primary_key=True, editable=False)  # Custom ID field
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    university = models.CharField(max_length=200)
    domain = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def save(self, *args, **kwargs):
        # Generate the custom ID
        id_prefix = self.lastname[:3].upper() + '-' + self.firstname[:3].upper() + '-AFPEC-00'
        id_suffix = str(len(self.university) + len(self.domain))
        self.id = id_prefix + id_suffix
        # if not self.pk:  # Only hash the password when creating a new instance
        self.password = make_password(self.password)
        super(Concurrent, self).save(*args, **kwargs)