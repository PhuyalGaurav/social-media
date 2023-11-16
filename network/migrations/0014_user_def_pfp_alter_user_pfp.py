# Generated by Django 4.2.7 on 2023-11-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_user_bio_alter_user_pfp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='def_pfp',
            field=models.ImageField(default='pfp/defaults/2.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='pfp',
            field=models.ImageField(upload_to='pfp/user'),
        ),
    ]
