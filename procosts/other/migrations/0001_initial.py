# Generated by Django 4.2.11 on 2024-03-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gain', models.DecimalField(decimal_places=10, max_digits=10)),
                ('risk', models.DecimalField(decimal_places=10, max_digits=10)),
            ],
        ),
    ]
