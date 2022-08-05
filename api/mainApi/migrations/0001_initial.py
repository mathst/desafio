# Generated by Django 4.1 on 2022-08-03 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veiculo', models.CharField(max_length=180)),
                ('marca', models.CharField(max_length=180)),
                ('cor', models.CharField(max_length=180)),
                ('ano', models.IntegerField()),
                ('descricao', models.CharField(max_length=360)),
                ('vendido', models.BooleanField(blank=True, default=False)),
                ('created', models.DateTimeField(blank=True)),
                ('update', models.DateTimeField(blank=True)),
            ],
        ),
    ]
