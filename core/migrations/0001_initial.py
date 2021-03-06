# Generated by Django 4.0 on 2021-12-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archived', models.DateTimeField(blank=True, editable=False, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='')),
                ('last_name', models.CharField(max_length=50, verbose_name='')),
                ('other_names', models.CharField(max_length=50, verbose_name='')),
                ('proffesion', models.CharField(max_length=50, verbose_name='')),
                ('bio', models.TextField(verbose_name='')),
                ('slug', models.SlugField(verbose_name='')),
            ],
            options={
                'ordering': ['-last_modified'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archived', models.DateTimeField(blank=True, editable=False, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, verbose_name='')),
                ('slug', models.SlugField(verbose_name='')),
            ],
            options={
                'ordering': ['-last_modified'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archived', models.DateTimeField(blank=True, editable=False, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=50, verbose_name='')),
                ('slug', models.SlugField(verbose_name='')),
                ('content', models.TextField(verbose_name='')),
                ('published', models.BooleanField(verbose_name='')),
                ('draft', models.BooleanField(verbose_name='')),
                ('authors', models.ManyToManyField(to='core.Author', verbose_name='')),
                ('tags', models.ManyToManyField(to='core.Tag', verbose_name='')),
            ],
            options={
                'ordering': ['-last_modified'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
