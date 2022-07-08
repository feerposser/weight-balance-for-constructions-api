from django.contrib import admin

from .models import ModelHistorico


class ModelAdminHistorico(admin.ModelAdmin):
    readonly_fields = ('get_datetime',)
    fields = ('balanca', 'weight', 'get_datetime')


admin.site.register(ModelHistorico, ModelAdminHistorico)
