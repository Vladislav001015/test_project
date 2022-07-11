from django.apps import AppConfig

# немного изменили путь, чтобы сеттинги видели наши приложения

# хранится название нашей модельки и запускается сразу после создания
class MusicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.music'
