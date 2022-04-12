# Generated by Django 4.0.3 on 2022-04-11 16:58

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
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Urgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urgency_type', models.CharField(max_length=255, unique=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sources', models.IntegerField()),
                ('details', models.TextField(blank=True, null=True)),
                ('paper_format', models.CharField(max_length=255)),
                ('education_level', models.CharField(choices=[('High School', 'High-School'), ('Bachelors', 'Bachelor'), ('Masters', 'Master'), ('PHD', 'Doctorate')], max_length=200)),
                ('pages', models.IntegerField()),
                ('spacing', models.CharField(choices=[('Single spacing', 'Single-Spacing'), ('Double spacing', 'Double-Spacing')], max_length=200)),
                ('order_status', models.CharField(choices=[('Pending', 'pending'), ('In progress', 'In-progress'), ('Completed', 'completed')], max_length=200)),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.subject')),
                ('urgency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.urgency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MediaFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_attachments', to='orders.order')),
            ],
        ),
    ]
