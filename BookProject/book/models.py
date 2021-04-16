from django.db import models

# Create your models here.



class Book(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=120)
    price=models.IntegerField(default=50)
    pages=models.IntegerField()
    category=models.CharField(max_length=120)


    def __str__(self):
        return self.book_name
