# Generated by Django 3.2.8 on 2021-11-27 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_alter_faq_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.TextField(blank=True, null=True),
        ),
    ]
