# Generated by Django 4.1.4 on 2022-12-28 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInputs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initialState', models.CharField(max_length=20)),
                ('lastState', models.CharField(max_length=20)),
            ],
        ),
    ]
