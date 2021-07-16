# Generated by Django 2.2.10 on 2021-07-14 13:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0023_auto_20210713_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistrationcourse',
            name='citizenship',
            field=models.CharField(
                choices=[('', 'Select...'), ('Polish', 'Polish'), ('Afghan', 'Afghan'), ('Albanian', 'Albanian'),
                         ('Algerian', 'Algerian'), ('American', 'American'), ('Argentinean', 'Argentinean'),
                         ('Armenian', 'Armenian'), ('Australian', 'Australian'), ('Austrian', 'Austrian'),
                         ('Azerbaijani', 'Azerbaijani'), ('Belarusian', 'Belarusian'), ('Belgian', 'Belgian'),
                         ('Bolivian', 'Bolivian'), ('Bosnian', 'Bosnian'), ('Brazilian', 'Brazilian'),
                         ('British', 'British'), ('Bulgarian', 'Bulgarian'), ('Cambodian', 'Cambodian'),
                         ('Cameroonian', 'Cameroonian'), ('Canadian', 'Canadian'), ('Chilean', 'Chilean'),
                         ('Chinese', 'Chinese'), ('Colombian', 'Colombian'), ('Croatian', 'Croatian'),
                         ('Cuban', 'Cuban'), ('Cypriot', 'Cypriot'), ('Czech', 'Czech'), ('Danish', 'Danish'),
                         ('Dominican', 'Dominican'), ('Dutch', 'Dutch'), ('Ecuadorean', 'Ecuadorean'),
                         ('Egyptian', 'Egyptian'), ('Estonian', 'Estonian'), ('Filipino', 'Filipino'),
                         ('Finnish', 'Finnish'), ('French', 'French'), ('Gabonese', 'Gabonese'),
                         ('Georgian', 'Georgian'), ('German', 'German'), ('Greek', 'Greek'), ('Haitian', 'Haitian'),
                         ('Hungarian', 'Hungarian'), ('Indian', 'Indian'), ('Indonesian', 'Indonesian'),
                         ('Iranian', 'Iranian'), ('Iraqi', 'Iraqi'), ('Irish', 'Irish'), ('Israeli', 'Israeli'),
                         ('Italian', 'Italian'), ('Jamaican', 'Jamaican'), ('Japanese', 'Japanese'),
                         ('Jordanian', 'Jordanian'), ('Kazakhstani', 'Kazakhstani'), ('Kenyan', 'Kenyan'),
                         ('Kuwaiti', 'Kuwaiti'), ('Laotian', 'Laotian'), ('Latvian', 'Latvian'),
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
        migrations.AlterField(
            model_name='userregistrationcourse',
            name='country',
            field=models.CharField(
                choices=[('', 'Select...'), ('AF', 'Afghanistan'), ('AX', 'Åland Islands'), ('AL', 'Albania'),
                         ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'),
                         ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'),
                         ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'),
                         ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'),
                         ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'),
                         ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia (Plurinational State of)'),
                         ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BA', 'Bosnia and Herzegovina'),
                         ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'),
                         ('IO', 'British Indian Ocean Territory'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'),
                         ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('CV', 'Cabo Verde'), ('KH', 'Cambodia'),
                         ('CM', 'Cameroon'), ('CA', 'Canada'), ('KY', 'Cayman Islands'),
                         ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'),
                         ('CX', 'Christmas Island'), ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'),
                         ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Congo (the Democratic Republic of the)'),
                         ('CK', 'Cook Islands'), ('CR', 'Costa Rica'), ('CI', "Côte d'Ivoire"), ('HR', 'Croatia'),
                         ('CU', 'Cuba'), ('CW', 'Curaçao'), ('CY', 'Cyprus'), ('CZ', 'Czechia'), ('DK', 'Denmark'),
                         ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'),
                         ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'),
                         ('EE', 'Estonia'), ('SZ', 'Eswatini'), ('ET', 'Ethiopia'),
                         ('FK', 'Falkland Islands (Malvinas)'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'),
                         ('FI', 'Finland'), ('FR', 'France'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'),
                         ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'),
                         ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'),
                         ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'),
                         ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'),
                         ('HT', 'Haiti'), ('HM', 'Heard Island and McDonald Islands'), ('VA', 'Holy See'),
                         ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'),
                         ('ID', 'Indonesia'), ('IR', 'Iran (Islamic Republic of)'), ('IQ', 'Iraq'), ('IE', 'Ireland'),
                         ('IM', 'Isle of Man'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'),
                         ('JE', 'Jersey'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'),
                         ('KP', "Korea (the Democratic People's Republic of)"), ('KR', 'Korea (the Republic of)'),
                         ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', "Lao People's Democratic Republic"),
                         ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'),
                         ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'),
                         ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'),
                         ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'),
                         ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'),
                         ('FM', 'Micronesia (Federated States of)'), ('MD', 'Moldova (the Republic of)'),
                         ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'),
                         ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'),
                         ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'),
                         ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'),
                         ('NF', 'Norfolk Island'), ('MK', 'North Macedonia'), ('MP', 'Northern Mariana Islands'),
                         ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'),
                         ('PS', 'Palestine, State of'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'),
                         ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'),
                         ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'),
                         ('RE', 'Réunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'),
                         ('BL', 'Saint Barthélemy'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'),
                         ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('MF', 'Saint Martin (French part)'),
                         ('PM', 'Saint Pierre and Miquelon'), ('VC', 'Saint Vincent and the Grenadines'),
                         ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'),
                         ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'),
                         ('SG', 'Singapore'), ('SX', 'Sint Maarten (Dutch part)'), ('SK', 'Slovakia'),
                         ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'),
                         ('GS', 'South Georgia and the South Sandwich Islands'), ('SS', 'South Sudan'), ('ES', 'Spain'),
                         ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SJ', 'Svalbard and Jan Mayen'),
                         ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syrian Arab Republic'),
                         ('TW', 'Taiwan (Province of China)'), ('TJ', 'Tajikistan'),
                         ('TZ', 'Tanzania, the United Republic of'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'),
                         ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'),
                         ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'),
                         ('TC', 'Turks and Caicos Islands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'),
                         ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'),
                         ('UM', 'United States Minor Outlying Islands'), ('US', 'United States of America'),
                         ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'),
                         ('VE', 'Venezuela (Bolivarian Republic of)'), ('VN', 'Viet Nam'),
                         ('VG', 'Virgin Islands (British)'), ('VI', 'Virgin Islands (U.S.)'),
                         ('WF', 'Wallis and Futuna'), ('EH', 'Western Sahara'), ('YE', 'Yemen'), ('ZM', 'Zambia'),
                         ('ZW', 'Zimbabwe'), ('ZZ', 'Unknown or unspecified country')], default='ZZ', max_length=30,
                verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='userregistrationcourse',
            name='education',
            field=models.CharField(
                choices=[('', 'Select...'), ('1', 'Pre-primary'), ('2', 'Primary'), ('3', 'Secondary'),
                         ('4', 'High school'), ('5', 'Higher')], max_length=1, verbose_name='Education'),
        ),
        migrations.AlterField(
            model_name='userregistrationcourse',
            name='gender',
            field=models.CharField(choices=[('', 'Select...'), ('M', 'Male'), ('F', 'Female')], max_length=1,
                                   verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='userregistrationcourse',
            name='status',
            field=models.CharField(
                choices=[('', 'Select...'), ('employed', 'Employed'), ('registered', 'Registered unemployed'),
                         ('unregistered', 'Unregistered unemployed'), ('looking', 'Unemployed, not looking for work')],
                max_length=1000, verbose_name='What is your current status on the labor market?'),
        ),
    ]
