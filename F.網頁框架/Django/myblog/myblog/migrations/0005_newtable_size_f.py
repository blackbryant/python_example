# Generated by Django 4.2.4 on 2023-08-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_alter_newtable_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='newtable',
            name='size_f',
            field=models.CharField(choices=[('S', 'Small'), ('L', 'Large'), ('M', 'Medium')], default='S', max_length=1),
        ),
    ]
