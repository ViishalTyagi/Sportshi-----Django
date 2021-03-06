# Generated by Django 2.1.5 on 2019-01-23 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('location', models.CharField(max_length=120)),
                ('Score', models.CharField(max_length=150)),
                ('first_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Team_1', to='teams.Team')),
                ('second_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Team_2', to='teams.Team')),
            ],
        ),
    ]
