# Generated by Django 3.1.6 on 2021-03-02 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Twitter_profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
    ]