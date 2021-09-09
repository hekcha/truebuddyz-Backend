# Generated by Django 3.1.2 on 2021-09-09 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=61)),
                ('email', models.EmailField(max_length=254)),
                ('game', models.CharField(max_length=45)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('rating', models.IntegerField()),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='NewGames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('link', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Trending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('link', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
