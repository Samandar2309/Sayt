# Generated by Django 5.0.4 on 2024-04-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_title_tags_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=212)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=212)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]