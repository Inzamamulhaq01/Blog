# Generated by Django 5.0.6 on 2024-07-28 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0003_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]