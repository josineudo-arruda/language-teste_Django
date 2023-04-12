from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def home(request):
    # trans = _('hello')
    trans = translate(language='fr')
    return render(request, 'home.html', {'trans': trans})

def item(request):
    return render(request, 'item.html')

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello') #identifica o que mudar
    finally:
        activate(cur_language)
    return text