from django.shortcuts import render
from elements.models import Element

def game(request):
    elements = Element.objects.all()  # Получаем все элементы
    return render(request, 'game/game.html', {'elements': elements})
