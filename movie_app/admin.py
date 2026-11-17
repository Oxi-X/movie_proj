from django.contrib import admin

from movie_app.models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('rating','name','year','budget','slug')
    list_filter = ('year',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}
    list_editable = ('year','budget')
    ordering = ('-rating','name')
    list_per_page = 2
