# Generated by Django 4.1.6 on 2023-04-06 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LaSegunda', '0002_delete_objetoimagen_amigo_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='la_segunda_avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
