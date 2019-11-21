from django.contrib import admin
from .models import *

class SubscriberAdmin(admin.ModelAdmin):
    # list_display = ['name', 'email'] какие поля отображать
    list_display = [field.name for field in Subscriber._meta.fields]
    exclude = ['email'] #отобразить все поля кроме email на странице редактирования записи
    # fields = ['email']  обратное exclude
    list_filter = ['name']  # поле позволяющие фильтровать по имени все записи
    search_fields = ['name', 'email']   # позволяет искать п мылу или имени какуюто запись


    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)