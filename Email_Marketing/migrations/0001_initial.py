# Generated by Django 4.0.5 on 2022-06-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_id', models.IntegerField()),
                ('Product_id', models.CharField(max_length=10)),
                ('Date', models.IntegerField()),
                ('Gender', models.CharField(max_length=10)),
                ('Template', models.IntegerField()),
                ('Countries', models.CharField(max_length=10)),
                ('Purchase', models.CharField(max_length=10)),
                ('Marital', models.CharField(max_length=10)),
                ('Age', models.IntegerField()),
            ],
        ),
    ]