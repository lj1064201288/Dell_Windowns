from django.conf.urls import include, url
from django.contrib import admin
from . import views as ov

urlpatterns = [
    # Examples:
    # url(r'^$', 'Liujun_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^/', include(admin.site.urls)),
    url(r'^taobao/', ov.do_taobao),
]