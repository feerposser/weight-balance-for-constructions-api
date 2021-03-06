# Generated by Django 3.1.7 on 2021-02-24 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('balanca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelHistorico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('horario', models.DateTimeField()),
                ('balanca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='balanca.modelbalanca')),
            ],
            options={
                'verbose_name': 'Histórico',
                'verbose_name_plural': 'Históricos',
            },
        ),
    ]
