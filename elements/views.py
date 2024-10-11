from django.shortcuts import render
from .models import Element
from django.db.models import Q

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

from django.shortcuts import render
from .models import Element

# Главная страница
def home(request):
    return render(request, 'home.html')  # Этот шаблон будет отображать главную страницу

# Таблица Менделеева
def element_list(request):
    elements = Element.objects.all()  # Получаем все элементы
    return render(request, 'elements/element_list.html', {'elements': elements})  # Передаём их в шаблон

