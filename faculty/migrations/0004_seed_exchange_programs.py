from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_exchange_program'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                INSERT INTO faculty_exchangeprogram (university, languages, places, deadline, description) VALUES
                ('Uniwersytet Warszawski, Польща', 'польська, англійська', '5', '2026-11-15', ''),
                ('KU Leuven (Бельгія)', 'English', '2 місця', '2026-12-01', ''),
                ('Vilnius University, Литва', 'англійська', 'до 4', '2026-10-20', ''),
                ('Uniwersytet Jagielloński, Польща', 'Польська, Англійська', '3', '2026-11-15', ''),
                ('University of Tartu - Естонія', 'англійська, естонська', '2', '2027-01-10', ''),
                ('Masaryk University, Чехія', 'англійська', '1 місце', '2026-09-30', '');
            """,
            reverse_sql="""
                DELETE FROM faculty_exchangeprogram WHERE university IN (
                    'Uniwersytet Warszawski, Польща',
                    'KU Leuven (Бельгія)',
                    'Vilnius University, Литва',
                    'Uniwersytet Jagielloński, Польща',
                    'University of Tartu - Естонія',
                    'Masaryk University, Чехія'
                );
            """,
        ),
    ]
