# Generated by Django 4.2 on 2023-06-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_customerregistration_no_of_sites'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to='media/slideshow')),
            ],
            options={
                'verbose_name': 'SlideShow',
                'verbose_name_plural': 'SlideShow',
            },
        ),
        migrations.RenameField(
            model_name='customerregistration',
            old_name='description',
            new_name='ID_Number',
        ),
    ]
