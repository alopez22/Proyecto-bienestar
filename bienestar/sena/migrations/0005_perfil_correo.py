# Generated by Django 2.1.5 on 2019-01-10 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sena', '0004_tips_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='correo',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
