"""
Definition of urls for OnlineCourse.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views


from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static #импорт функций для настройки доступа к загруженным файлам(и две строчки снизу)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^links$', app.views.links, name='links'),
    url(r'^blog$', app.views.blog, name='blog'),
    url(r'^(?P<parametr>\d+)/$', app.views.blogpost, name='blogpost'),
    url(r'^anketa$', app.views.anketa, name='anketa'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^katalog/', include('shop.urls', namespace='shop')),
    url(r'^registration$', app.views.registration, name='registration'),
    url(r'^newpost$', app.views.newpost, name='newpost'),
    url(r'^videopost$', app.views.videopost, name='videopost'),
    url(r'^users_orders$', app.views.users_orders, name='users_orders'),
    

    
    
   

  
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Войти',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
