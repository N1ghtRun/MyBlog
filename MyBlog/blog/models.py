from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField()
    title = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    slug = models.SlugField(blank=True)
    content = RichTextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse("post", kwargs={"category": self.category.slug,
                                       "slug": self.slug})

    def __str__(self):
        return self.title
