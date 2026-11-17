from . import views
from django.urls import path,include
import debug_toolbar

urlpatterns = [
    path('', views.show_all_movies,name='movies'  ),
    path('movie/<str:slug_movie>', views.show_one_movie,name='movie-detail'),
    path('__debug__/', include(debug_toolbar.urls)),
]