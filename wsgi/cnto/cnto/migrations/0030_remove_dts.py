# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnto', '0029_copy_dts_to_dates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='discharge_dt',
        ),
        migrations.RemoveField(
            model_name='member',
            name='join_dt',
        ),
    ]
