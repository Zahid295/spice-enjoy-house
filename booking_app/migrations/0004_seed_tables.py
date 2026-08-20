from django.db import migrations


def seed_tables(apps, schema_editor):
    Table = apps.get_model('booking_app', 'Table')
    for table_name in ('Window View', 'Cozy Corner', 'Family Booth'):
        Table.objects.get_or_create(name=table_name)


def remove_seeded_tables(apps, schema_editor):
    Table = apps.get_model('booking_app', 'Table')
    Table.objects.filter(
        name__in=('Window View', 'Cozy Corner', 'Family Booth')
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('booking_app', '0003_alter_booking_guest_name_alter_table_name'),
    ]

    operations = [
        migrations.RunPython(seed_tables, remove_seeded_tables),
    ]
