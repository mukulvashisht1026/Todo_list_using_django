from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
	path('todo/',views.index,name='index'),
	path('complete/<todo_id>',views.complete,name='complete'),
	path('add/',views.add,name='add'),
	path('delete/',views.delete,name='delete'),
]
