# Generated by Django 4.0 on 2021-12-27 09:44

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_blogpost_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='comments',
            field=jsonfield.fields.JSONField(default={'all': []}),
        ),
    ]
