# Generated by Django 3.2 on 2023-04-17 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='stream',
        ),
        migrations.AddField(
            model_name='show',
            name='shows',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='shows', to='stream.stream'),
            preserve_default=False,
        ),
    ]
