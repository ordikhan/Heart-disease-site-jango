# Generated by Django 3.0.1 on 2019-12-28 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='article_image')),
            ],
        ),
        migrations.DeleteModel(
            name='Base',
        ),
    ]
