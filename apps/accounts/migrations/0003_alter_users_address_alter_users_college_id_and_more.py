# Generated by Django 4.1.7 on 2023-03-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_users_options_alter_users_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='college_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(choices=[('student', 'STUDENT'), ('teacher', 'TEACHER')], default='STUDENT', max_length=20),
        ),
        migrations.AlterField(
            model_name='users',
            name='standard',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='student_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]
