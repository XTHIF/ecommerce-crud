# Generated by Django 4.1.7 on 2023-03-30 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_rename_m_product_product_m_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='m_description',
            field=models.CharField(max_length=200),
        ),
    ]
