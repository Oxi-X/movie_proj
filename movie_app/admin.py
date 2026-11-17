from django.contrib import admin, messages
from django.db.models import QuerySet
from movie_app.models import Movie

# Register your models here.
class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating_filter'

    def lookups(self, request, model_admin):

        return (
            ('50<', 'Высокий рейтинг'),
            ('50', 'Средний рейтинг'),
            ('50>', 'Низкий рейтинг'),
        )

    def queryset(self, request, queryset: QuerySet):
        if self.value()=='50<':
            return queryset.filter(rating__gt=50)
        if self.value()=='50':
            return queryset.filter(rating=50)
        if self.value()=='50>':
            return queryset.filter(rating__lt=50)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name','rating','year','currency','budget','slug', 'raiting_status')# Поля, которые будут отображаться в списке объектов в админке
    list_filter = ('year', 'currency', RatingFilter)# Фильтр по полям. В админке появится фильтр по году
    search_fields = ('name','year','budget','currency')#Поиск по полям.Строка поиска в админке
    prepopulated_fields = {'slug':('name',)}# Автоматическое заполнение поля slug на основе поля name
    list_editable = ('rating','year','currency','budget')# Разрешает редактирование полей в списке объектов
    ordering = ('-rating','name')# Сортировка по полям. '-' означает сортировку по убыванию
    list_per_page = 5# Количество объектов на странице в админке
    actions = ('set_rubles','set_euros','set_dollars')# Добавление действий в админку для изменения валюты у выбранных объектов
    

    @admin.display(ordering='rating',description='Status Movie')
    def raiting_status(self,movie:Movie):
        if movie.rating > 50:
            return 'Хороший фильм'
        elif movie.rating < 50:
            return 'Плохой фильм'
        else:
            return 'Нормальный фильм'

    @admin.action(description='Установить валюту в рубли')
    def set_rubles(self,requeast, qs:QuerySet):
        count_update = qs.update(currency=Movie.RUBLE)
        self.message_user(requeast,
                          f'Было оновлено {count_update} записей',
                          messages.INFO)

    @admin.action(description='Установить валюту в евро')
    def set_euros(self,requeast, qs:QuerySet):
        count_update = qs.update(currency=Movie.EURO)
        self.message_user(requeast,
                          f'Было оновлено {count_update} записей',
                          messages.INFO)

    @admin.action(description='Установить валюту в доллары')
    def set_dollars(self,requeast, qs:QuerySet):
        count_update = qs.update(currency=Movie.DOLLAR)
        self.message_user(requeast,
                          f'Было оновлено {count_update} записей',
                          messages.INFO)
