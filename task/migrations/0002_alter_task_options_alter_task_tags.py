# Generated by Django 4.2.3 on 2023-07-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['is_done', '-creation_date']},
        ),
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(related_name='tasks', to='task.tag'),
        ),
    ]
