from django.db import migrations, models


def split_university(value):
    if ', ' in value:
        university, country = value.split(', ')
        return university, country
    if ' - ' in value:
        university, country = value.split(' - ')
        return university, country
    if ' (' in value:
        university, country = value.split(' (')
        return university, country.removesuffix(')')
    return value, ''


def extract_places(value):
    if value.startswith('до '):
        return int(value.removeprefix('до '))
    if value.endswith((' місце', ' місця')):
        return int(value.split(' ')[0])
    return int(value)


def split_country_and_places(apps, schema_editor):
    ExchangeProgram = apps.get_model('faculty', 'ExchangeProgram')
    for exchange_program in ExchangeProgram.objects.all():
        exchange_program.university, exchange_program.country = split_university(exchange_program.university)
        exchange_program.places = extract_places(exchange_program.places)
        exchange_program.save()


def join_country(apps, schema_editor):
    ExchangeProgram = apps.get_model('faculty', 'ExchangeProgram')
    for exchange_program in ExchangeProgram.objects.exclude(country=''):
        exchange_program.university = f'{exchange_program.university}, {exchange_program.country}'
        exchange_program.save()


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_seed_exchange_programs'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangeprogram',
            name='country',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.RunPython(split_country_and_places, join_country),
        migrations.AlterField(
            model_name='exchangeprogram',
            name='places',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
