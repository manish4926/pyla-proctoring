from django.urls import path
#from ../.users import views

from users import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
#    path('index/', views.Users.index, name='index'),
 #   path('register/', views.Users().registerUser, name='registerUser'),
    path('login/', views.login, name='loginUser'),
    # path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('get_data/', views.getLoginData, name='getLoginData'),
    
]