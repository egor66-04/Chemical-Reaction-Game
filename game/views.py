from django.shortcuts import render
from elements.models import Element
import json
from django.http import JsonResponse, HttpResponse
from gtts import gTTS
import os
def game(request):
    elements = Element.objects.all()  # Получаем все элементы
    return render(request, 'game/game.html', {'elements': elements})



def text_to_speech(request):
    if request.method == 'POST':
        # Получаем текст из запроса
        data = json.loads(request.body)
        text = data.get('text', '')

        if not text:
            return JsonResponse({'error': 'No text provided'}, status=400)

        # Генерация речи с помощью gTTS
        tts = gTTS(text=text, lang='ru')
        file_path = 'speech.mp3'
        tts.save(file_path)

        # Отправка сгенерированного файла клиенту
        with open(file_path, 'rb') as audio_file:
            response = HttpResponse(audio_file.read(), content_type='audio/mpeg')
            response['Content-Disposition'] = 'attachment; filename="speech.mp3"'
            return response
    return JsonResponse({'error': 'Invalid request'}, status=400)
