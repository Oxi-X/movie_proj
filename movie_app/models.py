from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Movie(models.Model):
    EURO='eur'
    DOLLAR='usd'
    RUBLE='rub'
    CURRENCY_CHOICES = [
        (EURO,'Euro'),
        (DOLLAR,'Dollar'),
        (RUBLE ,'Ruble'),
    ]
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=100000)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUBLE)
    slug = models.SlugField(default='', null=False)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name,allow_unicode=True)
        super(Movie,self).save(*args,**kwargs)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'