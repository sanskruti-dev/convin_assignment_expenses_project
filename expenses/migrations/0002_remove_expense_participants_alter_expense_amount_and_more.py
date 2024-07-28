# Generated by Django 5.0.7 on 2024-07-28 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='participants',
        ),
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='expense',
            name='split_method',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='expenseparticipant',
            name='amount_owed',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expenseparticipant',
            name='expense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='expenses.expense'),
        ),
        migrations.AlterField(
            model_name='expenseparticipant',
            name='percentage_owed',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
