# Generated by Django 4.2.6 on 2023-11-30 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0001_initial'),
        ('core_user', '0002_alter_user_created_alter_user_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='posts_liked',
            field=models.ManyToManyField(related_name='liked_by', to='core_post.post'),
        ),
    ]
