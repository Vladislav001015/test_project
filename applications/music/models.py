from django.contrib.auth.models import User
from django.db import models

# модели это основа, то с чего начинается приложение, сначала продумываем архитектуру базы данных, затем приступаем
# к реализации, мы будем реализовывать бэк для песен, в которых будут категории и сами песни
# создадим модель для категорий


# class Music(models.Model):
#     id_vlad = models.AutoField(primary_key=True, )
#     title = models.CharField(max_length=255, verbose_name='Название')
#     description = models.TextField()
#     # description2_n = models.TextField(null=True) # Это означает, что форме требуется значение, а базе данных нет
#     # description3_b = models.TextField(blank=True) # то поле не будет обязательным
#     description4 = models.TextField(null=True, blank=True) # Комбинация этих двух вариантов встречается так часто,
#     # потому что, как правило, если вы собираетесь разрешить пустое поле в своей форме, вам также понадобится база
#     # данных, чтобы разрешить NULLзначения для этого поля.
#
#     country = models.CharField(max_length=30, choices=COUNTRY)
#     duration = models.IntegerField()
#     duration2 = models.IntegerField(default=1)

    # f = models.OneToOneField
    # f models.ManyToManyField
    #
    # def __str__(self):
    #     return f'{self.title} {self.country}'
    #
    # class Meta:
    #     verbose_name = 'Продукт'
    #     verbose_name_plural = 'Продукты'


class Category(models.Model):
    title = models.SlugField(primary_key=True)

    def __str__(self):
        return f'{self.title}'


class Music(models.Model):
    COUNTRY = (
        ('KG', 'Кыргызстан'),  # 1 - то что запишется в бд, 2 - то что мы видим
        ('KZ', 'Казахстан'),
        ('RU', 'Россия'),
        ('US', 'Америка')
    )
    author = models.ManyToManyField(User)
    title = models.CharField(max_length=255, verbose_name='Название')
    descriptions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='music')
    country = models.CharField(max_length=30, choices=COUNTRY)
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at2 = models.DateField(auto_now_add=True)
#
#     # f = models.OneToOneField
#     # f models.ManyToManyField
#
    def __str__(self):
        return f'{self.title} {self.created_at}'

    # class Meta:
#         verbose_name = 'Продукт'
#         verbose_name_plural = 'Продукты'


# Модели – это обьекты Python через которые Django управляет данными
# Модель – определяет структуру хранимых данных, включая типы полей и возможно их мак_разм, значения по умолчанию,
# параметры списка выбора, текст меток для форм и тд
# Джанго поддерживает субд – PostgreSQl, MariaDb, MySql, ORAACLE, Sqlite
# Sqlite – по умолчанию
# Числовые значения – integerfield, Positiveintegerfield, decimalField, FloatField
# Строковые – CharField, TextField
# Data – DateField, DateTimeField
# File and image – FileField, ImageField
# email – EmailField
# OneToOneField and ManyToManyField, ForeignKeyFiled
# Все модели являются наследниками базового класса Model
# Для создания моделей необходимо сделать миграции(то есть необходимо оповестить базу данных что мы сделали какие то
# изменения и необх их применить)
# makemigrations- создает миграции на основе изменений в моделях
# migrate – применят созданные миграции

# миграции сделать что бы увидеть результаты (т.е те миграции которые в инсталлед апп)


# class CheakDeleteField(models.Model):
#     # product = models.ForeignKey(Product, on_delete=models.CASCADE) # удалив этот продукт удалится и этот пост
#     # product = models.ForeignKey(Product, on_delete=models.RESTRICT) нужно удалить этот продукт что бы удалить этот пост
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True) # удалив продукт тут станет null
#     # product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, default=4) # (Product.objects.get(id=4)) # после удаления станет принадлежать продукту с id 4
#     name = models.TextField()


# primary_key - расказать что само по себе появляется
# почему pycharm - при создании генерирует виртуальное окружение

