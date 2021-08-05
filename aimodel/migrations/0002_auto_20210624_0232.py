# Generated by Django 3.2.4 on 2021-06-23 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aimodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linearmodel',
            name='Age',
            field=models.FloatField(default=18, verbose_name='Yaş'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='BallSkills',
            field=models.FloatField(default=70, verbose_name='Topla Oynama Becerisi'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='Defence',
            field=models.FloatField(default=70, verbose_name='Defansif Yeteneği'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='GKSkills',
            field=models.FloatField(default=70, verbose_name='Kalecilik Yetenekleri'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='Height',
            field=models.FloatField(default=175, verbose_name='Boy'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='Mental',
            field=models.FloatField(default=70, verbose_name='Mental Kabiliyeti'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='Passing',
            field=models.FloatField(default=70, verbose_name='Pas Yeteneği'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='Physical',
            field=models.FloatField(default=70, verbose_name='Fiziki Yetenekleri'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='Position',
            field=models.CharField(choices=[('CAM', 'CAM'), ('CB', 'CB'), ('CDM', 'CDM'), ('CF', 'CF'), ('CF', 'CM'), ('GK', 'GK'), ('LB', 'LB'), ('LM', 'LM'), ('LW', 'LW'), ('LWB', 'LWB'), ('RB', 'RB'), ('RM', 'RM'), ('RW', 'RW'), ('RWB', 'RWB'), ('ST', 'ST')], default='CAM', max_length=50, verbose_name='Pozisyon'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='PreferredFoot_R',
            field=models.CharField(choices=[('Right', 'Sağ'), ('Left', 'Sol')], default='Sağ', max_length=50, verbose_name='Tercih Ettiği Ayak'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='Shooting',
            field=models.FloatField(default=70, verbose_name='Şut Yetenekleri'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='SkillMoves',
            field=models.FloatField(default=3, verbose_name='Beceri Hareketleri'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='Value',
            field=models.FloatField(default=15000000, verbose_name='Piyas Değeri'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='Wage',
            field=models.FloatField(default=50000, verbose_name='Haftalık Maaşı(€)'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='WeakFoot',
            field=models.FloatField(default=3, verbose_name='Zayıf Ayak Yeteneği'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='Weight',
            field=models.FloatField(default=70, verbose_name='Kilo'),
        ),
        migrations.AddField(
            model_name='linearmodel',
            name='WorkRate',
            field=models.CharField(choices=[('High/High', 'High/High'), ('High/Low', 'High/Low'), ('High/Medium', 'High/Medium'), ('Low/High', 'Low/High'), ('Low/Low', 'Low/Low'), ('Low_Medium', 'Low_Medium'), ('Medium/High', 'Medium/High'), ('Medium/Low', 'Medium/Low'), ('Medium/Medium', 'Medium/Medium')], default='Medium/Medium', max_length=50, verbose_name='Çalışma Oranları'),
        ),
        migrations.AlterField(
            model_name='linearmodel',
            name='Overal',
            field=models.FloatField(default=70, verbose_name='Ortalama'),
        ),
    ]
