from pathlib import Path

# Путь до текущей директории
BASE_DIR = Path(__file__).resolve().parent.parent #
# /home/vlad/Python/notes_for_python/new_python/first_app/first_django_project

# секретный ключ вашего проекта, для каждого уникален
SECRET_KEY = 'django-insecure-a7^u8g3g+vuzk30labwn5*ri+9%^q0l0)6+wk8$ufr!6jff##@'

# режим отладки, показывает явные ошибки пока включен, как изменим на False, будет просто выдавать ошибку типа 404
DEBUG = True # например not found (но так же попребует что бы мы указали наши  ALLOWED_HOSTS) ( если на сервак будем
# закидывать нужно сделать false)

# разрешенные хосты -  домены, ip адресса, для которых может работать текущий сайт
ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# установленные приложения и наши сторонние библиотеки, то есть говорим джанго какие приложения вобщем есть
INSTALLED_APPS = [
    'django.contrib.admin', # Сайт администратора.
    'django.contrib.auth', # Система аутентификации.
    'django.contrib.contenttypes', # Структура для типов контента.
    'django.contrib.sessions',  # Структура сеанса.
    'django.contrib.messages', # Структура сеанса.
    'django.contrib.staticfiles', # Фреймворк для управления статическими файлами.

    #подключим сам рест
    'rest_framework',

    # customapplications, написали так, так как они хранятся в отдельной папке для приложений
    'applications.music'
] # пока не сделаем миграции не будет доступна даже админка


# промежуточные слои, функции, которые отрабатывают между запросом и ответом (отвечает за все
# наши сессии аунтификацию безопасность токены и тд)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # предоставляет ряд проверок безопасности при обработке
    # запроса/ответа
    'django.contrib.sessions.middleware.SessionMiddleware', # Всегда имейте в виду, что файлы cookie сохраняются на
    # стороне клиента, и в зависимости от уровня безопасности браузера клиента настройка файлов cookie может иногда
    # работать, а иногда — нет.  # Django обеспечивает полную поддержку анонимных сессий.
    # Фреймворк сессий позволяет хранить и извлекать произвольные данные для каждого посетителя сайта. Он хранит
    # данные на стороне сервера и абстрагирует отправку и получение cookies. Cookies содержат идентификатор сессии,
    # а не сами данные  (куки не резиновые, у них есть лимит)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # Включает CSRF защиту, добавляя скрытое поле в POST формы и
    # проверяя значение при запросе.
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Добавляет атрибут user, который указывает текущего
    # авторизованного пользователя, для каждого объекта HttpRequest.
    'django.contrib.messages.middleware.MessageMiddleware', # Добавляет поддержку сообщений на основе кук или сессии.
    'django.middleware.clickjacking.XFrameOptionsMiddleware', #  защищает от clickjacking атак
]

# маршрутизатор вашего проекта
ROOT_URLCONF = 'first_project.urls' # где неаходится наш корневой url

# шаблоны самого джанго - настройка наших шаблонов с расширение html чтобы джанго знал где находится тот или иной файл
TEMPLATES = [ # for admin too
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'first_project.wsgi.application' # подключение WSGI


# подключение базы данных для вашего проекта, по умолчанию это скюлайт 3(рассказать чем она хуже постгреса и сказать,
# чтобы лучше юзали постгрес), но если не подключать постгрес по умодчанию будет скюлайт3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# подкинем нашу бд
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'first_test', #название бд
#         'USER': 'vlad',
#         'PASSWORD': '1',
#         'HOST': 'localhost',
#         'PORT': 5432,
#         #postgresql://db_name@host:port?user=...&password=...
#     }
# }

# валидация для пароля
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # который проверяет
        # сходство пароля и набора атрибутов пользователя.
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # который проверяет, соответствует
        # ли пароль минимальной длине.
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # который проверяет, встречается
        # ли пароль в списке общих паролей. По умолчанию он сравнивается со включенным списком из 20 000 общих
        # паролей.
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # который проверяет, не является
        # ли пароль полностью числовым.
    },
]



# язык проекта
LANGUAGE_CODE = 'en-us' # 'ru-RU'

# временная зона, сменить на 'Asia/Bishkek'
TIME_ZONE = 'UTC'

# для переводов
USE_I18N = True

USE_L10N = True

USE_TZ = True

# статика проекта, картинки, видео, аудио и тд
STATIC_URL = '/static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # При определении модели, если ни одно поле в модели не
# определено с primary_key=True, добавляется неявный первичный ключ. Тип этого неявного первичного ключа теперь можно
# контролировать с помощью параметра DEFAULT_AUTO_FIELD
