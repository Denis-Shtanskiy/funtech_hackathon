# Generated by Django 5.0.4 on 2024-04-11 22:31

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
import users.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Название тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('yandex_id', models.PositiveBigIntegerField(unique=True, verbose_name='Связанный Яндекс ID')),
                ('first_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Фамилия')),
                ('username', models.CharField(blank=True, max_length=150, null=True, verbose_name='Логин из яндекс')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Адрес электронной почты')),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True, validators=[users.validators.validate_mobile], verbose_name='Номер телефона')),
                ('telegram_username', models.CharField(blank=True, max_length=150, null=True, validators=[users.validators.validate_telegram], verbose_name='Ник в телеграм')),
                ('position', models.CharField(blank=True, max_length=150, null=True, verbose_name='Должность')),
                ('work_place', models.CharField(blank=True, max_length=150, null=True, verbose_name='Место работы (компания)')),
                ('avatar', models.ImageField(blank=True, default='https://avatars.yandex.net/get-yapic/<default_avatar_id>/', null=True, upload_to='users/images/', verbose_name='Ссылка на фото')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('cities', models.ManyToManyField(blank=True, related_name='users', to='users.city', verbose_name='Интересующие города')),
                ('tags', models.ManyToManyField(blank=True, related_name='users', to='users.tag', verbose_name='Интересы')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('id', 'username'),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='NotificationSwitch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_notification', models.BooleanField(default=False, verbose_name='Общий флаг активации уведомлений')),
                ('is_email', models.BooleanField(default=False, verbose_name='Уведомления по электронной почте')),
                ('is_telegram', models.BooleanField(default=False, verbose_name='Уведомления в телеграм')),
                ('is_phone', models.BooleanField(default=False, verbose_name='Уведомления по СМС')),
                ('is_push', models.BooleanField(default=False, verbose_name='Пуш уведомления')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_notifications', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
            },
        ),
    ]
