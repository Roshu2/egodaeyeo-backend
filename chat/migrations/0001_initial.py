# Generated by Django 4.0.6 on 2022-08-11 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contract', '0004_alter_contract_status'),
        ('item', '0008_alter_item_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contract.contract')),
                ('inquirer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inquirer', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.item')),
            ],
            options={
                'db_table': 'chatrooms',
            },
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000, null=True, verbose_name='내용')),
                ('is_read', models.BooleanField(default=False, verbose_name='읽음/안읽음')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('application', models.BooleanField(default=False, verbose_name='신청')),
                ('contract_type', models.CharField(choices=[('신청', '신청'), ('거절', '거절'), ('수락', '수락'), ('종료', '종료')], max_length=6, null=True, verbose_name='신청 유형')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chatroom')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'chat_messages',
                'ordering': ['id'],
            },
        ),
    ]
