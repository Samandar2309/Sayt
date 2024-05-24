from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post1(TimeStampedModel):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='posts1/')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Home(TimeStampedModel):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='home/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Category(TimeStampedModel):
    title = models.CharField(max_length=212)
    category = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.title


class Tags(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Contact(TimeStampedModel):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    phone = models.CharField(max_length=212)
    message = models.TextField()

    def __str__(self):
        return self.name
#
# class Side_box(TimeStampedModel):
#     title = models.CharField(max_length=212)
#     image = models.ImageField(upload_to='sidebox/')
#     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
