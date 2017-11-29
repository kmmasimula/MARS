
from django.conf.urls import include,url
from django.contrib import admin

from SAT.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sat/', include('SAT.urls')),
    url(r'^$',index),
]
