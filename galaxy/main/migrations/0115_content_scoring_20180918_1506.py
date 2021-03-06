import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import galaxy.main.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0114_content_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentRule',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('rule_id', models.CharField(max_length=25)),
                ('linter_id', models.CharField(
                    choices=[
                        ('flake8', 'flake8'),
                        ('yamllint', 'yamllint'),
                        ('ansible-lint', 'ansible-lint')],
                    max_length=25)),
                ('severity', models.IntegerField(
                    default=0,
                    validators=[
                        django.core.validators.MinValueValidator(0),
                        django.core.validators.MaxValueValidator(5)])),
            ],
            bases=(models.Model, galaxy.main.mixins.DirtyMixin),
        ),
        migrations.AddField(
            model_name='content',
            name='compatibility_score',
            field=models.FloatField(
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AddField(
            model_name='content',
            name='content_score',
            field=models.FloatField(
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AddField(
            model_name='content',
            name='metadata_score',
            field=models.FloatField(
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AddField(
            model_name='content',
            name='quality_score',
            field=models.FloatField(
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AddField(
            model_name='importtaskmessage',
            name='content',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='messages',
                to='main.Content'),
        ),
        migrations.AddField(
            model_name='importtaskmessage',
            name='content_name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='importtaskmessage',
            name='is_linter_rule_violation',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='importtaskmessage',
            name='linter_rule_id',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='importtaskmessage',
            name='linter_type',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='importtaskmessage',
            name='rule_desc',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='importtaskmessage',
            name='rule_severity',
            field=models.IntegerField(
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='repository',
            name='quality_score',
            field=models.FloatField(
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='contenttype',
            name='name',
            field=models.CharField(
                choices=[
                    ('apb', 'Ansible Playbook Bundle'),
                    ('role', 'Role'),
                    ('module', 'Module'),
                    ('module_utils', 'Module Utils'),
                    ('action', 'Action Plugin'),
                    ('cache', 'Cache Plugin'),
                    ('callback', 'Callback Plugin'),
                    ('cliconf', 'CLI Conf Plugin'),
                    ('connection', 'Connection Plugin'),
                    ('filter', 'Filter Plugin'),
                    ('inventory', 'Inventory Plugin'),
                    ('lookup', 'Lookup Plugin'),
                    ('netconf', 'Netconf Plugin'),
                    ('shell', 'Shell Plugin'),
                    ('strategy', 'Strategy Plugin'),
                    ('terminal', 'Terminal Plugin'),
                    ('test', 'Test Plugin')],
                db_index=True,
                max_length=512,
                unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='contentrule',
            unique_together={('rule_id', 'linter_id')},
        ),
    ]
