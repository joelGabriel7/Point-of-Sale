# Generated by Django 4.1.5 on 2023-04-10 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.UUIDField(blank=True, editable=False, null=True),
        ),
    ]
