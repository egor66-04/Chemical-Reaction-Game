from django.contrib import admin
from django.urls import path, include
from elements import views  # Импортируем представления из приложения elements

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка Django
    path('', views.home, name='home'),  # Маршрут для главной страницы
    path('ptable/', views.element_list, name='element_list'),  # Маршрут для страницы таблицы Менделеева
    path('game/', include('game.urls')),  # Добавляем маршрут к мини-игре
]
