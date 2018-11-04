# Generated by Django 2.1.3 on 2018-11-04 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='review.Book'),
            preserve_default=False,
        ),
    ]
