# Generated by Django 2.2.10 on 2021-07-12 19:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0018_auto_20210712_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistrationcourse',
            name='citizenship',
            field=models.CharField(
                choices=[('Polish', 'Polish'), ('Afghan', 'Afghan'), ('Albanian', 'Albanian'), ('Algerian', 'Algerian'),
                         ('American', 'American'), ('Argentinean', 'Argentinean'), ('Armenian', 'Armenian'),
                         ('Australian', 'Australian'), ('Austrian', 'Austrian'), ('Azerbaijani', 'Azerbaijani'),
                         ('Belarusian', 'Belarusian'), ('Belgian', 'Belgian'), ('Bolivian', 'Bolivian'),
                         ('Bosnian', 'Bosnian'), ('Brazilian', 'Brazilian'), ('British', 'British'),
                         ('Bulgarian', 'Bulgarian'), ('Cambodian', 'Cambodian'), ('Cameroonian', 'Cameroonian'),
                         ('Canadian', 'Canadian'), ('Chilean', 'Chilean'), ('Chinese', 'Chinese'),
                         ('Colombian', 'Colombian'), ('Croatian', 'Croatian'), ('Cuban', 'Cuban'),
                         ('Cypriot', 'Cypriot'), ('Czech', 'Czech'), ('Danish', 'Danish'), ('Dominican', 'Dominican'),
                         ('Dutch', 'Dutch'), ('Ecuadorean', 'Ecuadorean'), ('Egyptian', 'Egyptian'),
                         ('Estonian', 'Estonian'), ('Filipino', 'Filipino'), ('Finnish', 'Finnish'),
                         ('French', 'French'), ('Gabonese', 'Gabonese'), ('Georgian', 'Georgian'), ('German', 'German'),
                         ('Greek', 'Greek'), ('Haitian', 'Haitian'), ('Hungarian', 'Hungarian'), ('Indian', 'Indian'),
                         ('Indonesian', 'Indonesian'), ('Iranian', 'Iranian'), ('Iraqi', 'Iraqi'), ('Irish', 'Irish'),
                         ('Israeli', 'Israeli'), ('Italian', 'Italian'), ('Jamaican', 'Jamaican'),
                         ('Japanese', 'Japanese'), ('Jordanian', 'Jordanian'), ('Kazakhstani', 'Kazakhstani'),
                         ('Kenyan', 'Kenyan'), ('Kuwaiti', 'Kuwaiti'), ('Laotian', 'Laotian'), ('Latvian', 'Latvian'),
                         ('Lebanese', 'Lebanese'), ('Liberian', 'Liberian'), ('Libyan', 'Libyan'),
                         ('Lithuanian', 'Lithuanian'), ('Luxembourger', 'Luxembourger'), ('Macedonian', 'Macedonian'),
                         ('Malagasy', 'Malagasy'), ('Malawian', 'Malawian'), ('Malaysian', 'Malaysian'),
                         ('Maltese', 'Maltese'), ('Mauritanian', 'Mauritanian'), ('Mauritian', 'Mauritian'),
                         ('Mexican', 'Mexican'), ('Moldovan', 'Moldovan'), ('Mongolian', 'Mongolian'),
                         ('Moroccan', 'Moroccan'), ('Nepalese', 'Nepalese'), ('Netherlander', 'Netherlander'),
                         ('New Zealander', 'New Zealander'), ('Nigerian', 'Nigerian'), ('Nigerien', 'Nigerien'),
                         ('North Korean', 'North Korean'), ('Norwegian', 'Norwegian'), ('Pakistani', 'Pakistani'),
                         ('Panamanian', 'Panamanian'), ('Peruvian', 'Peruvian'), ('Portuguese', 'Portuguese'),
                         ('Qatari', 'Qatari'), ('Romanian', 'Romanian'), ('Russian', 'Russian'), ('Rwandan', 'Rwandan'),
                         ('Salvadoran', 'Salvadoran'), ('Samoan', 'Samoan'), ('Saudi', 'Saudi'),
                         ('Scottish', 'Scottish'), ('Senegalese', 'Senegalese'), ('Serbian', 'Serbian'),
                         ('Singaporean', 'Singaporean'), ('Slovakian', 'Slovakian'), ('Slovenian', 'Slovenian'),
                         ('Somali', 'Somali'), ('South African', 'South African'), ('South Korean', 'South Korean'),
                         ('Spanish', 'Spanish'), ('Sudanese', 'Sudanese'), ('Swedish', 'Swedish'), ('Swiss', 'Swiss'),
                         ('Syrian', 'Syrian'), ('Taiwanese', 'Taiwanese'), ('Tajik', 'Tajik'),
                         ('Tanzanian', 'Tanzanian'), ('Thai', 'Thai'), ('Tunisian', 'Tunisian'), ('Turkish', 'Turkish'),
                         ('Ugandan', 'Ugandan'), ('Ukrainian', 'Ukrainian'), ('Uruguayan', 'Uruguayan'),
                         ('Uzbekistani', 'Uzbekistani'), ('Venezuelan', 'Venezuelan'), ('Vietnamese', 'Vietnamese'),
                         ('Welsh', 'Welsh'), ('Yemenite', 'Yemenite')], max_length=100, verbose_name='Citizenship'),
        ),
    ]