CORPS = map(lambda x: x.lower(), ['Inc', \
 'Corporation', \
 'Corp', \
 'Corp.', \
 'GmBH', \
 'Limitada', \
 'I/S', \
 'AB', \
 'Co.' \
 'SAS', \
 'ANS', \
 'LLC', \
 'Limited', \
 'Partnership', \
 'Holdings', \
 'Associates', \
 'Corporate', \
 'Organization', \
 'Company', \
 'B.V', \
 'L.L.C', \
 'LTD', \
 'L.T.D', \
 'G.K.', \
 'SRL', \
 'Pty.', \
 'Productions', \
 'International', \
 'Operations', \
 'LDC', \
 'Incorporated'])

EXCLUDE_CORPS = map(lambda x: x.lower(), ['incorporation'])
JUNK = ['Wholly-owned', 'NAME OF COMPANY', 'STATE OR COUNTRY OF INCORPORATION']


BASE_URL = 'http://www.sec.gov'
EXHIBIT21_WORDS = 'EX-21|EX-21.1|Exhibit 21.1|EXHIBIT 21.1|Exhibit 21|Subsidiaries|exhibit_21-1|SUBSIDIARIES OF THE REGISTRANT'


STATES = map(lambda x: x.lower(), ['Alabama', \
 'Alaska', \
 'Arizona', \
 'Arkansas', \
 'California', \
 'Colorado', \
 'Connecticut', \
 'Delaware', \
 'Florida', \
 'Georgia', \
 'Hawaii', \
 'Idaho', \
 'Illinois', \
 'Indiana', \
 'Iowa', \
 'Kansas', \
 'Kentucky', \
 'Louisiana', \
 'Maine', \
 'Maryland', \
 'Massachusetts', \
 'Michigan', \
 'Minnesota', \
 'Mississippi', \
 'Missouri', \
 'Montana', \
 'Nebraska', \
 'Nevada', \
 'New Hampshire', \
 'New Jersey', \
 'New Mexico', \
 'New York', \
 'North Carolina', \
 'North Dakota', \
 'Ohio', \
 'Oklahoma', \
 'Oregon', \
 'Pennsylvania', \
 'Rhode Island', \
 'South Carolina', \
 'South Dakota', \
 'Tennessee', \
 'Texas', \
 'Utah', \
 'Vermont', \
 'Virginia', \
 'Washington', \
 'West Virginia', \
 'Wisconsin', \
 'Wyoming'])

