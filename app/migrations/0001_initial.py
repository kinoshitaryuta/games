# Generated by Django 3.1.6 on 2021-03-01 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_us', models.CharField(choices=[('10', 'アプリの不具合'), ('20', 'スパムと迷惑行為について'), ('30', '要注意コンテンツ'), ('40', 'サービスの改善について'), ('50', 'その他')], max_length=20)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('message', models.TextField(blank=True, max_length=1000)),
            ],
        ),
    ]
