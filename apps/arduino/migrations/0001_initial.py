# Generated by Django 5.1.6 on 2025-05-01 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rfid', models.CharField(max_length=8, verbose_name='RFID')),
                ('available', models.BooleanField(default=True, verbose_name='Disponivel')),
            ],
            options={
                'verbose_name': 'Cartão',
                'verbose_name_plural': 'Cartões',
                'ordering': ['-created_at', 'available'],
            },
        ),
    ]
