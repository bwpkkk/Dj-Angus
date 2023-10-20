# Generated by Django 4.2.5 on 2023-10-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reg', '0005_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='DateofBirth',
            field=models.DateField(blank=True, null=True, verbose_name='DOB'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures', verbose_name='Profile Picture'),
        ),
    ]