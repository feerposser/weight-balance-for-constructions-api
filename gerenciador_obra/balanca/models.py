from django.db import models


class ModelBalanca(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Balança"
        verbose_name_plural = "Balanças"
