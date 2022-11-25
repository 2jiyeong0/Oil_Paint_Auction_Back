# Generated by Django 4.1.3 on 2022-11-25 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True, verbose_name='제목')),
                ('content', models.TextField(blank=True, max_length=200, null=True, verbose_name='내용')),
                ('before_image', models.ImageField(blank=True, upload_to='before_img', verbose_name='변환 전 사진')),
                ('after_image', models.ImageField(blank=True, upload_to='after_img', verbose_name='변환 후 사진')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 시간')),
                ('style', models.CharField(choices=[('1', 'composition'), ('2', 'la_muse'), ('3', 'starry_night'), ('4', 'the_wave'), ('5', 'candy'), ('6', 'feathers'), ('7', 'mosaic'), ('8', 'the_scream'), ('9', 'udnie')], max_length=20, verbose_name='스타일')),
                ('is_auction', models.BooleanField(default=False, verbose_name='경매상태')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='author_painting', to=settings.AUTH_USER_MODEL, verbose_name='원작자')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='owner_painting', to=settings.AUTH_USER_MODEL, verbose_name='소유자')),
            ],
            options={
                'db_table': 'db_painting',
            },
        ),
    ]
