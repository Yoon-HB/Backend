# Generated by Django 4.2.4 on 2023-11-07 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_alter_member_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(max_length=128, verbose_name='이름'),
        ),
    ]
