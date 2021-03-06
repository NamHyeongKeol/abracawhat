# Generated by Django 2.1.2 on 2018-10-09 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='move',
            name='player_round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moves', to='game.PlayerRound'),
        ),
        migrations.AddField(
            model_name='move',
            name='turn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moves', to='game.Turn'),
        ),
        migrations.AddField(
            model_name='game',
            name='users',
            field=models.ManyToManyField(related_name='games', through='game.Player', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.Player'),
        ),
        migrations.AddField(
            model_name='card',
            name='move',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='game.Move'),
        ),
        migrations.AddField(
            model_name='card',
            name='player_round',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='game.PlayerRound'),
        ),
        migrations.AddField(
            model_name='card',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='game.Round'),
        ),
    ]
