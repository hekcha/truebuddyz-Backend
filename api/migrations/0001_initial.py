# Generated by Django 3.1.2 on 2021-08-28 17:10

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
            name='Entertainment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('que1', models.CharField(blank=True, max_length=200, null=True)),
                ('option1A', models.CharField(max_length=50)),
                ('option1B', models.CharField(max_length=50)),
                ('option1C', models.CharField(blank=True, max_length=50, null=True)),
                ('option1D', models.CharField(blank=True, max_length=50, null=True)),
                ('que2', models.CharField(blank=True, max_length=200, null=True)),
                ('option2A', models.CharField(max_length=50)),
                ('option2B', models.CharField(max_length=50)),
                ('option2C', models.CharField(blank=True, max_length=50, null=True)),
                ('option2D', models.CharField(blank=True, max_length=50, null=True)),
                ('que3', models.CharField(blank=True, max_length=200, null=True)),
                ('option3A', models.CharField(max_length=50)),
                ('option3B', models.CharField(max_length=50)),
                ('option3C', models.CharField(blank=True, max_length=50, null=True)),
                ('option3D', models.CharField(blank=True, max_length=50, null=True)),
                ('que4', models.CharField(blank=True, max_length=200, null=True)),
                ('option4A', models.CharField(max_length=50)),
                ('option4B', models.CharField(max_length=50)),
                ('option4C', models.CharField(blank=True, max_length=50, null=True)),
                ('option4D', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntertainmentResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=4)),
                ('image', models.CharField(max_length=500)),
                ('text', models.CharField(max_length=200)),
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
            name='QuizQuestionBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('part1', models.CharField(blank=True, max_length=200, null=True)),
                ('part2', models.CharField(blank=True, max_length=200, null=True)),
                ('optionA', models.CharField(max_length=50)),
                ('optionB', models.CharField(max_length=50)),
                ('optionC', models.CharField(blank=True, max_length=50, null=True)),
                ('optionD', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RfQuestionBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('que', models.CharField(blank=True, max_length=200, null=True)),
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
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=14, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('que1', models.CharField(max_length=200)),
                ('option1A', models.CharField(max_length=50)),
                ('option1B', models.CharField(max_length=50)),
                ('option1C', models.CharField(blank=True, max_length=50, null=True)),
                ('option1D', models.CharField(blank=True, max_length=50, null=True)),
                ('ans1', models.IntegerField()),
                ('que2', models.CharField(max_length=200)),
                ('option2A', models.CharField(max_length=50)),
                ('option2B', models.CharField(max_length=50)),
                ('option2C', models.CharField(blank=True, max_length=50, null=True)),
                ('option2D', models.CharField(blank=True, max_length=50, null=True)),
                ('ans2', models.IntegerField()),
                ('que3', models.CharField(max_length=200)),
                ('option3A', models.CharField(max_length=50)),
                ('option3B', models.CharField(max_length=50)),
                ('option3C', models.CharField(blank=True, max_length=50, null=True)),
                ('option3D', models.CharField(blank=True, max_length=50, null=True)),
                ('ans3', models.IntegerField()),
                ('que4', models.CharField(max_length=200)),
                ('option4A', models.CharField(max_length=50)),
                ('option4B', models.CharField(max_length=50)),
                ('option4C', models.CharField(blank=True, max_length=50, null=True)),
                ('option4D', models.CharField(blank=True, max_length=50, null=True)),
                ('ans4', models.IntegerField()),
                ('que5', models.CharField(max_length=200)),
                ('option5A', models.CharField(max_length=50)),
                ('option5B', models.CharField(max_length=50)),
                ('option5C', models.CharField(blank=True, max_length=50, null=True)),
                ('option5D', models.CharField(blank=True, max_length=50, null=True)),
                ('ans5', models.IntegerField()),
                ('que6', models.CharField(max_length=200)),
                ('option6A', models.CharField(max_length=50)),
                ('option6B', models.CharField(max_length=50)),
                ('option6C', models.CharField(blank=True, max_length=50, null=True)),
                ('option6D', models.CharField(blank=True, max_length=50, null=True)),
                ('ans6', models.IntegerField()),
                ('que7', models.CharField(max_length=200)),
                ('option7A', models.CharField(max_length=50)),
                ('option7B', models.CharField(max_length=50)),
                ('option7C', models.CharField(blank=True, max_length=50, null=True)),
                ('option7D', models.CharField(blank=True, max_length=50, null=True)),
                ('ans7', models.IntegerField()),
                ('que8', models.CharField(max_length=200)),
                ('option8A', models.CharField(max_length=50)),
                ('option8B', models.CharField(max_length=50)),
                ('option8C', models.CharField(blank=True, max_length=50, null=True)),
                ('option8D', models.CharField(blank=True, max_length=50, null=True)),
                ('ans8', models.IntegerField()),
                ('que9', models.CharField(max_length=200)),
                ('option9A', models.CharField(max_length=50)),
                ('option9B', models.CharField(max_length=50)),
                ('option9C', models.CharField(blank=True, max_length=50, null=True)),
                ('option9D', models.CharField(blank=True, max_length=50, null=True)),
                ('ans9', models.IntegerField()),
                ('que10', models.CharField(max_length=200)),
                ('option10A', models.CharField(max_length=50)),
                ('option10B', models.CharField(max_length=50)),
                ('option10C', models.CharField(blank=True, max_length=50, null=True)),
                ('option10D', models.CharField(blank=True, max_length=50, null=True)),
                ('ans10', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuizResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizcode', models.CharField(max_length=14)),
                ('respcode', models.CharField(max_length=14)),
                ('name', models.CharField(max_length=25)),
                ('marks', models.IntegerField()),
                ('ans1', models.IntegerField()),
                ('ans2', models.IntegerField()),
                ('ans3', models.IntegerField()),
                ('ans4', models.IntegerField()),
                ('ans5', models.IntegerField()),
                ('ans6', models.IntegerField()),
                ('ans7', models.IntegerField()),
                ('ans8', models.IntegerField()),
                ('ans9', models.IntegerField()),
                ('ans10', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('quizcode', 'respcode')},
                'index_together': {('quizcode', 'respcode')},
            },
        ),
    ]
