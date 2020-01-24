# Generated by Django 2.1.7 on 2020-01-09 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_website', '0003_pagesection_heading_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageSectionText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='pagesection',
            name='text',
        ),
        migrations.AddField(
            model_name='pagesection',
            name='text',
            field=models.ManyToManyField(to='static_website.PageSectionText'),
        ),
    ]