from django.db import models

from balanca.models import ModelBalanca


class ModelHistorico(models.Model):
    balanca = models.ForeignKey(ModelBalanca, on_delete=models.CASCADE)
    weight = models.FloatField()
    horario = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.balanca.name + ": " + self.horario.strftime("%d/%m/%Y - %H:%M")

    def get_date(self):
        return self.horario.strftime("%d/%m/%Y")

    def get_hour(self):
        return self.horario.strftime("%H:%M")

    def get_datetime(self):
        return self.get_date() + " - " + self.get_hour()

    class Meta:
        verbose_name = "Histórico"
        verbose_name_plural = "Históricos"
