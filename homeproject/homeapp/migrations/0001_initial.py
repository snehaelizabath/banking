# Generated by Django 4.1.7 on 2023-04-20 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('p_DOB', models.DateField()),
                ('p_age', models.CharField(max_length=3)),
                ('p_phonenumber', models.CharField(max_length=10)),
                ('p_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
