# Generated by Django 4.2.6 on 2023-11-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telebe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adı', models.TextField()),
                ('Yasi', models.IntegerField()),
                ('Qrup_No', models.TextField()),
                ('Sekli', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('Teqaud', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Women',
        ),
    ]
