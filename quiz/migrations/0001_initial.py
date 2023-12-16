# Generated by Django 4.0.1 on 2022-05-18 04:12

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('quiz_code', models.CharField(max_length=50, unique=True)),
                ('topic', models.CharField(max_length=50)),
                ('number_of_chosen_questions', models.IntegerField()),
                ('number_of_theory_questions', models.IntegerField()),
                ('time', models.IntegerField(help_text='duration of the quiz in minutes.')),
                ('required_score_to_pass', models.IntegerField(help_text='required score in %.')),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], default=('easy', 'easy'), max_length=6)),
                ('start_quiz', models.DateTimeField(blank=True, null=True)),
                ('is_answered', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.instructoraccount')),
            ],
        ),
        migrations.CreateModel(
            name='TotalDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_to_pass', models.CharField(max_length=50)),
                ('total', models.FloatField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.studentaccount')),
            ],
        ),
        migrations.CreateModel(
            name='ReportResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('student_answer', models.CharField(max_length=255)),
                ('correct_answer', models.TextField()),
                ('is_true_answered', models.CharField(default='Correct answer', max_length=50)),
                ('question_score', models.FloatField()),
                ('on_date', models.DateTimeField(default=datetime.datetime(2022, 5, 18, 6, 12, 9, 466013))),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.studentaccount')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('is_theory_question', models.BooleanField(default=False)),
                ('question_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('chose1', models.CharField(blank=True, max_length=200, null=True)),
                ('chose2', models.CharField(blank=True, max_length=200, null=True)),
                ('chose3', models.CharField(blank=True, max_length=200, null=True)),
                ('chose4', models.CharField(blank=True, max_length=200, null=True)),
                ('correct_chosen', models.CharField(blank=True, max_length=200, null=True)),
                ('theory_answer', models.TextField(blank=True, max_length=500, null=True)),
                ('answerd_on', models.DateTimeField(default=datetime.datetime(2022, 5, 18, 6, 12, 9, 465556))),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='IntervalQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intervalTime', models.TimeField()),
                ('quiz', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
            ],
        ),
    ]
