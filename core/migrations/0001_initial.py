# Generated by Django 4.0.6 on 2022-07-30 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=18)),
                ('name', models.CharField(max_length=61)),
                ('email', models.EmailField(max_length=254)),
                ('game', models.CharField(max_length=45)),
                ('message', models.CharField(max_length=1300)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=18)),
                ('rating', models.IntegerField()),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='GamesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=50)),
                ('subGame', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('text', models.CharField(blank=True, max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='NewGames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('is_GradientCard', models.BooleanField(default=True)),
                ('link', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Trending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('is_GradientCard', models.BooleanField(default=True)),
                ('link', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
