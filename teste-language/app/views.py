from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def index(request):
    trans = translate(language='pt-br')
    return render(request, 'index.html', {'trans': trans})

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello') #identifica o que mudar
    finally:
        activate(cur_language)
    return text