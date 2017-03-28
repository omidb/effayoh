from effayoh.rectification.political_entities import FAOPolitEnt
from effayoh.mungers import FAOCountry

map = {
    FAOCountry("Afghanistan", "2"): FAOPolitEnt.AFGHANISTAN,
    FAOCountry("Albania", "3"): FAOPolitEnt.ALBANIA,
    FAOCountry("Algeria", "4"): FAOPolitEnt.ALGERIA,
    FAOCountry("Andorra", "6"): FAOPolitEnt.ANDORRA,
    FAOCountry("Angola", "7"): FAOPolitEnt.ANGOLA,
    FAOCountry("Anguilla", "258"): FAOPolitEnt.ANGUILLA,
    FAOCountry("Antarctica", "30"): FAOPolitEnt.ANTARCTICA,
    FAOCountry("Antigua and Barbuda", "8"): FAOPolitEnt.ANTIGUA_AND_BARBUDA,
    FAOCountry("Argentina", "9"): FAOPolitEnt.ARGENTINA,
    FAOCountry("Armenia", "1"): FAOPolitEnt.ARMENIA,
    FAOCountry("Aruba", "22"): FAOPolitEnt.ARUBA,
    FAOCountry("Australia", "10"): FAOPolitEnt.AUSTRALIA,
    FAOCountry("Austria", "11"): FAOPolitEnt.AUSTRIA,
    FAOCountry("Azerbaijan", "52"): FAOPolitEnt.AZERBAIJAN,
    FAOCountry("Bahamas", "12"): FAOPolitEnt.BAHAMAS,
    FAOCountry("Bahrain", "13"): FAOPolitEnt.BAHRAIN,
    FAOCountry("Bangladesh", "16"): FAOPolitEnt.BANGLADESH,
    FAOCountry("Barbados", "14"): FAOPolitEnt.BARBADOS,
    FAOCountry("Belarus", "57"): FAOPolitEnt.BELARUS,
    FAOCountry("Belgium", "255"): FAOPolitEnt.BELGIUM,
    FAOCountry("Belgium-Luxembourg", "15"): FAOPolitEnt.BELGIUM_LUXEMBOURG,
    FAOCountry("Belize", "23"): FAOPolitEnt.BELIZE,
    FAOCountry("Benin", "53"): FAOPolitEnt.BENIN,
    FAOCountry("Bermuda", "17"): FAOPolitEnt.BERMUDA,
    FAOCountry("Bhutan", "18"): FAOPolitEnt.BHUTAN,
    FAOCountry("Bolivia (Plurinational State of)", "19"): FAOPolitEnt.BOLIVIA,
    FAOCountry("Bosnia and Herzegovina", "80"): FAOPolitEnt.BOSNIA_AND_HERZEGOVINA,
    FAOCountry("Botswana", "20"): FAOPolitEnt.BOTSWANA,
    FAOCountry("Bouvet Island", "31"): FAOPolitEnt.BOUVET_ISLAND,
    FAOCountry("Brazil", "21"): FAOPolitEnt.BRAZIL,
    FAOCountry("British Indian Ocean Territory", "24"): FAOPolitEnt.BRITISH_INDIAN_OCEAN_TERRITORY,
    FAOCountry("Brunei Darussalam", "26"): FAOPolitEnt.BRUNEI_DARUSSALAM,
    FAOCountry("Bulgaria", "27"): FAOPolitEnt.BULGARIA,
    FAOCountry("Burkina Faso", "233"): FAOPolitEnt.BURKINA_FASO,
    FAOCountry("Burundi", "29"): FAOPolitEnt.BURUNDI,
    FAOCountry("Cabo Verde", "35"): FAOPolitEnt.CABO_VERDE,
    FAOCountry("Cambodia", "115"): FAOPolitEnt.CAMBODIA,
    FAOCountry("Cameroon", "32"): FAOPolitEnt.CAMEROON,
    FAOCountry("Canada", "33"): FAOPolitEnt.CANADA,
    FAOCountry("Caribbean", "5206"): FAOPolitEnt.CARIBBEAN,
    FAOCountry("Cayman Islands", "36"): FAOPolitEnt.CAYMAN_ISLANDS,
    FAOCountry("Central African Republic", "37"): FAOPolitEnt.CENTRAL_AFRICAN_REPUBLIC,
    FAOCountry("Chad", "39"): FAOPolitEnt.CHAD,
    FAOCountry("Channel Islands", "259"): FAOPolitEnt.CHANNEL_ISLANDS,
    FAOCountry("Chile", "40"): FAOPolitEnt.CHILE,
    FAOCountry("China", "351"): FAOPolitEnt.CHINA,
    FAOCountry("China (exc. Hong Kong & Macao)", "357"): FAOPolitEnt.CHINA_EXC_HK_MACAO,
    FAOCountry("China, Hong Kong SAR", "96"): FAOPolitEnt.CHINA_HK_SAR,
    FAOCountry("China, Macao SAR", "128"): FAOPolitEnt.CHINA_MACAO_SAR,
    FAOCountry("China, mainland", "41"): FAOPolitEnt.CHINA_MAINLAND,
    FAOCountry("China, Taiwan Province of", "214"): FAOPolitEnt.CHINA_TAIWAN,
    FAOCountry("Christmas Island", "42"): FAOPolitEnt.CHRISTMAS_ISLAND,
    FAOCountry("Cocos (Keeling) Islands", "43"): FAOPolitEnt.COCOS,
    FAOCountry("Colombia", "44"): FAOPolitEnt.COLOMBIA,
    FAOCountry("Comoros", "45"): FAOPolitEnt.COMOROS,
    FAOCountry("Congo", "46"): FAOPolitEnt.CONGO,
    FAOCountry("Cook Islands", "47"): FAOPolitEnt.COOK_ISLANDS,
    FAOCountry("Costa Rica", "48"): FAOPolitEnt.COSTA_RICA,
    FAOCountry("Cote d'Ivoire", "107"): FAOPolitEnt.COTE_DIVOIRE,
    FAOCountry("Croatia", "98"): FAOPolitEnt.CROATIA,
    FAOCountry("Cuba", "49"): FAOPolitEnt.CUBA,
    FAOCountry("Curacao", "279"): FAOPolitEnt.CURACAO,
    FAOCountry("Cyprus", "50"): FAOPolitEnt.CYPRUS,
    FAOCountry("Czechia", "167"): FAOPolitEnt.CZECHIA,
    FAOCountry("Czechoslovakia", "51"): FAOPolitEnt.CZECHOSLOVAKIA,
    FAOCountry("Democratic People's Republic of Korea", "116"): FAOPolitEnt.NORTH_KOREA,
    FAOCountry("Democratic Republic of the Congo", "250"): FAOPolitEnt.CONGO_DR,
    FAOCountry("Denmark", "54"): FAOPolitEnt.DENMARK,
    FAOCountry("Djibouti", "72"): FAOPolitEnt.DJIBOUTI,
    FAOCountry("Dominica", "55"): FAOPolitEnt.DOMINICA,
    FAOCountry("Dominican Republic", "56"): FAOPolitEnt.DOMINICAN_REPUBLIC,
    FAOCountry("Ecuador", "58"): FAOPolitEnt.ECUADOR,
    FAOCountry("Egypt", "59"): FAOPolitEnt.EGYPT,
    FAOCountry("El Salvador", "60"): FAOPolitEnt.EL_SALVADOR,
    FAOCountry("Equatorial Guinea", "61"): FAOPolitEnt.EQUATORIAL_GUINEA,
    FAOCountry("Eritrea", "178"): FAOPolitEnt.ERITREA,
    FAOCountry("Estonia", "63"): FAOPolitEnt.ESTONIA,
    FAOCountry("Ethiopia", "238"): FAOPolitEnt.ETHIOPIA,
    FAOCountry("Ethiopia PDR", "62"): FAOPolitEnt.ETHIOPIA_PDR,
    FAOCountry("Falkland Islands (Malvinas)", "65"): FAOPolitEnt.FALKLAND_ISLANDS,
    FAOCountry("Faroe Islands", "64"): FAOPolitEnt.FAROE_ISLANDS,
    FAOCountry("Fiji", "66"): FAOPolitEnt.FIJI,
    FAOCountry("Finland", "67"): FAOPolitEnt.FINLAND,
    FAOCountry("France", "68"): FAOPolitEnt.FRANCE,
    FAOCountry("French Guiana", "69"): FAOPolitEnt.FRENCH_GUIANA,
    FAOCountry("French Polynesia", "70"): FAOPolitEnt.FRENCH_POLYNESIA,
    FAOCountry("Gabon", "74"): FAOPolitEnt.GABON,
    FAOCountry("Gambia", "75"): FAOPolitEnt.GAMBIA,
    FAOCountry("Georgia", "73"): FAOPolitEnt.GEORGIA,
    FAOCountry("Germany", "79"): FAOPolitEnt.GERMANY,
    FAOCountry("Germany Fr", "78"): FAOPolitEnt.WEST_GERMANY,
    FAOCountry("Germany Nl", "77"): FAOPolitEnt.EAST_GERMANY,
    FAOCountry("Ghana", "81"): FAOPolitEnt.GHANA,
    FAOCountry("Gibraltar", "82"): FAOPolitEnt.GIBRALTAR,
    FAOCountry("Greece", "84"): FAOPolitEnt.GREECE,
    FAOCountry("Greenland", "85"): FAOPolitEnt.GREENLAND,
    FAOCountry("Grenada", "86"): FAOPolitEnt.GRENADA,
    FAOCountry("Guadeloupe", "87"): FAOPolitEnt.GUADELOUPE,
    FAOCountry("Guam", "88"): FAOPolitEnt.GUAM,
    FAOCountry("Guatemala", "89"): FAOPolitEnt.GUATEMALA,
    FAOCountry("Guinea", "90"): FAOPolitEnt.GUINEA,
    FAOCountry("Guinea-Bissau", "175"): FAOPolitEnt.GUINEA_BISSAU,
    FAOCountry("Guyana", "91"): FAOPolitEnt.GUYANA,
    FAOCountry("Haiti", "93"): FAOPolitEnt.HAITI,
    FAOCountry("Honduras", "95"): FAOPolitEnt.HONDURAS,
    FAOCountry("Hungary", "97"): FAOPolitEnt.HUNGARY,
    FAOCountry("India", "100"): FAOPolitEnt.INDIA,
    FAOCountry("Indonesia", "101"): FAOPolitEnt.INDONESIA,
    FAOCountry("Iran (Islamic Republic of)", "102"): FAOPolitEnt.IRAN,
    FAOCountry("Iraq", "103"): FAOPolitEnt.IRAQ,
    FAOCountry("Ireland", "104"): FAOPolitEnt.IRELAND,
    FAOCountry("Israel", "105"): FAOPolitEnt.ISRAEL,
    FAOCountry("Italy", "106"): FAOPolitEnt.ITALY,
    FAOCountry("Jamaica", "109"): FAOPolitEnt.JAMAICA,
    FAOCountry("Japan", "110"): FAOPolitEnt.JAPAN,
    FAOCountry("Jordan", "112"): FAOPolitEnt.JORDAN,
    FAOCountry("Kazakhstan", "108"): FAOPolitEnt.KAZAKHSTAN,
    FAOCountry("Kenya", "114"): FAOPolitEnt.KENYA,
    FAOCountry("Kosovo", "275"): FAOPolitEnt.KOSOVO,
    FAOCountry("Kuwait", "118"): FAOPolitEnt.KUWAIT,
    FAOCountry("Kyrgyzstan", "113"): FAOPolitEnt.KYRGYZSTAN,
    FAOCountry("Lao People's Democratic Republic", "120"): FAOPolitEnt.LAOS,
    FAOCountry("Latvia", "119"): FAOPolitEnt.LATVIA,
    FAOCountry("Lebanon", "121"): FAOPolitEnt.LEBANON,
    FAOCountry("Lesotho", "122"): FAOPolitEnt.LESOTHO,
    FAOCountry("Liberia", "123"): FAOPolitEnt.LIBERIA,
    FAOCountry("Libya", "124"): FAOPolitEnt.LIBYA,
    FAOCountry("Liechtenstein", "125"): FAOPolitEnt.LIECNTENSTEIN,
    FAOCountry("Lithuania", "126"): FAOPolitEnt.LITHUANIA,
    FAOCountry("Luxembourg", "256"): FAOPolitEnt.LUXEMBOURG,
    FAOCountry("Madagascar", "129"): FAOPolitEnt.MADAGASCAR,
    FAOCountry("Malawi", "130"): FAOPolitEnt.MALAWI,
    FAOCountry("Malaysia", "131"): FAOPolitEnt.MALAYSIA,
    FAOCountry("Mali", "133"): FAOPolitEnt.MALI,
    FAOCountry("Mauritania", "136"): FAOPolitEnt.MAURITANIA,
    FAOCountry("Mauritius", "137"): FAOPolitEnt.MAURITIUS,
    FAOCountry("Mexico", "138"): FAOPolitEnt.MEXICO,
    FAOCountry("Mongolia", "141"): FAOPolitEnt.MONGOLIA,
    FAOCountry("Montenegro", "273"): FAOPolitEnt.MONTENEGRO,
    FAOCountry("Morocco", "143"): FAOPolitEnt.MOROCCO,
    FAOCountry("Mozambique", "144"): FAOPolitEnt.MOZAMBIQUE,
    FAOCountry("Myanmar", "28"): FAOPolitEnt.MYANMAR,
    FAOCountry("Namibia", "147"): FAOPolitEnt.NAMIBIA,
    FAOCountry("Nepal", "149"): FAOPolitEnt.NEPAL,
    FAOCountry("Netherlands", "150"): FAOPolitEnt.NETHERLANDS,
    FAOCountry("New Zealand", "156"): FAOPolitEnt.NEW_ZEALAND,
    FAOCountry("Nicaragua", "157"): FAOPolitEnt.NICARAGUA,
    FAOCountry("Niger", "158"): FAOPolitEnt.NIGER,
    FAOCountry("Nigeria", "159"): FAOPolitEnt.NIGERIA,
    FAOCountry("Norway", "162"): FAOPolitEnt.NORWAY,
    FAOCountry("Oman", "221"): FAOPolitEnt.OMAN,
    FAOCountry("Pakistan", "165"): FAOPolitEnt.PAKISTAN,
    FAOCountry("Panama", "166"): FAOPolitEnt.PANAMA,
    FAOCountry("Papua New Guinea", "168"): FAOPolitEnt.PAPUA_NEW_GUINEA,
    FAOCountry("Paraguay", "169"): FAOPolitEnt.PARAGUAY,
    FAOCountry("Peru", "170"): FAOPolitEnt.PERU,
    FAOCountry("Philippines", "171"): FAOPolitEnt.PHILIPPINES,
    FAOCountry("Poland", "173"): FAOPolitEnt.POLAND,
    FAOCountry("Portugal", "174"): FAOPolitEnt.PORTUGAL,
    FAOCountry("Puerto Rico", "177"): FAOPolitEnt.PUERTO_RICO,
    FAOCountry("Qatar", "179"): FAOPolitEnt.QATAR,
    FAOCountry("Republic of Korea", "117"): FAOPolitEnt.SOUTH_KOREA,
    FAOCountry("Republic of Moldova", "146"): FAOPolitEnt.MOLDOVA,
    FAOCountry("Reunion", "182"): FAOPolitEnt.REUNION,
    FAOCountry("Romania", "183"): FAOPolitEnt.ROMANIA,
    FAOCountry("Russian Federation", "185"): FAOPolitEnt.RUSSIA,
    FAOCountry("Rwanda", "184"): FAOPolitEnt.RWANDA,
    FAOCountry("Saudi Arabia", "194"): FAOPolitEnt.SAUDI_ARABIA,
    FAOCountry("Senegal", "195"): FAOPolitEnt.SENEGAL,
    FAOCountry("Serbia", "272"): FAOPolitEnt.SERBIA,
    # We omit 286 Serbia (exc Kosovo) because it does not appear to have
    # an M49 country code.
    FAOCountry("Serbia and Montenegro", "186"): FAOPolitEnt.SERBIA_AND_MONTENEGRO,
    FAOCountry("Sierra Leone", "197"): FAOPolitEnt.SIERRA_LEONE,
    FAOCountry("Singapore", "200"): FAOPolitEnt.SINGAPORE,
    FAOCountry("Slovakia", "199"): FAOPolitEnt.SLOVAKIA,
    FAOCountry("Slovenia", "198"): FAOPolitEnt.SLOVENIA,
    FAOCountry("Solomon Islands", "25"): FAOPolitEnt.SOLOMON_ISLANDS,
    FAOCountry("Somalia", "201"): FAOPolitEnt.SOMALIA,
    FAOCountry("South Africa", "202"): FAOPolitEnt.SOUTH_AFRICA,
    FAOCountry("South Sudan", "277"): FAOPolitEnt.SOUTH_SUDAN,
    FAOCountry("Spain", "203"): FAOPolitEnt.SPAIN,
    FAOCountry("Sri Lanka", "38"): FAOPolitEnt.SRI_LANKA,
    FAOCountry("Sudan", "276"): FAOPolitEnt.SUDAN,
    FAOCountry("Sudan (former)", "206"): FAOPolitEnt.SUDAN_FORMER,
    FAOCountry("Suriname", "207"): FAOPolitEnt.SURINAME,
    FAOCountry("Swaziland", "209"): FAOPolitEnt.SWAZILAND,
    FAOCountry("Sweden", "210"): FAOPolitEnt.SWEDEN,
    FAOCountry("Switzerland", "211"): FAOPolitEnt.SWITZERLAND,
    FAOCountry("Syrian Arab Republic", "212"): FAOPolitEnt.SYRIA,
    FAOCountry("Tajikistan", "208"): FAOPolitEnt.TAJIKISTAN,
    FAOCountry("Thailand", "216"): FAOPolitEnt.THAILAND,
    FAOCountry("The former Yugoslav Republic of Macedonia", "154"): FAOPolitEnt.MACEDONIA,
    FAOCountry("Timor-Leste", "176"): FAOPolitEnt.TIMOR_LESTE,
    FAOCountry("Togo", "217"): FAOPolitEnt.TOGO,
    FAOCountry("Trinidad and Tobago", "220"): FAOPolitEnt.TRINIDAD_AND_TOBAGO,
    FAOCountry("Tunisia", "222"): FAOPolitEnt.TUNISIA,
    FAOCountry("Turkey", "223"): FAOPolitEnt.TURKEY,
    FAOCountry("Turkmenistan", "213"): FAOPolitEnt.TURKMENISTAN,
    FAOCountry("Uganda", "226"): FAOPolitEnt.UGANDA,
    FAOCountry("Ukraine", "230"): FAOPolitEnt.UKRAINE,
    FAOCountry("United Arab Emirates", "225"): FAOPolitEnt.UNITED_ARAB_EMIRATES,
    FAOCountry("United Kingdom", "229"): FAOPolitEnt.UNITED_KINGDOM,
    FAOCountry("United Republic of Tanzania", "215"): FAOPolitEnt.TANZANIA,
    FAOCountry("United States of America", "231"): FAOPolitEnt.USA,
    FAOCountry("Uruguay", "234"): FAOPolitEnt.URUGUAY,
    FAOCountry("USSR", "228"): FAOPolitEnt.USSR,
    FAOCountry("Uzbekistan", "235"): FAOPolitEnt.UZBEKISTAN,
    FAOCountry("Venezuela (Bolivarian Republic of)", "236"): FAOPolitEnt.VENEZUELA,
    FAOCountry("Viet Nam", "237"): FAOPolitEnt.VIETNAM,
    FAOCountry("Yemen", "249"): FAOPolitEnt.YEMEN,
    FAOCountry("Yemen Ar Rp", "246"): FAOPolitEnt.NORTH_YEMEN,
    FAOCountry("Yemen Dem", "247"): FAOPolitEnt.SOUTH_YEMEN,
    FAOCountry("Yugoslav SFR", "248"): FAOPolitEnt.YUGOSLAVIA,
    FAOCountry("Zambia", "251"): FAOPolitEnt.ZAMBIA,
    FAOCountry("Zimbabwe", "181"): FAOPolitEnt.ZIMBABWE
}
