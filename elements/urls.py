from django.urls import path
from elements import views  # Импорт представлений

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('ptable/', views.element_list, name='element_list'),  # Таблица Менделеева
    path('text_to_speech/', views.text_to_speech, name='text_to_speech'),  # Озвучка текста
]
