# Generated by Django 4.0.1 on 2022-05-18 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuperUserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('is_superuser', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdminAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=100)),
                ('admin_type', models.CharField(choices=[('main', 'Main'), ('inherit', 'Inherit')], default='inherit', max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50, unique=True)),
                ('admins_number', models.IntegerField()),
                ('instrauctors_number', models.IntegerField()),
                ('students_number', models.IntegerField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('is_sign_up', models.BooleanField(default=True)),
                ('contact_email', models.EmailField(max_length=254, unique=True)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('admins_number', models.IntegerField()),
                ('instrauctors_number', models.IntegerField()),
                ('students_number', models.IntegerField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('is_sign_up', models.BooleanField(default=True)),
                ('contact_email', models.EmailField(max_length=254)),
                ('description', models.TextField(max_length=200)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_have_perm', models.CharField(max_length=50, unique=True)),
                ('company_name', models.CharField(max_length=50)),
                ('add_doctor', models.BooleanField(default=False)),
                ('delete_doctor', models.BooleanField(default=False)),
                ('update_doctor', models.BooleanField(default=False)),
                ('add_assistant', models.BooleanField(default=False)),
                ('delete_assistant', models.BooleanField(default=False)),
                ('update_assistant', models.BooleanField(default=False)),
                ('add_trainer', models.BooleanField(default=False)),
                ('delete_trainer', models.BooleanField(default=False)),
                ('update_trainer', models.BooleanField(default=False)),
                ('add_admin', models.BooleanField(default=False)),
                ('delete_admin', models.BooleanField(default=False)),
                ('update_admin', models.BooleanField(default=False)),
                ('add_student', models.BooleanField(default=False)),
                ('delete_student', models.BooleanField(default=False)),
                ('update_student', models.BooleanField(default=False)),
                ('add_course', models.BooleanField(default=False)),
                ('add_schedule', models.BooleanField(default=False)),
                ('add_instructor_schedule', models.BooleanField(default=False)),
                ('add_student_schedule', models.BooleanField(default=False)),
                ('delete_instructor_schedule', models.BooleanField(default=False)),
                ('delete_course', models.BooleanField(default=False)),
                ('open_course', models.BooleanField(default=False)),
                ('upload_materials', models.BooleanField(default=False)),
                ('add_quiz', models.BooleanField(default=False)),
                ('add_task', models.BooleanField(default=False)),
                ('add_post', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='InstructorAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('instructor_type', models.CharField(choices=[('doctor', 'Doctor'), ('assistant', 'Assistant'), ('trainer', 'Trainer')], default='doctor', max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParentAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('national_id', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=70)),
                ('id_college', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='female', max_length=10)),
                ('age', models.IntegerField()),
                ('national_id', models.CharField(max_length=50)),
                ('parent_national_id', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
