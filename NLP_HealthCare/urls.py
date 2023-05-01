"""NLP_HealthCare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('articles1/<int:id>', views.articles, name='articles_id'),
    path('articles', views.articles, name='articles'),
    path('articles/<int:id>', views.articles_page, name='articles_pages'),
    path('tags/<slug:tag>/<int:page>', views.articles_page_w_tag, name='articles_page_w_tag'),
    path('article/<slug:name>', views.show_article, name='show_article'),
    path('qa_articles', views.qa_main, name='qa_main'),
]
