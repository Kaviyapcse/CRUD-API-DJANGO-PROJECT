# Generated by Django 4.2.2 on 2023-08-03 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('color', models.CharField(default='5800FF', max_length=6)),
                ('description', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
