from django.db import models
from authe.models import Author
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="имя")
    def __str__(self):
        return f"{self.name}"
    class Meta():
        verbose_name = "Теги"
        verbose_name_plural = "Теги"
    

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name = "тайтл")
    body = models.TextField(max_length=1000, verbose_name= "боди")
    tags = models.ManyToManyField(Tag, related_name = 'posts', verbose_name="теги")
    author = models.ForeignKey(Author, related_name= 'posts', on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.title}"
    class Meta():
        verbose_name = "Посты"
        verbose_name_plural = "Посты"
    
    


    