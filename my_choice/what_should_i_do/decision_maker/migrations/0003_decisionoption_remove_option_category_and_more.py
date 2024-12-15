# Generated by Django 5.1.2 on 2024-12-13 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decision_maker', '0002_category_option_delete_decisionoption'),
    ]

    operations = [
        migrations.CreateModel(
            name='DecisionOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('option', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='option',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
    ]
