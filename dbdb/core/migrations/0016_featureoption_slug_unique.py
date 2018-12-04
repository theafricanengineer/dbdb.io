# Generated by Django 2.0.9 on 2018-12-04 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_featureoption_slug_populate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featureoption',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterUniqueTogether(
            name='featureoption',
            unique_together={('feature', 'slug')},
        ),
    ]
