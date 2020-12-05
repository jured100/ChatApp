"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

'''
from message.views import home_view #, RecipesView, RecipesAdvancedView, ProfileView

from Recipes.views import TopView, register_view, login_view, template_view, addcomment_view
from Recipes.views import dodajrecept_view, dodajpostopek_view, dodajsestavina_view, addrating_view
from Recipes.views import menjajgeslo_view, menjajime_view
from Recipes.models import Vrste,Postopki,Ocene,Sestavine,Slike,Komentarji,Recepti,ReceptiSestavine
'''

#from CustomUser.models import CustomUser

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('message.urls')),
]