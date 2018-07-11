# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-11 23:25
from __future__ import unicode_literals

import core.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cluster', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('external_id', models.CharField(blank=True, help_text='An ID representing this instance in an external system', max_length=32, null=True)),
                ('external_source', models.TextField(blank=True, choices=[('HPC', 'HPC'), ('OPS', 'OPS')], null=True)),
                ('title', models.CharField(help_text='Please make sure this matches the name you enter in VISION', max_length=255, verbose_name='Full Name')),
                ('short_title', models.CharField(blank=True, max_length=50)),
                ('alternate_title', models.CharField(blank=True, max_length=255, null=True)),
                ('partner_type', models.CharField(choices=[('B/M', 'Bilateral / Multilateral'), ('CSO', 'Civil Society Organization'), ('Gov', 'Government'), ('UNA', 'UN Agency')], default='Gov', max_length=3)),
                ('shared_partner', models.CharField(choices=[('No', 'No'), ('UND', 'with UNDP'), ('UNF', 'with UNFPA'), ('U&U', 'with UNDP & UNFPA')], default='No', help_text='Partner shared with UNDP or UNFPA?', max_length=3)),
                ('cso_type', models.CharField(blank=True, choices=[('Int', 'International'), ('Nat', 'National'), ('CBO', 'Community Based Organization'), ('AI', 'Academic Institution')], max_length=3, null=True, verbose_name='CSO Type')),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=32, null=True)),
                ('last_assessment_date', models.DateField(blank=True, null=True)),
                ('core_values_assessment_date', models.DateField(blank=True, null=True, verbose_name='Date positively assessed against core values')),
                ('street_address', models.CharField(blank=True, max_length=512, null=True)),
                ('city', models.CharField(blank=True, max_length=64, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=32, null=True)),
                ('country_code', models.CharField(blank=True, choices=[('AF', 'Afghanistan'), ('AX', 'Åland Islands'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BA', 'Bosnia and Herzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('CV', 'Cabo Verde'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmas Island'), ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Congo'), ('CK', 'Cook Islands'), ('CR', 'Costa Rica'), ('CI', "Côte d'Ivoire"), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CW', 'Curaçao'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FK', 'Falkland Islands (Malvinas)'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'), ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heard Island and McDonald Islands'), ('VA', 'Holy See (Vatican City State)'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IM', 'Isle of Man'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KP', 'North Korea'), ('KR', 'South Korea'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', "Lao People's Democratic Republic"), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MK', 'Macedonia'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia'), ('MD', 'Moldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk Island'), ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestine'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RE', 'Réunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('BL', 'Saint Barthélemy'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('MF', 'Saint Martin (French part)'), ('PM', 'Saint Pierre and Miquelon'), ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SX', 'Sint Maarten (Dutch part)'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('GS', 'South Georgia and the South Sandwich Islands'), ('SS', 'South Sudan'), ('SS', 'South Sudan Pound'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SJ', 'Svalbard and Jan Mayen'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syrian Arab Republic'), ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TC', 'Turks and Caicos Islands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'), ('US', 'United States'), ('UM', 'United States Minor Outlying Islands'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela'), ('VN', 'Viet Nam'), ('VG', 'Virgin Islands, British'), ('VI', 'Virgin Islands, U.S.'), ('WF', 'Wallis and Futuna'), ('EH', 'Western Sahara'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=2, null=True)),
                ('total_ct_cp', models.DecimalField(blank=True, decimal_places=2, help_text='Total Cash Transferred for Country Programme', max_digits=12, null=True)),
                ('total_ct_cy', models.DecimalField(blank=True, decimal_places=2, help_text='Total Cash Transferred per Current Year', max_digits=12, null=True)),
                ('vendor_number', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('alternate_id', models.IntegerField(blank=True, null=True)),
                ('rating', models.CharField(blank=True, max_length=50, null=True, verbose_name='Risk Rating')),
                ('basis_for_risk_rating', models.CharField(blank=True, max_length=50, null=True)),
                ('ocha_external_id', core.fields.UniqueNullCharField(blank=True, max_length=128, null=True, unique=True)),
                ('clusters', models.ManyToManyField(related_name='partners', to='cluster.Cluster')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='PartnerActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=2048)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('Ong', 'Ongoing'), ('Pla', 'Planned'), ('Com', 'Completed')], default='Ong', max_length=3)),
                ('cluster_activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner_activities', to='cluster.ClusterActivity')),
                ('cluster_objective', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner_activities', to='cluster.ClusterObjective')),
                ('locations', models.ManyToManyField(related_name='partner_activities', to='core.Location')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_activities', to='partner.Partner')),
            ],
            options={
                'ordering': ['-id'],
                'permissions': (('imo_object', 'IMO Object'), ('partner_object', 'Partner Object')),
            },
        ),
        migrations.CreateModel(
            name='PartnerProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('external_id', models.CharField(blank=True, help_text='An ID representing this instance in an external system', max_length=32, null=True)),
                ('external_source', models.TextField(blank=True, choices=[('HPC', 'HPC'), ('OPS', 'OPS')], null=True)),
                ('code', models.TextField(blank=True, null=True, unique=True, verbose_name='Project code in HRP')),
                ('type', models.CharField(blank=True, choices=[('HRP', 'HRP'), ('FA', 'FA')], help_text='Is this project part of an HRP or FA?', max_length=3, null=True, verbose_name='Plan Type')),
                ('title', models.CharField(max_length=1024)),
                ('description', models.TextField(blank=True, max_length=5120, null=True)),
                ('additional_information', models.CharField(blank=True, max_length=255, null=True, verbose_name='Additional information (e.g. links)')),
                ('custom_fields', django.contrib.postgres.fields.jsonb.JSONField(default=[])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('Ong', 'Ongoing'), ('Pla', 'Planned'), ('Com', 'Completed')], default='Ong', max_length=3)),
                ('agency_name', models.TextField(blank=True, max_length=512, null=True)),
                ('agency_type', models.TextField(blank=True, max_length=128, null=True)),
                ('prioritization', models.TextField(blank=True, null=True, verbose_name='Prioritization Classification')),
                ('total_budget', models.DecimalField(decimal_places=2, help_text='Total Budget (USD)', max_digits=12, null=True)),
                ('funding_source', models.TextField(blank=True, max_length=2048, null=True)),
                ('additional_partners', models.ManyToManyField(blank=True, to='partner.Partner', verbose_name='Additional implementing partners')),
                ('clusters', models.ManyToManyField(related_name='partner_projects', to='cluster.Cluster')),
                ('locations', models.ManyToManyField(related_name='partner_projects', to='core.Location')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_projects', to='partner.Partner')),
            ],
            options={
                'ordering': ['-id'],
                'permissions': (('imo_object', 'IMO Object'), ('partner_object', 'Partner Object')),
            },
        ),
        migrations.CreateModel(
            name='PartnerProjectFunding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('required_funding', models.DecimalField(blank=True, decimal_places=2, max_digits=32, null=True)),
                ('internal_funding', models.DecimalField(blank=True, decimal_places=2, max_digits=32, null=True)),
                ('cerf_funding', models.DecimalField(blank=True, decimal_places=2, max_digits=32, null=True, verbose_name='Central Emergency Response Fund funding')),
                ('cbpf_funding', models.DecimalField(blank=True, decimal_places=2, max_digits=32, null=True, verbose_name='Country based pooled funds funding')),
                ('bilateral_funding', models.DecimalField(blank=True, decimal_places=2, max_digits=32, null=True, verbose_name='Funding from bilateral agreements, not including UNICEF/WFP')),
                ('unicef_funding', models.DecimalField(blank=True, decimal_places=2, max_digits=32, null=True, verbose_name='Funding from UNICEF including supplies cost')),
                ('wfp_funding', models.DecimalField(blank=True, decimal_places=2, max_digits=32, null=True, verbose_name='Funding from WFP including supplies cost')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='partner.PartnerProject')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='partneractivity',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner_activities', to='partner.PartnerProject'),
        ),
        migrations.AlterUniqueTogether(
            name='partnerproject',
            unique_together=set([('external_id', 'external_source')]),
        ),
        migrations.AlterUniqueTogether(
            name='partner',
            unique_together=set([('title', 'vendor_number')]),
        ),
    ]
