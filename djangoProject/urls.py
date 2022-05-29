from django.contrib import admin
from django.urls import path,include
from accounts import views,urls as acc_urls
from posts import urls as post_urls
from groups import urls as group_urls
from django.contrib.auth import urls
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include(acc_urls,namespace='accounts')),
    path('',views.Base.as_view()),
    path('accounts/',include('django.contrib.auth.urls')),
    path('bye/',views.Bye.as_view(),name='bye'),
    path('hello/',views.Hello.as_view(),name='hello'),
    path('groups/',include(group_urls,namespace='groups')),
    path('posts/', include(post_urls, namespace='posts')),
    path('about_us/',views.About.as_view(),name='about')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns