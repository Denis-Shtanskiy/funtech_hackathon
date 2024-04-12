# Generated by Django 5.0.4 on 2024-04-11 22:31

import django.db.models.deletion
import tickets.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name="Registration",
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_code', models.CharField(auto_created=True, default=tickets.utils.get_uuid_str, help_text='Уникальный код для кодирования данных о билете в QR-код.', max_length=36, unique=True, verbose_name='Уникальный код')),
                ('status', models.CharField(choices=[('PENDING', 'Ожидание подтверждения'), ('REJECTED', 'Заявка отклонена'), ('CONFIRMED', 'Вы участвуете')], default='PENDING', max_length=25, verbose_name='Статус регистрации')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event', verbose_name='Событие')),
            ],
            options={
                "verbose_name": "Регистрация",
                "verbose_name_plural": "регистрации",
                "default_related_name": "ticket_registrations",
            },
        ),
    ]
