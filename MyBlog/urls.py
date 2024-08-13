
from django.contrib import admin
from django.urls import path
from . import views

appname = 'MyBlog'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.index,name='index'),
    path('post/<str:slug>',views.detail, name='detail'),
    path('contact/', views.contact ,name='contact'),
    path('about/',views.aboutus,name='about'),
    path('',views.login,name='login'),
    path('logout/',views.logoutUser,name='logoutUser'),
    path('signup/',views.signup,name='signup'),
    path('post/<str:slug>/comments/',views.commentview,name='comment')
]
