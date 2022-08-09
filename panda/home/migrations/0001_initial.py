# Generated by Django 4.0.3 on 2022-08-09 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('slug', models.SlugField(max_length=70, unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('content', models.TextField(max_length=150)),
                ('price', models.FloatField(default=0)),
                ('photo', models.ImageField(upload_to='photo/%Y/%m%d')),
                ('slug', models.SlugField(max_length=70, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='home.category')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
