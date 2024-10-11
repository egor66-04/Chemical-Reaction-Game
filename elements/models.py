from django.db import models

class Element(models.Model):
    symbol = models.CharField(max_length=5)  # Химический символ
    name = models.CharField(max_length=100)  # Название элемента
    atomic_number = models.IntegerField()  # Порядковый номер
    category = models.CharField(max_length=100)  # Категория (например, благородный газ)
    description = models.TextField()  # Описание элемента
    application = models.TextField()  # Применение элемента
    fact = models.TextField()  # Интересный факт об элементе
    wiki_link = models.URLField()  # Ссылка на Википедию

    def __str__(self):
        return f"{self.name} ({self.symbol})"
