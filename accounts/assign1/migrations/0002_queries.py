# Generated by Django 2.1.1 on 2018-09-19 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000)),
                ('content', models.CharField(max_length=10000)),
                ('text', models.CharField(max_length=10000)),
                ('code', models.CharField(max_length=1000)),
                ('user_id', models.IntegerField()),
                ('time', models.IntegerField()),
                ('vote', models.IntegerField()),
                ('reputation', models.IntegerField()),
                ('tag', models.CharField(max_length=1000)),
            ],
        ),
    ]
