from django.conf.urls import include, url
from django.contrib import admin
from index import views as iv
from resume import resume_url
from outer_net import net_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'Liujun_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', iv.do_index),
    url(r'^resume/', include(resume_url)),
    url(r'^outer/', include(net_urls)),
]
