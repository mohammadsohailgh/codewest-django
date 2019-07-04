# Generated by Django 2.2.2 on 2019-07-04 17:19

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
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_0_0', models.CharField(default='Not answered', max_length=25)),
                ('question_0_1', models.CharField(default='Not answered', max_length=25)),
                ('question_0_2', models.CharField(default='Not answered', max_length=25)),
                ('question_0_3', models.CharField(default='Not answered', max_length=25)),
                ('question_0_4', models.CharField(default='Not answered', max_length=25)),
                ('question_0_5', models.CharField(default='Not answered', max_length=25)),
                ('question_0_6', models.CharField(default='Not answered', max_length=25)),
                ('question_0_7', models.CharField(default='Not answered', max_length=25)),
                ('question_0_8', models.CharField(default='Not answered', max_length=25)),
                ('question_0_9', models.CharField(default='Not answered', max_length=25)),
                ('question_0_10', models.CharField(default='Not answered', max_length=25)),
                ('question_0_11', models.CharField(default='Not answered', max_length=25)),
                ('question_0_12', models.CharField(default='Not answered', max_length=25)),
                ('question_0_13', models.CharField(default='Not answered', max_length=25)),
                ('question_1_0', models.CharField(default='Not answered', max_length=25)),
                ('question_1_1', models.CharField(default='Not answered', max_length=25)),
                ('question_1_2', models.CharField(default='Not answered', max_length=25)),
                ('question_1_3', models.CharField(default='Not answered', max_length=25)),
                ('question_1_4', models.CharField(default='Not answered', max_length=25)),
                ('question_1_5', models.CharField(default='Not answered', max_length=25)),
                ('question_1_6', models.CharField(default='Not answered', max_length=25)),
                ('question_1_7', models.CharField(default='Not answered', max_length=25)),
                ('question_1_8', models.CharField(default='Not answered', max_length=25)),
                ('question_2_0', models.CharField(default='Not answered', max_length=25)),
                ('question_2_1', models.CharField(default='Not answered', max_length=25)),
                ('question_2_2', models.CharField(default='Not answered', max_length=25)),
                ('question_2_3', models.CharField(default='Not answered', max_length=25)),
                ('question_2_4', models.CharField(default='Not answered', max_length=25)),
                ('question_2_5', models.CharField(default='Not answered', max_length=25)),
                ('question_2_6', models.CharField(default='Not answered', max_length=25)),
                ('question_3_0', models.CharField(default='Not answered', max_length=25)),
                ('question_3_1', models.CharField(default='Not answered', max_length=25)),
                ('question_3_2', models.CharField(default='Not answered', max_length=25)),
                ('question_3_3', models.CharField(default='Not answered', max_length=25)),
                ('question_3_4', models.CharField(default='Not answered', max_length=25)),
                ('question_3_5', models.CharField(default='Not answered', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.Survey')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('text', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_questions', to='languages.Question')),
            ],
        ),
        migrations.CreateModel(
            name='SavedAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.Answer')),
                ('sub_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.SubQuestion')),
                ('survey_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_answers', to='languages.SurveyData')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='languages.Survey'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='languages.Question'),
        ),
    ]
