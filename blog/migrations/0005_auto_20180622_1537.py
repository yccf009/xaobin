# Generated by Django 2.0.6 on 2018-06-22 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180622_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_username', models.CharField(max_length=20)),
                ('blog_link', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
