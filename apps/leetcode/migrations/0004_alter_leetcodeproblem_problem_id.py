# Generated by Django 4.1.7 on 2023-04-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leetcode', '0003_alter_leetcodeproblem_beats_time_complexity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leetcodeproblem',
            name='problem_id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
