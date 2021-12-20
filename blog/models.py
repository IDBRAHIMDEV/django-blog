from django.db import models
from django.db.models.fields import CharField, DateTimeField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey, ManyToManyField

PUBLISHED = (
    (0, "Disable"),
    (1, "Enable"),
)
# Create your models here.
class Article(models.Model):

    title = CharField(max_length=120)
    description = TextField(null=True)
    published = IntegerField(null=True, choices=PUBLISHED)
    category = ForeignKey("Category", null=True, on_delete=models.SET_NULL)
    tags = ManyToManyField("Tag")
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):

    published = IntegerField(max_length=1, null=True, default=0, choices=PUBLISHED)
    name = CharField(max_length=50)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):

    name = CharField(max_length=50)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
