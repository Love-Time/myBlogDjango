from django.db import models


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    preview = models.ImageField( blank=True, null=True)
    cat = models.ForeignKey("Category", on_delete=models.RESTRICT)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='photos/%y/%m/%d/')
    description = models.CharField(null=True, blank=True, max_length=50)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, default=4)
    post = models.ForeignKey('News', on_delete=models.CASCADE, blank=True, null=True)
    is_published = models.BooleanField(default=True)


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title
