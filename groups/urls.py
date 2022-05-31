from django.urls import path,re_path,include
from rest_framework import routers
from . import views

router=routers.DefaultRouter()

router.register(r'group',views.GroupViewSet)
router.register(r'groupmember',views.GroupmemberViewSet)


app_name='groups'

urlpatterns=[
    path('api/',include(router.urls)),
    path('', views.GroupsList.as_view(),name='all'),
    path('new/',views.CreateGroup.as_view(),name='create'),
    path('posts/in/<slug:slug>/', views.SingleGroup.as_view(), name="single"),
    re_path(r"^join/(?P<slug>[-\w]+)/$", views.JoinGroup.as_view(), name="join"),
    re_path(r"^leave/(?P<slug>[-\w]+)/$", views.LeaveGroup.as_view(), name="leave"),
]

