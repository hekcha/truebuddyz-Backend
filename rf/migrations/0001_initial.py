# Generated by Django 3.1.2 on 2021-09-07 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RfQuestionBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('que', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
