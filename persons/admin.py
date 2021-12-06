from django.contrib.admin import ModelAdmin, register

from persons.models import Person


@register(Person)
class PersonAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name','age')
    icon_name = 'fingerprint'