# Generated by Django 4.2.5 on 2023-10-08 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reg', '0004_alter_user_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/profile_pictures'),
        ),
    ]