#-*- coding: utf-8 -*-

from django.conf.urls import url,include
from django.contrib import admin
from content import urls,views
from django.conf.urls.static import static
from django.conf import settings
from content import views as content_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',content_views.fms_list, name="index"),
    url(r'accounts/', include('accounts.urls')),
    url(r'fms/', include('content.urls')),

    url(r'^type/add$', views.type_add,name='type_add'),
    url(r'^type/del/(?P<id>\d+)$', views.type_del,name='type_del'),

    url(r'^get/email$',views.get_email, name='get_email'),
    url(r'^send/emails$',views.send_mails, name='send_mails'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
