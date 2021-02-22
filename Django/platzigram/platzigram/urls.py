"""platzigram URL Configuration

The `urlpatterns` list routes URLs to local_views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function local_views
    1. Add an import:  from my_app import local_views
    2. Add a URL to urlpatterns:  path('', local_views.home, name='home')
Class-based local_views
    1. Add an import:  from other_app.local_views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""Platzigram URLs module."""


from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from platzigram import views as local_views
from posts import views as posts_views

def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Hello, world!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', local_views.hello_world),
    path('hi/', local_views.hi),
    path('sort_integers/', local_views.sort_integers),
    path('bye/<str:name>/<int:age>/',local_views.bye),
    path('posts/', posts_views.list_posts),
]