COUNTRIES = map(lambda x: x.lower(), ['AFGHANISTAN', \
'LAND ISLANDS', \
'ALBANIA', \
'ALGERIA', \
'AMERICAN SAMOA', \
'ANDORRA', \
'ANGOLA', \
'ANGUILLA', \
'ANTARCTICA', \
'ANTIGUA AND BARBUDA', \
'ARGENTINA', \
'ARMENIA', \
'ARUBA', \
'AUSTRALIA', \
'AUSTRIA', \
'AZERBAIJAN', \
'BAHAMAS', \
'BAHRAIN', \
'BANGLADESH', \
'BARBADOS', \
'BELARUS', \
'BELGIUM', \
'BELIZE', \
'BENIN', \
'BERMUDA', \
'BHUTAN', \
'BOLIVIA, \
 PLURINATIONAL STATE OF', \
 'BONAIRE, \
 SINT EUSTATIUS AND SABA', \
 'BOSNIA AND HERZEGOVINA', \
'BOTSWANA', \
'BOUVET ISLAND', \
'BRAZIL', \
'BRITISH INDIAN OCEAN TERRITORY', \
'BRUNEI DARUSSALAM', \
'BULGARIA', \
'BURKINA FASO', \
'BURUNDI', \
'CAMBODIA', \
'CAMEROON', \
'CANADA', \
'CAPE VERDE', \
'CAYMAN ISLANDS', \
'CENTRAL AFRICAN REPUBLIC', \
'CHAD', \
'CHILE', \
'CHINA', \
'CHRISTMAS ISLAND', \
'COCOS (KEELING) ISLANDS', \
'COLOMBIA', \
'COMOROS', \
'CONGO', \
'CONGO, \
 THE DEMOCRATIC REPUBLIC OF THE', \
'COOK ISLANDS', \
'COSTA RICA', \
'CUBA', \
'CYPRUS', \
'CZECH REPUBLIC', \
'DENMARK', \
'DJIBOUTI', \
'DOMINICA', \
'DOMINICAN REPUBLIC', \
'ECUADOR', \
'EGYPT', \
'EL SALVADOR', \
'EQUATORIAL GUINEA', \
'ERITREA', \
'ESTONIA', \
'ETHIOPIA', \
'FALKLAND ISLANDS (MALVINAS)', \
'FAROE ISLANDS', \
'FIJI', \
'FINLAND', \
'FRANCE', \
'FRENCH GUIANA', \
'FRENCH POLYNESIA', \
'FRENCH SOUTHERN TERRITORIES', \
'GABON', \
'GAMBIA', \
'GEORGIA', \
'GERMANY', \
'GHANA', \
'GIBRALTAR', \
'GREECE', \
'GREENLAND', \
'GRENADA', \
'GUADELOUPE', \
'GUAM', \
'GUATEMALA', \
'GUERNSEY', \
'GUINEA', \
'GUINEA-BISSAU', \
'GUYANA', \
'HAITI', \
'HEARD ISLAND AND MCDONALD ISLANDS', \
'HOLY SEE (VATICAN CITY STATE)', \
'HONDURAS', \
'HONG KONG', \
'HUNGARY', \
'ICELAND', \
'INDIA', \
'INDONESIA', \
'IRAN, \
 ISLAMIC REPUBLIC OF', \
 'IRAQ', \
'IRELAND', \
'ISLE OF MAN', \
'ISRAEL', \
'ITALY', \
'JAMAICA', \
'JAPAN', \
'JERSEY', \
'JORDAN', \
'KAZAKHSTAN', \
'KENYA', \
'KIRIBATI', \
'KOREA, \
 DEMOCRATIC PEOPLE\'S REPUBLIC OF', \
 'KOREA, \
 REPUBLIC OF', \
 'KUWAIT', \
'KYRGYZSTAN', \
'LAO PEOPLE\'S DEMOCRATIC REPUBLIC', \
'LATVIA', \
'LEBANON', \
'LESOTHO', \
'LIBERIA', \
'LIBYA', \
'LIECHTENSTEIN', \
'LITHUANIA', \
'LUXEMBOURG', \
'MACAO', \
'MACEDONIA, \
 THE FORMER YUGOSLAV REPUBLIC OF', \
 'MADAGASCAR', \
'MALAWI', \
'MALAYSIA', \
'MALDIVES', \
'MALI', \
'MALTA', \
'MARSHALL ISLANDS', \
'MARTINIQUE', \
'MAURITANIA', \
'MAURITIUS', \
'MAYOTTE', \
'MEXICO', \
'MICRONESIA, \
 FEDERATED STATES OF', \
 'MOLDOVA, \
 REPUBLIC OF', \
 'MONACO', \
'MONGOLIA', \
'MONTENEGRO', \
'MONTSERRAT', \
'MOROCCO', \
'MOZAMBIQUE', \
'MYANMAR', \
'NAMIBIA', \
'NAURU', \
'NEPAL', \
'NETHERLANDS', \
'NEW CALEDONIA', \
'NEW ZEALAND', \
'NICARAGUA', \
'NIGER', \
'NIGERIA', \
'NIUE', \
'NORFOLK ISLAND', \
'NORTHERN MARIANA ISLANDS', \
'NORWAY', \
'OMAN', \
'PAKISTAN', \
'PALAU', \
'PALESTINIAN TERRITORY, \
 OCCUPIED', \
 'PANAMA', \
'PAPUA NEW GUINEA', \
'PARAGUAY', \
'PERU', \
'PHILIPPINES', \
'PITCAIRN', \
'POLAND', \
'PORTUGAL', \
'PUERTO RICO', \
'QATAR', \
'ROMANIA', \
'RUSSIAN FEDERATION', \
'RWANDA', \
'SAINT HELENA, \
 ASCENSION AND TRISTAN DA CUNHA', \
 'SAINT KITTS AND NEVIS', \
'SAINT LUCIA', \
'SAINT MARTIN (FRENCH PART)', \
'SAINT PIERRE AND MIQUELON', \
'SAINT VINCENT AND THE GRENADINES', \
'SAMOA', \
'SAN MARINO', \
'SAO TOME AND PRINCIPE', \
'SAUDI ARABIA', \
'SENEGAL', \
'SERBIA', \
'SEYCHELLES', \
'SIERRA LEONE', \
'SINGAPORE', \
'SINT MAARTEN (DUTCH PART)', \
'SLOVAKIA', \
'SLOVENIA', \
'SOLOMON ISLANDS', \
'SOMALIA', \
'SOUTH AFRICA', \
'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS', \
'SOUTH SUDAN', \
'SPAIN', \
'SRI LANKA', \
'SUDAN', \
'SURINAME', \
'SVALBARD AND JAN MAYEN', \
'SWAZILAND', \
'SWEDEN', \
'SWITZERLAND', \
'SYRIAN ARAB REPUBLIC', \
'TAIWAN, \
 PROVINCE OF CHINA', \
 'TAJIKISTAN', \
'TANZANIA, \
 UNITED REPUBLIC OF', \
 'THAILAND', \
'TIMOR-LESTE', \
'TOGO', \
'TOKELAU', \
'TONGA', \
'TRINIDAD AND TOBAGO', \
'TUNISIA', \
'TURKEY', \
'TURKMENISTAN', \
'TURKS AND CAICOS ISLANDS', \
'TUVALU', \
'UGANDA', \
'UKRAINE', \
'UNITED ARAB EMIRATES', \
'UNITED KINGDOM', \
'UNITED STATES', \
'UNITED STATES MINOR OUTLYING ISLANDS', \
'URUGUAY', \
'UZBEKISTAN', \
'VANUATU', \
'VENEZUELA, \
 BOLIVARIAN REPUBLIC OF', \
 'VIET NAM', \
'VIRGIN ISLANDS, \
 BRITISH', \
 'VIRGIN ISLANDS, \
 U.S.', \
 'WALLIS AND FUTUNA', \
'WESTERN SAHARA', \
'YEMEN', \
'ZAMBIA', \
'ZIMBABWE'])


PLACES = STATES + COUNTRIES
