
from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, ProfileView, generate_new_password

app_name= UsersConfig.name

urlpatterns = [

    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'), # Нужно создавать контроллер вручную
    path('profile/', ProfileView.as_view(), name='profile'), # Нужно создавать контроллер вручную
    path('profile/genpassword', generate_new_password, name='generate_new_password'), # Нужно создавать контроллер вручную (функцию для генерации пароля)

]