
from django.conf.urls import include,url
from django.contrib import admin

from SAT.views import index,upload,fileupload,view,users

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sat/', include('SAT.urls')),
    url(r'^$',index),
    url(r'^upload/',upload),
    url(r'^view/',view),
    url(r'^file/',fileupload),
    url(r'^users/',users),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
	urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)