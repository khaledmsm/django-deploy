# Generated by Django 3.2.5 on 2022-07-05 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eid_Post', '0007_name_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
