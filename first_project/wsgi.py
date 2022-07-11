import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

application = get_wsgi_application()

# WSGI - стандарт обмена данными между веб-сервером (backend) и веб-приложением (frontend).
# Основное использование развертывания с помощью WSGI — это вызываемое приложение, которое сервер приложений использует
# для связи с вашим кодом. Обычно он предоставляется как объект с именем application в модуле Python, доступном для
# сервера.


# Нужен прежде всего для того что бы ранить проект
# помогает  приложению джанго контактировать с джанго, благодаря ему может контактировать с любым веб сервером