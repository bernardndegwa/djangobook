from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sections.views.home_page', name='home_page'),
    url(r'^sections/(\d+)/$', 'sections.views.view_section',name='view_section'),
    url(r'^sections/(\d+)/add_user$', 'sections.views.add_user',name='add_user'),
    url(r'^sections/new$', 'sections.views.new_user', name='new_user'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
)
