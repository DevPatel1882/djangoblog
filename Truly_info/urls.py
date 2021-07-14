"""Truly_info URL Configuration

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
from django.urls import path,include
from.import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.contrib.sitemaps.views import sitemap
from info_data.sitemaps import Blog_PostSitemap

sitemaps = {
    "Blog_Post":Blog_PostSitemap,

}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path("sitemap.xml/", sitemap, {"sitemaps":sitemaps}, name="sitemap"),
    path('404/',views.Error_Page,name='404'),
    path('master/',views.master,name='master'),

    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.Blog,name='Blog'),
    path('post/<slug:slug>',views.Blog_single,name='post'),

    path('viral_videos/',views.viral_videos,name='viral_videos'),
    path('funny_images/',views.funny_images,name='funny_images'),

    path('gedgets/', views.gedgets, name='gedgets'),






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

