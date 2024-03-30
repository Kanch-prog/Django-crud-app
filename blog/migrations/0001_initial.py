# Generated by Django 5.0.3 on 2024-03-23 02:09

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-published_at'],
            },
        ),
    ]