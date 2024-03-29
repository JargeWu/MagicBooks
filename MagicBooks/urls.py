"""MagicBooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from Blog import views
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^admin/', admin.site.urls),
                  url(r'^index/$', views.index, name='index'),
                  url(r'^login/$', views.login, name='login'),
                  url(r'^logon/$', views.logon, name='logon'),
                  url(r'^article/$', views.article, name='article'),
                  url(r'^comment/$', views.comment, name='comment'),
                  url(r'^about/$', views.about, name='about'),
                  url(r'^read/(\d+)/$', views.view_article, name='read'),
                  url(r'^search/$', views.search, name='search'),
                  url(r'user_info/$', views.user_info, name='user_info'),
                  url(r'logout/$', views.logout, name='logout'),
                  url(r'editor/$', views.editor, name='editor'),
                  url(r'delarticle/(\d+)/$', views.delarticle, name='delarticle'),

                  url(r'mdeditor/', include('mdeditor.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
