# Generated by Django 2.1.1 on 2018-09-20 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assign1', '0003_solutions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solutions',
            name='q_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assign1.Queries'),
        ),
    ]