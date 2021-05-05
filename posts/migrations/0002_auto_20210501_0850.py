# Generated by Django 3.1.6 on 2021-04-30 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventscheduleapex',
            name='title',
        ),
        migrations.RemoveField(
            model_name='eventschedulefortnite',
            name='title',
        ),
        migrations.RemoveField(
            model_name='eventscheduleguraburu',
            name='title',
        ),
        migrations.RemoveField(
            model_name='eventschedulemonhan',
            name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='address',
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_us', models.CharField(choices=[('10', '不審な内容またはスパムである'), ('20', '不適切な画像または性的内容を含む画像動画を表示している'), ('30', '不適切または攻撃的な内容を含んでいる'), ('40', '自傷行為や自殺の意思をほのめかしている'), ('50', 'その他')], max_length=20)),
                ('message', models.TextField(blank=True, max_length=1000)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]