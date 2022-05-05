"""iert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path,include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
         path('',views.index,name='index'),
         path('movie',views.movie,name='movie'),
         #path('rating',views.rating,name='rating'),
         path('xmen',views.xmen,name='review'),
         path('spm2',views.spm2,name='review'),
         path('spm3',views.spm3,name='review'),
         path('valkyrie',views.valkyrie,name='review'),
         path('gladiator',views.gladiator,name='review'),
         path('iceage',views.iceage,name='review'),
         path('transformers',views.transformers,name='review'),
         path('magneto',views.magneto,name='review'),
         path('login/xmen',views.xmen,name='review'),
         path('login/spm2',views.spm2,name='review'),
         path('login/spm3',views.spm3,name='review'),
         path('login/valkyrie',views.valkyrie,name='review'),
         path('login/gladiator',views.gladiator,name='review'),
         path('login/iceage',views.iceage,name='review'),
         path('login/transformers',views.transformers,name='review'),
         path('login/magneto',views.magneto,name='review'),
         path('sub',views.sub,name='review'),
         
]
