from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_event/', views.add_event_view, name='EventAdd'),
    path('Event_List/', views.Event_list_view, name='My_Events'),
    path('edit_event/<int:event_id>/', views.edit_event_view, name='edit_event'),
    path('delete_event/<int:event_id>/', views.delete_event_view, name='delete_event'),
    path('event/<int:event_id>/', views.detail_event_view, name='event_detail'),
]
