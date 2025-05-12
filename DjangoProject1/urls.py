from django.contrib import admin
from django.urls import path, include
from core.views import index
from core.views import login
from core.views import error
from core.views import blank
from core.views import buttons
from core.views import cards
from core.views import charts
from core.views import register
from core.views import tables
from core.views import utilities_color
from core.views import utilities_other
from core.views import utilities_border
from core.views import utilities_animation
from core.views import forgotpassword
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    path('login/', login, name='login'),

    path('register/', register, name='register'),

    path('forgotpassword/', forgotpassword, name='forgot_password'),

    path('cards/', cards, name='cards'),

    path('charts/', charts, name='charts'),

    path('tables/', tables, name='tables'),

    path('error/', error, name='error'),

    path('blank/', blank, name='blank'),

    path('buttons/', buttons, name='buttons'),

    path('utilities-color/', utilities_color, name='utilities-color'),

    path('utilities-other/', utilities_other, name='utilities-other'),

    path('utilities-border/', utilities_border, name='utilities-border'),

    path('utilities-animation/', utilities_animation, name='utilities-animation'),








]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
