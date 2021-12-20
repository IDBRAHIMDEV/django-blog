# Generated by Django 4.0 on 2021-12-20 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_tag_article_published_article_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='published',
            field=models.IntegerField(choices=[(0, 'Disable'), (0, 'Enable')], default=0, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]