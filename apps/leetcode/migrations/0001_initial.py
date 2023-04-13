# Generated by Django 4.1.7 on 2023-04-04 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeetCodeProblem',
            fields=[
                ('problem_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=100, null=True)),
                ('leetcode_question_link', models.URLField(max_length=255)),
                ('difficulty', models.CharField(choices=[('Easy', 'EASY'), ('Not Set', ''), ('Medium', 'MEDIUM'), ('Hard', 'HARD')], max_length=100)),
                ('started_at', models.DateTimeField()),
                ('finished_at', models.DateTimeField()),
                ('solved', models.BooleanField(default=False)),
                ('beats_time_complexity', models.FloatField()),
            ],
        ),
    ]
