# Generated by Django 5.2 on 2025-04-16 09:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kindergarten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('kindergarten_type', models.CharField(choices=[('state', 'Государственный'), ('private', 'Частный')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('age_range', models.CharField(max_length=100)),
                ('activities', models.TextField(blank=True)),
                ('working_hours', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('instagram', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('address', models.TextField()),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('rating', models.FloatField(default=0)),
                ('main_image', models.ImageField(upload_to='kindergartens/')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.district')),
            ],
        ),
        migrations.CreateModel(
            name='KindergartenImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='kindergartens/gallery/')),
                ('kindergarten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='kindergarten.kindergarten')),
            ],
        ),
        migrations.CreateModel(
            name='KindergartenReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('kindergarten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='kindergarten.kindergarten')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kindergarten_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KindergartenVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='kindergartens/videos/')),
                ('youtube_link', models.URLField(blank=True)),
                ('kindergarten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='kindergarten.kindergarten')),
            ],
        ),
    ]
