# Generated by Django 4.1.6 on 2023-04-06 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LaSegunda', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ObjetoImagen',
        ),
        migrations.AddField(
            model_name='amigo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='la_segunda_objetos'),
        ),
    ]