# Generated by Django 2.1.5 on 2019-01-10 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sena', '0006_centros_ubicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='centros',
            name='telefono',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]