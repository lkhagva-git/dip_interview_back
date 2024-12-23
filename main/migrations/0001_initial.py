# Generated by Django 5.1.3 on 2024-11-15 09:02

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_count', models.CharField(blank=True, max_length=500, null=True, verbose_name='Хэдэн ярилцлага хийх')),
                ('status', models.IntegerField(blank=True, choices=[(0, '')], null=True, verbose_name='Статус')),
                ('created_at', models.DateField(blank=True, null=True, verbose_name='Үүссэн огноо')),
                ('company', models.CharField(blank=True, max_length=500, null=True, verbose_name='Байгууллага')),
                ('department', models.CharField(blank=True, max_length=500, null=True, verbose_name='Алба, хэлтэс')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='Албан тушаал')),
                ('ethnicity', models.CharField(blank=True, max_length=500, null=True, verbose_name='Иргэний харьяалал')),
                ('family_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Ургийн овог')),
                ('last_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Эцэг эхийн нэр')),
                ('first_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Нэр')),
                ('register_number', models.CharField(blank=True, max_length=500, null=True, verbose_name='Регистрийн дугаар')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Төрсөн огноо')),
                ('email', models.CharField(blank=True, max_length=500, null=True, verbose_name='Имэйл')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Утасны дугаар')),
                ('phone2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Утасны дугаар 2')),
                ('city', models.CharField(blank=True, max_length=500, null=True, verbose_name='Хот')),
                ('district', models.CharField(blank=True, max_length=500, null=True, verbose_name='Дүүрэг')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Бүтэн хаяг')),
                ('sex', models.IntegerField(blank=True, choices=[(0, '')], null=True, verbose_name='Хүйс')),
                ('blood', models.IntegerField(blank=True, choices=[(0, '')], null=True, verbose_name='Цусны бүлэг')),
                ('driver_type', models.IntegerField(blank=True, choices=[(0, '')], null=True, verbose_name='Жолооны ангилал')),
                ('driver_license', models.CharField(blank=True, max_length=500, null=True)),
                ('medical', models.CharField(blank=True, max_length=5000, null=True, verbose_name='Та эрүүл мэндийн хувьд анхаарах ямар нэгэн зовиур байгаа эсэх')),
            ],
            options={
                'verbose_name': 'Анкет',
                'verbose_name_plural': 'Анкет',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('photo', models.ImageField(upload_to='anket/475b67a9fcd6441a955ce9c0099810a2')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Гавьяа шагналын нэр')),
                ('year', models.DateField(blank=True, null=True, verbose_name='Хүртсэн огноо')),
                ('where', models.CharField(blank=True, max_length=500, null=True, verbose_name='Хаана ажиллах хугацаанд шагнагдсан')),
                ('anket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.anket')),
            ],
        ),
        migrations.CreateModel(
            name='CareerContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Нэр')),
                ('last_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Овог')),
                ('company', models.CharField(blank=True, max_length=500, null=True, verbose_name='Байгууллага')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='Албан тушаал')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Утасны дугаар')),
                ('email', models.CharField(blank=True, max_length=500, null=True, verbose_name='Имэйл хаяг')),
                ('anket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.anket')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('AF', 'AFGHANISTAN'), ('AL', 'ALBANIA'), ('DZ', 'ALGERIA'), ('AS', 'AMERICAN SAMOA'), ('AD', 'ANDORRA'), ('AO', 'ANGOLA'), ('AI', 'ANGUILLA'), ('AQ', 'ANTARCTICA'), ('AG', 'ANTIGUA AND BARBUDA'), ('AR', 'ARGENTINA'), ('AM', 'ARMENIA'), ('AW', 'ARUBA'), ('AU', 'AUSTRALIA'), ('AT', 'AUSTRIA'), ('AZ', 'AZERBAIJAN'), ('BS', 'BAHAMAS'), ('BH', 'BAHRAIN'), ('BD', 'BANGLADESH'), ('BB', 'BARBADOS'), ('BY', 'BELARUS'), ('BE', 'BELGIUM'), ('BZ', 'BELIZE'), ('BJ', 'BENIN'), ('BM', 'BERMUDA'), ('BT', 'BHUTAN'), ('BO', 'BOLIVIA'), ('BA', 'BOSNIA AND HERZEGOVINA'), ('BW', 'BOTSWANA'), ('BV', 'BOUVET ISLAND'), ('BR', 'BRAZIL'), ('IO', 'BRITISH INDIAN OCEAN TERRITORY'), ('BN', 'BRUNEI DARUSSALAM'), ('BG', 'BULGARIA'), ('BF', 'BURKINA FASO'), ('BI', 'BURUNDI'), ('KH', 'CAMBODIA'), ('CM', 'CAMEROON'), ('CA', 'CANADA'), ('CV', 'CAPE VERDE'), ('KY', 'CAYMAN ISLANDS'), ('CF', 'CENTRAL AFRICAN REPUBLIC'), ('TD', 'CHAD'), ('CL', 'CHILE'), ('CN', 'CHINA'), ('CX', 'CHRISTMAS ISLAND'), ('CC', 'COCOS (KEELING) ISLANDS'), ('CO', 'COLOMBIA'), ('KM', 'COMOROS'), ('CG', 'CONGO'), ('CD', 'CONGO, THE DEMOCRATIC REPUBLIC OF'), ('CK', 'COOK ISLANDS'), ('CR', 'COSTA RICA'), ('CI', "CÃ”TE D'IVOIRE"), ('HR', 'CROATIA'), ('CU', 'CUBA'), ('CY', 'CYPRUS'), ('CZ', 'CZECH REPUBLIC'), ('DK', 'DENMARK'), ('DJ', 'DJIBOUTI'), ('DM', 'DOMINICA'), ('DO', 'DOMINICAN REPUBLIC'), ('EC', 'ECUADOR'), ('EG', 'EGYPT'), ('SV', 'EL SALVADOR'), ('GQ', 'EQUATORIAL GUINEA'), ('ER', 'ERITREA'), ('EE', 'ESTONIA'), ('ET', 'ETHIOPIA'), ('FK', 'FALKLAND ISLANDS (MALVINAS)'), ('FO', 'FAROE ISLANDS'), ('FJ', 'FIJI'), ('FI', 'FINLAND'), ('FR', 'FRANCE'), ('GF', 'FRENCH GUIANA'), ('PF', 'FRENCH POLYNESIA'), ('TF', 'FRENCH SOUTHERN TERRITORIES'), ('GA', 'GABON'), ('GM', 'GAMBIA'), ('GE', 'GEORGIA'), ('DE', 'GERMANY'), ('GH', 'GHANA'), ('GI', 'GIBRALTAR'), ('GR', 'GREECE'), ('GL', 'GREENLAND'), ('GD', 'GRENADA'), ('GP', 'GUADELOUPE'), ('GU', 'GUAM'), ('GT', 'GUATEMALA'), ('GN', 'GUINEA'), ('GW', 'GUINEA'), ('GY', 'GUYANA'), ('HT', 'HAITI'), ('HM', 'HEARD ISLAND AND MCDONALD ISLANDS'), ('HN', 'HONDURAS'), ('HK', 'HONG KONG'), ('HU', 'HUNGARY'), ('IS', 'ICELAND'), ('IN', 'INDIA'), ('ID', 'INDONESIA'), ('IR', 'IRAN, ISLAMIC REPUBLIC OF'), ('IQ', 'IRAQ'), ('IE', 'IRELAND'), ('IL', 'ISRAEL'), ('IT', 'ITALY'), ('JM', 'JAMAICA'), ('JP', 'JAPAN'), ('JO', 'JORDAN'), ('KZ', 'KAZAKHSTAN'), ('KE', 'KENYA'), ('KI', 'KIRIBATI'), ('KP', "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF"), ('KR', 'KOREA, REPUBLIC OF'), ('KW', 'KUWAIT'), ('KG', 'KYRGYZSTAN'), ('LA', "LAO PEOPLE'S DEMOCRATIC REPUBLIC"), ('LV', 'LATVIA'), ('LB', 'LEBANON'), ('LS', 'LESOTHO'), ('LR', 'LIBERIA'), ('LY', 'LIBYAN ARAB JAMAHIRIYA'), ('LI', 'LIECHTENSTEIN'), ('LT', 'LITHUANIA'), ('LU', 'LUXEMBOURG'), ('MO', 'MACAO'), ('MK', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF'), ('MG', 'MADAGASCAR'), ('MW', 'MALAWI'), ('MY', 'MALAYSIA'), ('MV', 'MALDIVES'), ('ML', 'MALI'), ('MT', 'MALTA'), ('MH', 'MARSHALL ISLANDS'), ('MQ', 'MARTINIQUE'), ('MR', 'MAURITANIA'), ('MU', 'MAURITIUS'), ('YT', 'MAYOTTE'), ('MX', 'MEXICO'), ('FM', 'MICRONESIA, FEDERATED STATES OF'), ('MD', 'MOLDOVA, REPUBLIC OF'), ('MC', 'MONACO'), ('MN', 'MONGOLIA'), ('MS', 'MONTSERRAT'), ('MA', 'MOROCCO'), ('MZ', 'MOZAMBIQUE'), ('MM', 'MYANMAR'), ('NA', 'NAMIBIA'), ('NR', 'NAURU'), ('NP', 'NEPAL'), ('NL', 'NETHERLANDS'), ('AN', 'NETHERLANDS ANTILLES'), ('NC', 'NEW CALEDONIA'), ('NZ', 'NEW ZEALAND'), ('NI', 'NICARAGUA'), ('NE', 'NIGER'), ('NG', 'NIGERIA'), ('NU', 'NIUE'), ('NF', 'NORFOLK ISLAND'), ('MP', 'NORTHERN MARIANA ISLANDS'), ('NO', 'NORWAY'), ('OM', 'OMAN'), ('PK', 'PAKISTAN'), ('PW', 'PALAU'), ('PS', 'PALESTINIAN TERRITORY, OCCUPIED'), ('PA', 'PANAMA'), ('PG', 'PAPUA NEW GUINEA'), ('PY', 'PARAGUAY'), ('PE', 'PERU'), ('PH', 'PHILIPPINES'), ('PN', 'PITCAIRN'), ('PL', 'POLAND'), ('PT', 'PORTUGAL'), ('PR', 'PUERTO RICO'), ('QA', 'QATAR'), ('RE', 'RÃ‰UNION'), ('RO', 'ROMANIA'), ('RU', 'RUSSIAN FEDERATION'), ('RW', 'RWANDA'), ('SH', 'SAINT HELENA'), ('KN', 'SAINT KITTS AND NEVIS'), ('LC', 'SAINT LUCIA'), ('PM', 'SAINT PIERRE AND MIQUELON'), ('VC', 'SAINT VINCENT AND THE GRENADINES'), ('WS', 'SAMOA'), ('SM', 'SAN MARINO'), ('ST', 'SAO TOME AND PRINCIPE'), ('SA', 'SAUDI ARABIA'), ('SN', 'SENEGAL'), ('CS', 'SERBIA AND MONTENEGRO'), ('SC', 'SEYCHELLES'), ('SL', 'SIERRA LEONE'), ('SG', 'SINGAPORE'), ('SK', 'SLOVAKIA'), ('SI', 'SLOVENIA'), ('SB', 'SOLOMON ISLANDS'), ('SO', 'SOMALIA'), ('ZA', 'SOUTH AFRICA'), ('GS', 'SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS'), ('ES', 'SPAIN'), ('LK', 'SRI LANKA'), ('SD', 'SUDAN'), ('SR', 'SURINAME'), ('SJ', 'SVALBARD AND JAN MAYEN'), ('SZ', 'SWAZILAND'), ('SE', 'SWEDEN'), ('CH', 'SWITZERLAND'), ('SY', 'SYRIAN ARAB REPUBLIC'), ('TW', 'TAIWAN, PROVINCE OF CHINA'), ('TJ', 'TAJIKISTAN'), ('TZ', 'TANZANIA, UNITED REPUBLIC OF'), ('TH', 'THAILAND'), ('TL', 'TIMOR'), ('TG', 'TOGO'), ('TK', 'TOKELAU'), ('TO', 'TONGA'), ('TT', 'TRINIDAD AND TOBAGO'), ('TN', 'TUNISIA'), ('TR', 'TURKEY'), ('TM', 'TURKMENISTAN'), ('TC', 'TURKS AND CAICOS ISLANDS'), ('TV', 'TUVALU'), ('UG', 'UGANDA'), ('UA', 'UKRAINE'), ('AE', 'UNITED ARAB EMIRATES'), ('GB', 'UNITED KINGDOM'), ('US', 'UNITED STATES'), ('UM', 'UNITED STATES MINOR OUTLYING ISLANDS'), ('UY', 'URUGUAY'), ('UZ', 'UZBEKISTAN'), ('VU', 'VANUATU'), ('VN', 'VIET NAM'), ('VG', 'VIRGIN ISLANDS, BRITISH'), ('VI', 'VIRGIN ISLANDS, U.S.'), ('WF', 'WALLIS AND FUTUNA'), ('EH', 'WESTERN SAHARA'), ('YE', 'YEMEN'), ('ZW', 'ZIMBABWE')], default='MN', max_length=10)),
                ('school_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Сургуулийн нэр')),
                ('degree_level', models.IntegerField(blank=True, choices=[(1, 'Дээд (Бакалавр)'), (2, 'Дээд (Магистр)'), (3, 'Дээд (Доктор)'), (4, 'Тусгай дунд'), (5, 'Бүрэн дунд')], null=True, verbose_name='Боловсролын зэрэг')),
                ('start_date', models.DateField(blank=True, max_length=500, null=True, verbose_name='Элссэн он')),
                ('end_date', models.DateField(blank=True, max_length=500, null=True, verbose_name='Төгссөн он')),
                ('profession', models.CharField(blank=True, max_length=500, null=True, verbose_name='Эзэмшсэн мэргэжил')),
                ('gpa', models.CharField(blank=True, max_length=500, null=True, verbose_name='Үнэлгээ')),
                ('anket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.anket')),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what', models.IntegerField(blank=True, choices=[(1, 'Авга'), (2, 'Ах'), (3, 'Ач'), (4, 'Баз'), (5, 'Бэр'), (6, 'Өвөө'), (7, 'Дүү'), (8, 'Зээ'), (9, 'Нагац'), (10, 'Найз бүсгүй'), (11, 'Найз залуу'), (12, 'Нөхөр'), (13, 'Охин'), (14, 'Хадам ах'), (15, 'Хадам дүү'), (16, 'Хадам эгч'), (17, 'Хадам эх'), (18, 'Хадам эцэг'), (19, 'Хамтран амьдрагч'), (20, 'Хүргэн'), (21, 'Хүү'), (22, 'Эгч'), (23, 'Эмээ'), (24, 'Эх'), (25, 'Эхнэр'), (26, 'Эцэг'), (98, 'Найз'), (99, 'Бусад')], null=True)),
                ('first_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Нэр')),
                ('last_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Овог')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Төрсөн огноо')),
                ('profession', models.CharField(blank=True, max_length=500, null=True, verbose_name='Мэргэжил')),
                ('company', models.CharField(blank=True, max_length=500, null=True, verbose_name='Байгууллага')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='Албан тушаал')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Утасны дугаар')),
                ('is_emergency_contact', models.BooleanField(default=False, verbose_name='Яаралтай үед холбогдох эсэх')),
                ('is_live_together', models.BooleanField(default=False, verbose_name='Цуг амьдардаг эсэх')),
                ('anket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.anket')),
            ],
        ),
        migrations.AddField(
            model_name='anket',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.image'),
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, max_length=100, null=True, verbose_name='Хэд дэх ярилцлага')),
                ('status', models.IntegerField(blank=True, choices=[(0, '')], null=True, verbose_name='Ярилцлагийн статус')),
                ('last_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Овог')),
                ('first_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Нэр')),
                ('interviewed_date', models.DateField(blank=True, null=True, verbose_name='Ярилцлага хийсэн огноо')),
                ('company', models.CharField(blank=True, max_length=500, null=True, verbose_name='Байгууллага')),
                ('department', models.CharField(blank=True, max_length=500, null=True, verbose_name='Алба хэлтэс')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='Албан тушаал')),
                ('pros', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Анхаарал татсан чадварууд')),
                ('cons', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ажиглагдсан сул тал')),
                ('main_overall', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ерөнхий дүгнэлт')),
                ('conclution_points', models.IntegerField(blank=True, null=True, verbose_name='Нэгдсэн дүгнэлт (оноо)')),
                ('possible_date', models.DateField(blank=True, max_length=500, null=True, verbose_name='Ажилд орох боломжтой огноо')),
                ('additional_note', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Нэмэлт тайлбар/тэмдэглэгээ')),
                ('communication', models.IntegerField(blank=True, choices=[(1, 'Хангалтгүй'), (2, 'Дунджаас доогуур'), (3, 'Дундаж'), (4, 'Сайн'), (5, 'Маш сайн')], null=True, verbose_name='Харилцаа өөрийгөө илэрхийлэх чадвар')),
                ('appearance', models.IntegerField(blank=True, choices=[(1, 'Хангалтгүй'), (2, 'Дунджаас доогуур'), (3, 'Дундаж'), (4, 'Сайн'), (5, 'Маш сайн')], null=True, verbose_name='Гадаад төрх')),
                ('logic_skill', models.IntegerField(blank=True, choices=[(1, 'Хангалтгүй'), (2, 'Дунджаас доогуур'), (3, 'Дундаж'), (4, 'Сайн'), (5, 'Маш сайн')], null=True, verbose_name='Харилцаа өөрийгөө илэрхийлэх чадвар')),
                ('attitude', models.IntegerField(blank=True, choices=[(1, 'Хангалтгүй'), (2, 'Дунджаас доогуур'), (3, 'Дундаж'), (4, 'Сайн'), (5, 'Маш сайн')], null=True, verbose_name='Харилцаа өөрийгөө илэрхийлэх чадвар')),
                ('independence', models.IntegerField(blank=True, choices=[(1, 'Хангалтгүй'), (2, 'Дунджаас доогуур'), (3, 'Дундаж'), (4, 'Сайн'), (5, 'Маш сайн')], null=True, verbose_name='Харилцаа өөрийгөө илэрхийлэх чадвар')),
                ('responsibility', models.IntegerField(blank=True, choices=[(1, 'Хангалтгүй'), (2, 'Дунджаас доогуур'), (3, 'Дундаж'), (4, 'Сайн'), (5, 'Маш сайн')], null=True, verbose_name='Харилцаа өөрийгөө илэрхийлэх чадвар')),
                ('leadership', models.IntegerField(blank=True, choices=[(1, 'Хангалтгүй'), (2, 'Дунджаас доогуур'), (3, 'Дундаж'), (4, 'Сайн'), (5, 'Маш сайн')], null=True, verbose_name='Харилцаа өөрийгөө илэрхийлэх чадвар')),
                ('knowledge', models.IntegerField(blank=True, choices=[(1, 'Хангалтгүй'), (2, 'Дунджаас доогуур'), (3, 'Дундаж'), (4, 'Сайн'), (5, 'Маш сайн')], null=True, verbose_name='Харилцаа өөрийгөө илэрхийлэх чадвар')),
                ('overall_score', models.IntegerField(blank=True, choices=[(1, 'Хангалтгүй'), (2, 'Дунджаас доогуур'), (3, 'Дундаж'), (4, 'Сайн'), (5, 'Маш сайн')], null=True, verbose_name='Харилцаа өөрийгөө илэрхийлэх чадвар')),
                ('anket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.anket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Desicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desicion_type', models.IntegerField(blank=True, choices=[(0, 'Ажилд авах'), (1, 'Санал болгох'), (2, 'Санал болгохгүй'), (3, 'Ажлаас гаргах'), (4, 'Нөөцөнд хадгалах'), (5, 'Уулзалт товлох'), (6, 'Ажилд авахгүй')], null=True, verbose_name='Шийдвэрийн төрөл')),
                ('created_at', models.DateField(blank=True, null=True, verbose_name='Үүссэн огноо')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.interview')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Нэр')),
                ('listening', models.IntegerField(blank=True, choices=[(0, '0%'), (10, '10%'), (20, '20%'), (30, '30%'), (40, '40%'), (50, '50%'), (60, '60%'), (70, '70%'), (80, '80%'), (90, '90%'), (100, '100%')], null=True, verbose_name='Сонсоод ойлгох чадвар')),
                ('reading', models.IntegerField(blank=True, choices=[(0, '0%'), (10, '10%'), (20, '20%'), (30, '30%'), (40, '40%'), (50, '50%'), (60, '60%'), (70, '70%'), (80, '80%'), (90, '90%'), (100, '100%')], null=True, verbose_name='Уншаад ойлгох чадвар')),
                ('writing', models.IntegerField(blank=True, choices=[(0, '0%'), (10, '10%'), (20, '20%'), (30, '30%'), (40, '40%'), (50, '50%'), (60, '60%'), (70, '70%'), (80, '80%'), (90, '90%'), (100, '100%')], null=True, verbose_name='Бичих чадвар')),
                ('speaking', models.IntegerField(blank=True, choices=[(0, '0%'), (10, '10%'), (20, '20%'), (30, '30%'), (40, '40%'), (50, '50%'), (60, '60%'), (70, '70%'), (80, '80%'), (90, '90%'), (100, '100%')], null=True, verbose_name='Ярих чадвар')),
                ('anket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.anket')),
            ],
        ),
        migrations.CreateModel(
            name='PriorCareer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=500, null=True, verbose_name='Байгууллага')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='Албан тушаал')),
                ('salary', models.CharField(blank=True, max_length=500, null=True, verbose_name='Цалингийн хэмжээ')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Орсон огноо')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Гарсан огноо')),
                ('leave_reason', models.CharField(blank=True, max_length=500, null=True, verbose_name='Гарсан шалтгаан')),
                ('anket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.anket')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.IntegerField(choices=[(0, 'Хүний нөөцийн ажилтан'), (1, 'Захирал'), (2, 'Админ')], default=0, verbose_name='Хэрэглэгчийн төрөл')),
                ('company', models.CharField(blank=True, max_length=500, null=True, verbose_name='Байгууллага')),
                ('department', models.CharField(blank=True, max_length=500, null=True, verbose_name='Алба хэлтэс')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='Албан тушаал')),
                ('first_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Нэр')),
                ('last_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Овог')),
                ('email', models.CharField(blank=True, max_length=500, null=True, verbose_name='Имэйл хаяг')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Хаяг')),
                ('date_time', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('anket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.anket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Нэр')),
                ('duration', models.CharField(blank=True, max_length=100, null=True, verbose_name='Хугацаа')),
                ('award', models.CharField(blank=True, max_length=500, null=True, verbose_name='Зэрэг, шагналтай эсэх')),
                ('anket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.anket')),
            ],
        ),
    ]
