# Generated by Django 5.1.2 on 2024-11-03 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_tag'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='comment',
            new_name='comments_created_9b3f77_idx',
            old_name='blog_commen_created_0e6ed4_idx',
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comments',
        ),
    ]
