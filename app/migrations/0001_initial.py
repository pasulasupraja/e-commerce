# Generated by Django 4.2.11 on 2024-04-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('name', models.CharField(max_length=25)),
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
