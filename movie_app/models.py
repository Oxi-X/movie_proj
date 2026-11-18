from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator 



# Create your models here.
class Director(models.Model):
    first_name= models.CharField(max_length=100,null=False)
    last_name= models.CharField(max_length=100,null=False)
    email = models.EmailField(null=True)    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'



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
    rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=100000)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUBLE)
    slug = models.SlugField(default='', null=False)
    director = models.ForeignKey(
        Director,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'