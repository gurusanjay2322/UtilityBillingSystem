from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
class AuthSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_system'