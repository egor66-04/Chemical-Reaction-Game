from django.shortcuts import render
from .models import Element
from django.db.models import Q
from django.http import HttpResponse
from gtts import gTTS
import os

# Главная страница
def home(request):
    return render(request, 'home.html')  # Этот шаблон будет отображать главную страницу

# Таблица Менделеева (страница с элементами)
def element_list(request):
    # Получаем категорию из GET-запроса, по умолчанию "Все элементы"
    category = request.GET.get('category', 'Все элементы')

    # Получаем поисковый запрос из GET-запроса (в нижнем регистре)
    search_query = request.GET.get('search', '').lower()

    # Начальная выборка всех элементов
    elements = Element.objects.all()

    # Фильтрация по категории (если выбрана не "Все элементы")
    if category != 'Все элементы':
        elements = elements.filter(category__icontains=category)

    # Фильтрация по поисковому запросу (нечувствительно к регистру)
    if search_query:
        elements = elements.filter(Q(name__icontains=search_query) | Q(symbol__icontains=search_query))

    # Рендерим страницу с элементами
    return render(request, 'elements/element_list.html', {
        'elements': elements,
        'category': category,
        'search_query': search_query
    })

# Преобразование текста в речь
def text_to_speech(request):
    # Получаем текст из параметров GET-запроса
    text = request.GET.get('text', '')

    if text:
        # Используем gTTS для преобразования текста в речь
        tts = gTTS(text, lang='ru')
        file_path = "/tmp/speech.mp3"
        tts.save(file_path)

        # Читаем сохранённый файл и отправляем его как ответ
        with open(file_path, 'rb') as speech_file:
            response = HttpResponse(speech_file.read(), content_type='audio/mpeg')
            response['Content-Disposition'] = 'inline; filename="speech.mp3"'

        # Удаляем файл после отправки
        os.remove(file_path)
        return response
    else:
        return HttpResponse("No text provided for speech", status=400)
