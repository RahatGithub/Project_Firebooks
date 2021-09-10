from django.db import models


class PopularBooks(models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    link = models.TextField()
    def __str__(self):
        return self.title


class Category1(models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    link = models.TextField()
    def __str__(self):
        return self.title


class Category2(models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    link = models.TextField()
    def __str__(self):
        return self.title


class Category3(models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    link = models.TextField()
    def __str__(self):
        return self.title


class TopMembers(models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    msg = models.TextField()
    def __str__(self):
        return self.email