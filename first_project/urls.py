from django.contrib import admin
from django.urls import path, include

from applications import music

#  при импорте просто зажимаем alt + enter и выбираем откуда импортировать
# подключили удаленные пути, так как в самом начале все равно пройдет через корневой юрл
# маршрутизатор (указатель на определенный ресурс)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('applications.music.urls')),
]
