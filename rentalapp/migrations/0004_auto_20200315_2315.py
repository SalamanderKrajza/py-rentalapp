# Generated by Django 3.0.4 on 2020-03-15 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rentalapp', '0003_auto_20200314_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(default='CUSTOM', max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='custom_action',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='order',
            name='action_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentalapp.Action'),
        ),
    ]