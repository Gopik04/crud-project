# Generated by Django 5.1.3 on 2024-12-12 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rollno', models.IntegerField()),
                ('marks', models.FloatField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
