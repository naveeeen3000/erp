# Generated by Django 4.1.7 on 2023-03-30 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_users_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(db_index=True, max_length=254),
        ),
        migrations.AddConstraint(
            model_name='users',
            constraint=models.UniqueConstraint(fields=('email', 'student_id', 'phone'), name='unique_student_constraint'),
        ),
    ]