
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    #path('admin/', admin.site.urls),
    path(_('admin/'), admin.site.urls),
    path('', include('lang.urls', namespace='lang'))
]

urlpatterns += i18n_patterns ( # quais sessões serão internacionalizadas
    path('', include('lang.urls', namespace='lang'))
)
