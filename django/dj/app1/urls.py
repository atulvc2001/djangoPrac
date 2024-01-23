from django.urls import path
from app1 import views

urlpatterns = [
    path('fun.com/',views.fun),
    path('sample.com/',views.sam),
    path('flp/',views.flp),
    path('func/',views.func),
    path('page1/',views.page1,name='page1'),
    path('page2/',views.page2,name='page2'),
    path('page2/',views.page3,name='page3')
    
]