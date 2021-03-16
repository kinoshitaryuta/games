# Generated by Django 3.1.6 on 2021-03-01 05:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000)),
                ('title', models.CharField(max_length=100)),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_type', models.CharField(choices=[('10', 'キャリア'), ('20', 'スポーツ'), ('30', 'e-スポーツ'), ('40', 'コミニケーション')], max_length=100)),
                ('work_detail', models.CharField(blank=True, choices=[('10', 'セミナー'), ('20', '朝活'), ('30', '意見交換会'), ('40', '名刺交換会'), ('50', '学生向け'), ('60', 'その他')], max_length=100)),
                ('sport_detail', models.CharField(blank=True, choices=[('10', '誰でもOK'), ('20', '経験者のみ'), ('30', '観戦'), ('40', 'その他')], max_length=100)),
                ('e_sport_detail', models.CharField(blank=True, choices=[('10', 'FORTNITE'), ('20', 'PUBG'), ('30', '荒野行動'), ('40', 'APEX'), ('50', 'スプラトゥーン'), ('60', '大乱闘スマッシュブラザーズ'), ('70', '鉄拳'), ('80', 'ストリートファイター'), ('90', 'リーグオブレジェンド'), ('100', 'ウイニングイレブン'), ('110', 'パズル＆ドラゴンズ'), ('120', 'ぷよぷよ'), ('130', 'その他')], max_length=100)),
                ('hobby_detail', models.CharField(blank=True, choices=[('10', '読書会'), ('20', '飲み会'), ('30', 'カフェ会'), ('40', 'もくもく会'), ('50', 'その他')], max_length=100)),
                ('holding_method', models.CharField(choices=[('10', 'オンライン'), ('20', 'オフライン')], max_length=100)),
                ('event_date', models.DateField(blank=True, null=True)),
                ('start_application_date', models.DateField(blank=True, null=True)),
                ('finish_application_date', models.DateField(blank=True, null=True)),
                ('master_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]