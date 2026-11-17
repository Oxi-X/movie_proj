from django.contrib import admin

from movie_app.models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name','rating','year','budget','slug', 'raiting_status')
    list_filter = ('year',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}
    list_editable = ('rating','year','budget')
    ordering = ('-rating','name')
    list_per_page = 5

    @admin.display(ordering='rating',description='Status Movie')
    def raiting_status(self,movie:Movie):
        if movie.rating > 50:
            return 'Хороший фильм'
        elif movie.rating < 50:
            return 'Плохой фильм'
        else:
            return 'Нормальный фильм'
