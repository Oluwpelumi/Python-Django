# Generated by Django 4.0.3 on 2022-04-09 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('tag', models.TextField()),
                ('offer1', models.BooleanField(default=False)),
                ('offer2', models.BooleanField(default=False)),
                ('offer3', models.BooleanField(default=False)),
            ],
        ),
    ]