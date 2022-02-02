# Generated by Django 4.0.1 on 2022-01-31 05:44

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='setting',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='setting',
            name='logo',
            field=models.ImageField(upload_to='logo'),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('meta_title', models.CharField(max_length=255)),
                ('meta_keyword', models.TextField()),
                ('meta_description', models.TextField()),
                ('image', models.ImageField(upload_to='blog')),
                ('page_visit', models.IntegerField(default=0)),
                ('description', ckeditor.fields.RichTextField()),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.category')),
            ],
        ),
    ]