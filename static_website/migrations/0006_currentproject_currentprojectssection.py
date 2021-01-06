# Generated by Django 2.1.7 on 2021-01-06 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_website', '0005_pagesectiontext_col_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('tech_stack', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CurrentProjectsSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('heading_icon', models.TextField()),
                ('projects', models.ManyToManyField(to='static_website.CurrentProject')),
            ],
        ),
    ]