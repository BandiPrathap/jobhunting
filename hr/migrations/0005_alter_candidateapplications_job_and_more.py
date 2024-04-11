# Generated by Django 5.0.2 on 2024-04-01 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_alter_selectcandidatejob_candidate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateapplications',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.jobpost'),
        ),
        migrations.AlterField(
            model_name='candidateapplications',
            name='status',
            field=models.CharField(choices=[('pandding', 'pandding'), ('selected', 'selected')], default='pending', max_length=20),
        ),
    ]