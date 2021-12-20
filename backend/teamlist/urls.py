from django.urls import path
from .views import CreateUserView , EditUserView , ListUserView , DeleteUserView

urlpatterns = [
    path('create/' , CreateUserView.as_view() , name='create'),
    path('<pk>/update' , EditUserView.as_view() , name='edit'),
    path('list/' , ListUserView.as_view() , name='list'),
    path('<pk>/delete' , DeleteUserView.as_view() , name='delete')
]
