# Generated by Django 4.2.11 on 2024-04-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=250)),
                ('user_id', models.IntegerField()),
                ('to_perosn', models.CharField(max_length=250)),
                ('project', models.CharField(max_length=250)),
                ('printer', models.CharField(max_length=250)),
                ('time', models.FloatField()),
                ('material', models.CharField(max_length=250)),
                ('quantity', models.FloatField()),
                ('price_or_order', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('total_price', models.FloatField()),
                ('finance', models.IntegerField()),
                ('supervisor', models.BooleanField(default=False)),
                ('membership', models.BooleanField(default=False)),
                ('gain', models.IntegerField()),
                ('risk', models.IntegerField()),
            ],
        ),
    ]
