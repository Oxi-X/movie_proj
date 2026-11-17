from django.contrib import admin

from movie_app.models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name','rating','year','budget','slug')
    list_filter = ('year',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}
    list_editable = ('rating','year','budget')
