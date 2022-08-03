
# Generated by Django 4.0.6 on 2022-08-01 14:57


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_alter_item_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(blank=True, choices=[('대여 가능', '대여 가능'), ('대여 중', '대여 중'), ('대여 종료', '대여 종료')], max_length=10, verbose_name='상태'),
        ),
    ]