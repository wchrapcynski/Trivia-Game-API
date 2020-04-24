# Generated by Django 3.0.3 on 2020-04-24 23:39

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answers', django_mysql.models.ListTextField(models.CharField(max_length=300), max_length=66, size=4)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]