from django.contrib import admin

# Register your models here. - регистрируем наши модельки
from applications.music.models import *


class MusicAdmin(admin.ModelAdmin):
    # exclude = ('uuid', 'last_bid_price', 'amount', 'bid_duration')
    list_display = ('title',)
    # list_filter = ['categories', 'status', 'start_date']
    # search_fields = ['uuid', 'title', 'desc']


admin.site.register(Category)
admin.site.register(Music, MusicAdmin)


