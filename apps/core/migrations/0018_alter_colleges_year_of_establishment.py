# Generated by Django 4.1.7 on 2023-03-31 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_colleges_college_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colleges',
            name='year_of_establishment',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
