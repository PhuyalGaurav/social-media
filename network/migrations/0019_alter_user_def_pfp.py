# Generated by Django 4.2.7 on 2023-11-16 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0018_alter_user_def_pfp_alter_user_pfp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='def_pfp',
            field=models.ImageField(default='pfp/defaults/4.png', upload_to=''),
        ),
    ]
