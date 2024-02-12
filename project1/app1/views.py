from django.shortcuts import render
import logging


logger = logging.getLogger(__name__)

# Create your views here.
def index(request):

    logger.info('Пользователь посетил главную страницу')
    return render(request, 'index.html')

def about(request):

    logger.info('Пользователь посетил страницу "О себе"')
    return render(request, 'about.html')
