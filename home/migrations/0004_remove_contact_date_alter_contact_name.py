# Generated by Django 4.1.3 on 2023-01-12 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contact_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=45),
        ),
    ]
