# Generated by Django 4.2.1 on 2023-05-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinariaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenmascotas',
            name='estado',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordenmascotas',
            name='fechaHistoria',
            field=models.CharField(default=28, max_length=200),
            preserve_default=False,
        ),
    ]
