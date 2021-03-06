# Generated by Django 2.2.6 on 2020-12-07 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0006_auto_20201207_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='book_publisher', to='p_library.Publisher'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publisher',
            name='pub_name',
            field=models.TextField(default=''),
        ),
    ]
