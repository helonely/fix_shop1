# Generated by Django 5.0.6 on 2024-07-09 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='manufactured_at',
            field=models.DateTimeField(auto_now=True, help_text='Дата производства продукта', verbose_name='Дата производства'),
        ),
    ]