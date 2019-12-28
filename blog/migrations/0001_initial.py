# Generated by Django 2.1.7 on 2019-12-28 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Category')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('slug', models.SlugField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.Category')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.AddField(
            model_name='blogentry',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('slug', 'parent')},
        ),
    ]
