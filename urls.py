from django.urls import path
from . import views

urlpatterns=[
    path('select/',views.register ,name='student_register'),
    path('login/',views.student_login,name='student_login'),
    path('dashboard/',views.student_dashboard,name='student_dashboard'),
    path('admin/',views.admin_login,name='admin_login'),
    path('adminn/',views.enter,name='enter'),
    path('marks/',views.student_marks,name='marks'),
    path('update',views.update_marks,name='update_marks'),
    path('studentdashboard/', views.student_marks_dashboard, name='student_marks_dashboard'),

   

]