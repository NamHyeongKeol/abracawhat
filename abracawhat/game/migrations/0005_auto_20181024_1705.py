# Generated by Django 2.1.2 on 2018-10-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20181024_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='num',
            field=models.IntegerField(db_index=True, default=1),
        ),
    ]
