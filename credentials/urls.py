from . import views
from django.urls import path


urlpatterns = [

    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('new_page',views.new_page,name='new_page'),
    path('form', views.form, name='form'),
    # path('add/',views.StudentCreateView.as_view(),name='student_add'),
    # path('<int:pk>/',views.StudentUpdateView.as_view(),name='student_change'),

]