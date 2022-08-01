# Generated by Django 4.0.6 on 2022-08-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_remove_chatmessage_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='contract_type',
            field=models.CharField(choices=[('신청', '신청'), ('거절', '거절'), ('수락', '수락'), ('종료', '종료')], max_length=6, null=True, verbose_name='신청 유형'),
        ),
    ]
