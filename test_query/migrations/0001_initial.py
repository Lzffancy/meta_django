# Generated by Django 3.2.12 on 2022-03-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message_board',
            fields=[
                ('uid', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('nick_name', models.CharField(max_length=16)),
                ('message', models.TextField(max_length=258)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]