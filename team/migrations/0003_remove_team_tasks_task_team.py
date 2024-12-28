# Generated by Django 5.1.4 on 2024-12-28 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_team_admins_team_archived_team_deadline_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='team',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='team.team'),
            preserve_default=False,
        ),
    ]