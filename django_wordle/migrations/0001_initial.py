# Generated by Django 5.1.4 on 2024-12-17 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempts_count', models.IntegerField(default=6)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess', models.CharField(max_length=5)),
                ('feedback', models.CharField(default='rrrrr', max_length=5)),
                ('won', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_wordle.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_wordle.word'),
        ),
    ]
