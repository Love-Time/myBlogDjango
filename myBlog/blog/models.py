from django.db import models


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
    cat = models.ForeignKey("Category", on_delete=models.RESTRICT)
    is_published = models.BooleanField(default=True)


class Image(models.Model):
    image = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)



class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
