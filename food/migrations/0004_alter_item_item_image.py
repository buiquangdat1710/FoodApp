# Generated by Django 4.2.16 on 2024-10-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_item_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://cdn-icons-png.flaticon.com/512/4901/4901689.png', max_length=500),
        ),
    ]
