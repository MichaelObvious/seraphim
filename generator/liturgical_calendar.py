from datetime import date, timedelta

EASTER_DATES = {
    2024: date(2024, 3, 31),
    2025: date(2025, 4, 20),
    2026: date(2026, 4, 5),
    2027: date(2027, 3, 28),
}

SUNDAYS_AND_FEAST_NT_READINGS = {'A': {'10TO': 'Rm 4, 18-25',
       '11TO': 'Rm 5, 6-11',
       '12TO': 'Rm 5, 12-15',
       '13TO': 'Rm 6, 3-4.8-11',
       '14TO': 'Rm 8, 9.11-13',
       '15TO': 'Rm 8, 18-23',
       '16TO': 'Rm 8, 26-27',
       '17TO': 'Rm 8, 28-30',
       '18TO': 'Rm 8, 35.37-39',
       '19TO': 'Rm 9, 1-5',
       '1AD': 'Rm 13, 11-14',
       '1Q': 'Rm 5, 12-19',
       '20TO': 'Rm 11, 13-15.29-32',
       '21TO': 'Rm 11, 33-36',
       '22TO': 'Rm 12, 1-2',
       '23TO': 'Rm 13, 8-10',
       '24TO': 'Rm 14, 7-9',
       '25TO': 'Fil 1, 20c-24.27a',
       '26TO': 'Fil 2, 1-11',
       '27TO': 'Fil 4, 6-9',
       '28TO': 'Fil 4, 12-14.19-20',
       '29TO': '1Ts 1, 1-5b',
       '2AD': 'Rm 15, 4-9',
       '2N': 'Ef 1, 3-6.15-18',
       '2P': '1Pt 1, 3-9',
       '2Q': '2Tm 1, 8b-10',
       '2TO': '1Cor 1, 1-3',
       '30TO': '1Ts 1, 5c-10',
       '31TO': '1Ts 2, 7b-9.13',
       '32TO': '1Ts 4, 13-18',
       '33TO': '1Ts 5, 1-6',
       '3AD': 'Gc 5, 7-10',
       '3P': '1Pt 1, 17-21',
       '3Q': 'Rm 5, 1-2.5-8',
       '3TO': '1Cor 1, 10-13.17',
       '4AD': 'Rm 1, 1-7',
       '4P': '1Pt 2, 20b-25',
       '4Q': 'Ef 5, 8-14',
       '4TO': '1Cor 1, 26-31',
       '5P': '1Pt 2, 4-9',
       'LZR': 'Rm 8, 8-11',
       '5TO': '1Cor 2, 1-5',
       '6P': '1Pt 3, 15-18',
       '6TO': '1Cor 2, 6-10',
       '7P': '1Pt 4, 13-16',
       '7TO': '1Cor 3, 16-23',
       '8TO': '1Cor 4, 1-5',
       '9TO': 'Rm 3, 21-25.28',
       'AD': 'Ef 1, 17-23',
       'AM': '1Cor 15, 20-27',
       'ANN': 'Eb 10, 4-10',
       'BD': 'At 10, 34-38',
       'CAND': 'Eb 2, 14-18',
       'CD': '1Cor 10, 16-17',
       'CR': '1Cor 15, 20-26.28',
       'E': 'Ef 3, 2-3a.5-6',
       'EC': 'Fil 2, 6-11',
       'GS': '1Cor 11, 23-26',
       'IC': 'Ef 1, 3-6.11-12',
       'MSMD': 'Gal 4, 4-7',
       'NIB': 'At 13, 22-26',
       'OS': '1Gv 3, 1-3',
       'PLM': 'Fil 2, 6-11',
       'PSQ': 'Col 3, 1-4',
       'PTK': '1Cor 12, 3b-7.12-13',
       'SCJ': '1Gv 4, 7-16',
       'SF': 'Col 3, 12-21',
       'SPP': '2Tm 4, 6-8.17-18',
       'ST': '2Cor 13, 11-13',
       'STJ': 'Rm 4, 13.16-18.22',
       'TSF': '2Pt 1, 16-19',
       'VS': 'Eb 4, 14-16; 5, 7-9',
       'XMAS': 'Eb 1, 1-6',
       'MC': '2Cor 5, 20-21; 6, 1-2',
       'NVM': 'Rm 8, 28-30'},
 'B': {'10TO': '2Cor 4, 13-5, 1',
       '11TO': '2Cor 5, 6-10',
       '12TO': '2Cor 5, 14-17',
       '13TO': '2Cor 8, 7.9.13-15',
       '14TO': '2Cor 12, 7-10',
       '15TO': 'Ef 1, 3-14',
       '16TO': 'Ef 2, 13-18',
       '17TO': 'Ef 4, 1-6',
       '18TO': 'Ef 4, 17.20-24',
       '19TO': 'Ef 4, 30-5, 2',
       '1AD': '1Cor 1, 3-9',
       '1Q': '1Pt 3, 18-22',
       '20TO': 'Ef 5, 15-20',
       '21TO': 'Ef 5, 21-32',
       '22TO': 'Gc 1, 17-18.21b-22.27',
       '23TO': 'Gc 2, 1-5',
       '24TO': 'Gc 2, 14-18',
       '25TO': 'Gc 3, 16-4, 3',
       '26TO': 'Gc 5, 1-6',
       '27TO': 'Eb 2, 9-11',
       '28TO': 'Eb 4, 12-13',
       '29TO': 'Eb 4, 14-16',
       '2AD': '2Pt 3, 8-14',
       '2N': 'Ef 1, 3-6.15-18',
       '2P': '1Gv 5, 1-6',
       '2Q': 'Rm 8, 31b-34',
       '2TO': '1Cor 6, 13c-15a.17-20',
       '30TO': 'Eb 5, 1-6',
       '31TO': 'Eb 7, 23-28',
       '32TO': 'Eb 9, 24-28',
       '33TO': 'Eb 10, 11-14.18',
       '3AD': '1Ts 5, 16-24',
       '3P': '1Gv 2, 1-5a',
       '3Q': '1Cor 1, 22-25',
       '3TO': '1Cor 7, 29-31',
       '4AD': 'Rm 16, 25-27',
       '4P': '1Gv 3, 1-2',
       '4Q': 'Ef 2, 4-10',
       '4TO': '1Cor 7, 32-35',
       '5P': '1Gv 3, 18-24',
       '5Q': 'Eb 5, 7-9',
       '5TO': '1Cor 9, 16-19.22-23',
       '6P': '1Gv 4, 7-10',
       '6TO': '1Cor 10, 31-11, 1',
       '7P': '1Gv 4, 11-16',
       '7TO': '2Cor 1, 18-22',
       '8TO': '2Cor 3, 1b-6',
       '9TO': '2Cor 4, 6-11',
       'AD': 'Ef 1, 17-23',
       'AM': '1Cor 15, 20-27',
       'ANN': 'Eb 10, 4-10',
       'BD': '1Gv 5, 1-9',
       'CAND': 'Eb 2, 14-18',
       'CD': 'Eb 9, 11-15',
       'CR': 'Ap 1, 5-8',
       'E': 'Ef 3, 2-3a.5-6',
       'EC': 'Fil 2, 6-11',
       'GS': '1Cor 11, 23-26',
       'IC': 'Ef 1, 3-6.11-12',
       'MSMD': 'Gal 4, 4-7',
       'NIB': 'At 13, 22-26',
       'OS': '1Gv 3, 1-3',
       'PENTECOOOOSTE': 'Gal 5, 16-25',
       'PLM': 'Fil 2, 6-11',
       'PSQ': 'Col 3, 1-4',
       'PTK': '1Cor 12, 3b-7.12-13',
       'SCJ': 'Ef 3, 8-12.14-19',
       'SF': 'Eb 11, 8.11-12.17-19',
       'SPP': '2Tm 4, 6-8.17-18',
       'ST': 'Rm 8, 14-17',
       'STJ': 'Rm 4, 13.16-18.22',
       'TSF': '2Pt 1, 16-19',
       'VS': 'Eb 4, 14-16; 5, 7-9',
       'XMAS': 'Eb 1, 1-6',
       'MC': '2Cor 5, 20-21; 6, 1-2',
       'NVM': 'Rm 8, 28-30'},
 'C': {'10TO': 'Gal 1, 11-19',
       '11TO': 'Gal 2, 16.19-21',
       '12TO': 'Gal 3, 26-29',
       '13TO': 'Gal 5, 1.13-18',
       '14TO': 'Gal 6, 14-18',
       '15TO': 'Col 1, 15-20',
       '16TO': 'Col 1, 24-28',
       '17TO': 'Col 2, 12-14',
       '18TO': 'Col 3, 1-5.9-11',
       '19TO': 'Eb 11, 1-2.8-19',
       '1AD': '1Ts 3, 12-4, 2',
       '1Q': 'Rm 10, 8-13',
       '20TO': 'Eb 12, 1-4',
       '21TO': 'Eb 12, 5-7.11-13',
       '22TO': 'Eb 12, 18-19.22-24a',
       '23TO': 'Fm 9-10.12-17',
       '24TO': '1Tm 1, 12-17',
       '25TO': '1Tm 2, 1-8',
       '26TO': '1Tm 6, 11-16',
       '27TO': '2Tm 1, 6-8.13-14',
       '28TO': '2Tm 2, 8-13',
       '29TO': '2Tm 3, 14-4, 2',
       '2AD': 'Fil 1, 4-6.8-11',
       '2N': 'Ef 1, 3-6.15-18',
       '2P': 'Ap 1, 9-11a.12-13.17-19',
       '2Q': 'Fil 3, 17-4, 1',
       '2TO': '1Cor 12, 4-11',
       '30TO': '2Tm 4, 6-8.16-18',
       '31TO': '2Ts 1, 11-2, 2',
       '32TO': '2Ts 2, 16-3, 5',
       '33TO': '2Ts 3, 7-12',
       '3AD': 'Fil 4, 4-7',
       '3P': 'Ap 5, 11-14',
       '3Q': '1Cor 10, 1-6.10-12',
       '3TO': '1Cor 12, 12-30',
       '4AD': 'Eb 10, 5-10',
       '4P': 'Ap 7, 9.14b-17',
       '4Q': '2Cor 5, 17-21',
       '4TO': '1Cor 12, 31-13, 13',
       '5P': 'Ap 21, 1-5a',
       '5Q': 'Fil 3, 8-14',
       '5TO': '1Cor 15, 1-11',
       '6P': 'Ap 21, 10-14.22-23',
       '6TO': '1Cor 15, 12.16-20',
       '7P': 'Ap 22, 12-14.16-17.20',
       '7TO': '1Cor 15, 45-49',
       '8TO': '1Cor 15, 54-58',
       '9TO': 'Gal 1, 1-2.6-10',
       'AD': 'Eb 9, 24-28; 10, 19-23',
       'AM': '1Cor 15, 20-27',
       'ANN': 'Eb 10, 4-10',
       'BD': 'Tt 2, 11-14; 3, 4-7',
       'CAND': 'Eb 2, 14-18',
       'CD': '1Cor 11, 23-26',
       'CR': 'Col 1, 12-20',
       'E': 'Ef 3, 2-3a.5-6',
       'EC': 'Fil 2, 6-11',
       'GS': '1Cor 11, 23-26',
       'IC': 'Ef 1, 3-6.11-12',
       'MSMD': 'Gal 4, 4-7',
       'NIB': 'At 13, 22-26',
       'OS': '1Gv 3, 1-3',
       'PLM': 'Fil 2, 6-11',
       'PSQ': 'Col 3, 1-4',
       'PTK': '1Cor 12, 3b-7.12-13',
       'SCJ': 'Rm 5, 5b-11',
       'SF': '1Gv 3, 1-2.21-24',
       'SPP': '2Tm 4, 6-8.17-18',
       'ST': 'Rm 5, 1-5',
       'STJ': 'Rm 4, 13.16-18.22',
       'TSF': '2Pt 1, 16-19',
       'VS': 'Eb 4, 14-16; 5, 7-9',
       'XMAS': 'Eb 1, 1-6',
       'MC': '2Cor 5, 20-21; 6, 1-2',
       'NVM': 'Rm 8, 28-30'}}

SUNDAYS_AND_FEAST_GOSPELS = {'A': 
    {'10TO': 'Mt 9, 9-13',
       '11TO': 'Mt 9, 36 - 10, 8',
       '12TO': 'Mt 10, 26-33',
       '13TO': 'Mt 10, 37-42',
       '14TO': 'Mt 11, 25-30',
       '15TO': 'Mt 13, 1-23',
       '16TO': 'Mt 13, 24-43',
       '17TO': 'Mt 13, 44-52',
       '18TO': 'Mt 14, 13-21',
       '19TO': 'Mt 14, 22-33',
       '1AD': 'Mt 24, 37-44',
       '1Q': 'Mt 4, 1-11',
       '20TO': 'Mt 15, 21-28',
       '21TO': 'Mt 16, 13-20',
       '22TO': 'Mt 16, 21-27',
       '23TO': 'Mt 18, 15-20',
       '24TO': 'Mt 18, 21-35',
       '25TO': 'Mt 20, 1-16a',
       '26TO': 'Mt 21, 28-32',
       '27TO': 'Mt 21, 33-43',
       '28TO': 'Mt 22, 1-14',
       '29TO': 'Mt 22, 15-21',
       '2AD': 'Mt 3, 1-12',
       '2N': 'Gv 1, 1-18',
       '2P': 'Gv 20, 19-31',
       '2Q': 'Mt 17, 1-9',
       '2TO': 'Gv 1, 29-34',
       '30TO': 'Mt 22, 34-40',
       '31TO': 'Mt 23, 1-12',
       '32TO': 'Mt 25, 1-13',
       '33TO': 'Mt 25, 14-30',
       '3AD': 'Mt 11, 2-11',
       '3P': 'Lc 24, 13-35',
       '3Q': 'Gv 4, 5-42',
       '3TO': 'Mt 4, 12-23',
       '4AD': 'Mt 1, 18-24',
       '4P': 'Gv 10, 1-10',
       '4Q': 'Gv 9, 1-41',
       '4TO': 'Mt 5, 1-12a',
       '5P': 'Gv 14, 1-12',
       '5Q': 'Rom 8, 8-11',
       '5TO': 'Mt 5, 13-16',
       '6P': 'Gv 14, 15-21',
       '6TO': 'Mt 5, 17-37',
       '7P': 'Gv 17, 1-11a',
       '7TO': 'Mt 5, 38-48',
       '8TO': 'Mt 6, 24-34',
       '9TO': 'Mt 7, 21-27',
       'AD': 'Mt 28, 16-20',
       'AM': 'Lc 1, 39-56',
       'ANN': 'Lc 1, 26-38',
       'BD': 'Mt 3, 13-17',
       'CAND': 'Lc 2, 22-40',
       'CD': 'Gv 6, 51-58',
       'CR': 'Mt 25, 31-46',
       'E': 'Mt 2, 1-12',
       'EC': 'Gv 3, 13-17',
       'GS': 'Gv 13, 1-15',
       'IC': 'Lc 1, 26-38',
       'MSMD': 'Lc 2, 16-21',
       'NIB': 'Lc 1, 57-66.80',
       'OS': 'Mt 5, 1-12a',
       'PLM': 'Mt 27, 11-54',
       'PSQ': 'Gv 20, 1-9',
       'PTK': 'Gv 20, 19-23',
       'SCJ': 'Mt 11, 25-30',
       'SF': 'Mt 2, 13-15.19-23',
       'SPP': 'Mt 16, 13-19',
       'ST': 'Gv 3, 16-18',
       'STJ': 'Mt 1, 16.18-21.24a',
       'TSF': 'Mt 17, 1-9',
       'VS': 'Gv 18, 1 - 19, 42',
       'XMAS': 'Gv 1, 1-18',
       'NVM': 'Mt 1, 1-16.18-23',
       'MC': 'Mt 6, 1-6.16-18',
       'LZR': 'Gv 11, 1-45'
    },
 'B': {'10TO': 'Mc 3, 20-35',
       '11TO': 'Mc 4, 26-34',
       '12TO': 'Mc 4, 35-41',
       '13TO': 'Mc 5, 21-43',
       '14TO': 'Mc 6, 1-6',
       '15TO': 'Mc 6, 7-13',
       '16TO': 'Mc 6, 30-34',
       '17TO': 'Gv 6, 1-15',
       '18TO': 'Gv 6, 24-35',
       '19TO': 'Gv 6, 41-51',
       '1AD': 'Mc 13, 33-37',
       '1Q': 'Mc 1, 12-15',
       '20TO': 'Gv 6, 51-58',
       '21TO': 'Gv 6, 60-69',
       '22TO': 'Mc 7, 1-8.14-15.21-23',
       '23TO': 'Mc 7, 31-37',
       '24TO': 'Mc 8, 27-35',
       '25TO': 'Mc 9, 30-37',
       '26TO': 'Mc 9, 38-43.45.47-48',
       '27TO': 'Mc 10, 2-16',
       '28TO': 'Mc 10, 17-30',
       '29TO': 'Mc 10, 35-45',
       '2AD': 'Mc 1, 1-8',
       '2N': 'Gv 1, 1-18',
       '2P': 'Gv 20, 19-31',
       '2Q': 'Mc 9, 2-10',
       '2TO': 'Gv 1, 35-42',
       '30TO': 'Mc 10, 46-52',
       '31TO': 'Mc 12, 28b-34',
       '32TO': 'Mc 12, 38-44',
       '33TO': 'Mc 13, 24-32',
       '3AD': 'Gv 1, 6-8.19-28',
       '3P': 'Lc 24, 35-48',
       '3Q': 'Gv 2, 13-25',
       '3TO': 'Mc 1, 14-20',
       '4AD': 'Lc 1, 26-38',
       '4P': 'Gv 10, 11-18',
       '4Q': 'Gv 3, 14-21',
       '4TO': 'Mc 1, 21-28',
       '5P': 'Gv 15, 1-8',
       '5Q': 'Gv 12, 20-33',
       '5TO': 'Mc 1, 29-39',
       '6P': 'Gv 15, 9-17',
       '6TO': 'Mc 1, 40-45',
       '7P': 'Gv 17, 11b-19',
       '7TO': 'Mc 2, 1-12',
       '8TO': 'Mc 2, 18-22',
       '9TO': 'Mc 2, 23 - 3, 6',
       'AD': 'Mc 16, 15-20',
       'AM': 'Lc 1, 39-56',
       'ANN': 'Lc 1, 26-38',
       'BD': 'Mc 1, 7-11',
       'CAND': 'Lc 2, 22-40',
       'CD': 'Mc 14, 12-16.22-26',
       'CR': 'Gv 18, 33b-37',
       'E': 'Mt 2, 1-12',
       'EC': 'Gv 3, 13-17',
       'GS': 'Gv 13, 1-15',
       'IC': 'Lc 1, 26-38',
       'MSMD': 'Lc 2, 16-21',
       'NIB': 'Lc 1, 57-66.80',
       'OS': 'Mt 5, 1-12a',
       'PLM': 'Mc 15, 1-39',
       'PSQ': 'Gv 20, 1-9',
       'PTK': 'Gv 15, 26-27; 16, 12-15',
       'SCJ': 'Gv 19, 31-37',
       'SF': 'Lc 2, 22-40',
       'SPP': 'Mt 16, 13-19',
       'ST': 'Mt 28, 16-20',
       'TSF': 'Mc 9, 2-10',
       'VS': 'Gv 18, 1 - 19, 42',
       'XMAS': 'Gv 1, 1-18',
       'NVM': 'Mt 1, 1-16.18-23',
       'MC': 'Mt 6, 1-6.16-18'},
 'C': {'10TO': 'Lc 7, 11-17',
       '11TO': 'Lc 7, 36 - 8, 3',
       '12TO': 'Lc 9, 18-24',
       '13TO': 'Lc 9, 51-62',
       '14TO': 'Lc 10, 1-12.17-20',
       '15TO': 'Lc 10, 25-37',
       '16TO': 'Lc 10, 38-42',
       '17TO': 'Lc 11, 1-13',
       '18TO': 'Lc 12, 13-21',
       '19TO': 'Lc 12, 32-48',
       '1AD': 'Lc 21, 25-28.34-36',
       '1Q': 'Lc 4, 1-13',
       '20TO': 'Lc 12, 49-53',
       '21TO': 'Lc 13, 22-30',
       '22TO': 'Lc 14, 1.7-14',
       '23TO': 'Lc 14, 25-33',
       '24TO': 'Lc 15, 1-32',
       '25TO': 'Lc 16, 1-13',
       '26TO': 'Lc 16, 19-31',
       '27TO': 'Lc 17, 5-10',
       '28TO': 'Lc 17, 11-19',
       '29TO': 'Lc 18, 1-8',
       '2AD': 'Lc 3, 1-6',
       '2N': 'Gv 1, 1-18',
       '2P': 'Gv 20, 19-31',
       '2Q': 'Lc 9, 28b-36',
       '2TO': 'Gv 2, 1-11',
       '30TO': 'Lc 18, 9-14',
       '31TO': 'Lc 19, 1-10',
       '32TO': 'Lc 20, 27-38',
       '33TO': 'Lc 21, 5-19',
       '3AD': 'Lc 3, 10-18',
       '3P': 'Gv 21, 1-19',
       '3Q': 'Lc 13, 1-9',
       '3TO': 'Lc 1, 1-4; 4, 14-21',
       '4AD': 'Lc 1, 39-45',
       '4P': 'Gv 10, 27-30',
       '4Q': 'Lc 15, 1-3.11-32',
       '4TO': 'Lc 4, 21-30',
       '5P': 'Gv 13, 31-33a.34-35',
       '5Q': 'Gv 8, 1-11',
       '5TO': 'Lc 5, 1-11',
       '6P': 'Gv 14, 23-29',
       '6TO': 'Lc 6, 17.20-26',
       '7P': 'Gv 17, 20-26',
       '7TO': 'Lc 6, 27-38',
       '8TO': 'Lc 6, 39-45',
       '9TO': 'Lc 7, 1-10',
       'AD': 'Lc 24, 46-53',
       'AM': 'Lc 1, 39-56',
       'ANN': 'Lc 1, 26-38',
       'BD': 'Lc 3, 15-16.21-22',
       'CAND': 'Lc 2, 22-40',
       'CD': 'Lc 9, 11b-17',
       'CR': 'Lc 23, 35-43',
       'E': 'Mt 2, 1-12',
       'EC': 'Gv 3, 13-17',
       'GS': 'Gv 13, 1-15',
       'IC': 'Lc 1, 26-38',
       'MSMD': 'Lc 2, 16-21',
       'NIB': 'Lc 1, 57-66.80',
       'OS': 'Mt 5, 1-12a',
       'PLM': 'Lc 23, 1-49',
       'PSQ': 'Gv 20, 1-9',
       'PTK': 'Gv 14, 15-16.23b-26',
       'SCJ': 'Lc 15, 3-7',
       'SF': 'Lc 2, 41-52',
       'SPP': 'Mt 16, 13-19',
       'ST': 'Gv 16, 12-15',
       'STJ': 'Lc 2, 41-51a',
       'TSF': 'Lc 9, 28b-36',
       'VS': 'Gv 18, 1 - 19, 42',
       'XMAS': 'Gv 1, 1-18',
       'NVM': 'Mt 1, 1-16.18-23',
       'MC': 'Mt 6, 1-6.16-18'}
}

FEAST_NAMES = {
    'XMAS': 'Natale del Signore',
    'MSMD': 'Maria Santissima Madre di Dio',
    'E': 'Epifania del Signore',
    'CAND': 'Prensentazione del Signore al Tempio',
    'ANN': 'Annunciazione del Signore',
    'STJ': 'San Giuseppe',
    'TSF': 'Trasfigurazione del Signore',
    'PLM': 'Palme e Passione del Signore',
    'LZR': 'V Quaresima – Lazzaro',
    'PSQ': 'Pasqua – Resurrezione del Signore',
    'VS': 'Venerdì Santo – Passione del Signore',
    'GS': 'Giovedì Santo – Cena del Signore',
    'AD': 'Ascensione del Signore',
    'AM': 'Assunzione della Beata Vergine Maria',
    'PTK': 'Pentecoste',
    'OS': 'Tutti i Santi',
    'IC': 'Immacolata Concezione della Beata Vergine Maria',
    'SPP': 'Santi Pietro e Paolo, Apostoli',
    'CD': 'Santissimo Corpo e Sangue del Signore',
    'ST': 'Santissima Trinità',
    'EC': 'Esaltazione della Santa Croce',
    'SCJ': 'Sacratissimo Cuore di Gesù',
    'CR': 'XXXIV Ordinario – Nostro Signore Gesù Cristo Re dell\'Universo',
    'NIB': 'Natività di San Giovanni Battista',
    'MC': 'Mercoledì delle Ceneri',
    'NVM': 'Natività della Beata Vergine Maria',
    'SF': 'Santa Famiglia di Gesù, Maria e Giuseppe',
}


def roman(num):
    vals = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    res = ""
    for v, s in vals:
        while num >= v:
            res += s
            num -= v
    return res

def christmas(year: int) -> date:
    return date(year, 12, 25)

def advent_start(year: int) -> date:
    xmas = christmas(year)
    return xmas - timedelta(3*7 + xmas.isoweekday())

def liturgical_year(d: date) -> str:
    return "CAB"[d.year % 3 + (1 if d >= advent_start(d.year) else 0)]

def is_advent(d: date) -> bool:
    return advent_start(d.year) <= d < christmas(d.year)

def is_lent(d: date) -> bool:
    return lent_start(d.year) <= d < EASTER_DATES[d.year] - timedelta(3)

def is_holy_week(d: date) -> bool:
    return EASTER_DATES[d.year] - timedelta(7) <= d <= EASTER_DATES[d.year]

def is_eastertide(d: date) -> bool:
    return EASTER_DATES[d.year] <= d <= EASTER_DATES[d.year] + timedelta(49)

def lent_start(year: int) -> date:
    return EASTER_DATES[year] - timedelta(46)

def easter_time_end(year: int) -> date:
    return EASTER_DATES[year] + timedelta(49)

def christmastide_end(christmas_year: int) -> date:
    d = date(christmas_year, 1, 6)
    d += timedelta(7 - d.isoweekday())
    return d

def is_christmastide(d: date) -> bool:
    if d.month > 1 and d.month < 12:
        return False
    if d.month == 12:
        return christmas(d.year) <= d
    elif d.month == 1:
        return d <= christmastide_end(d.year)
    else:
        assert False, "unreacheable"
        
def is_christmas_octave(d: date) -> bool:
    christmas_date = christmas(d.year)
    return christmas_date <= d <= christmas_date + timedelta(7)

def is_easter_octave(d: date) -> bool:
    easter_date = EASTER_DATES[d.year]
    return easter_date <= d <= easter_date + timedelta(7)

def is_strong_time(d: date):
    return (is_advent(d) or is_christmastide(d) or is_lent(d) or is_holy_week(d) or is_eastertide(d))

def ascension(year: int):
    return EASTER_DATES[year] + timedelta(39)

def pentecost(year: int):
    return EASTER_DATES[year] + timedelta(7*7)

def holy_trinity_sunday(year: int):
    return EASTER_DATES[year] + timedelta(7*7+7)

class LiturgicalCalendar:
    def __init__(self, year: int = date.today().year) -> None:
        self.year = year
        self.feast_dates: list[tuple[date, bool, str]] = self.populate_feast_dates()
        self.sundays_and_feasts: list[tuple[date, str]] = self.populate_sundays_and_feast_dates()
        self.sundays_and_feasts_names: dict[date, str] = self.populate_sundays_and_feasts_names()
    
    def populate_feast_dates(self):
        XMAS = christmas(self.year)
        dates = [
            (XMAS, True, "XMAS"),
            ((date(self.year, 12, 30) if XMAS.isoweekday() == 7 else XMAS + timedelta(7-XMAS.isoweekday())), False, "SF"),
            (date(self.year, 1, 1), False, "MSMD"),
            (date(self.year, 1, 6), False, "E"),
            (date(self.year, 2, 2), False, "CAND"),
            (date(self.year, 3, 19), True, "STJ"),
            (date(self.year, 3, 25), True, "ANN"),
            (lent_start(self.year), False, "MC"),
            (EASTER_DATES[self.year] - timedelta(7), False, "PLM"),
            (EASTER_DATES[self.year] -  timedelta(3), False, "GS"),
            (EASTER_DATES[self.year] -  timedelta(2), False, "VS"),
            (EASTER_DATES[self.year], False, "PSQ"),
            (ascension(self.year), False, "AD"),
            (pentecost(self.year), False, "PTK"),
            (holy_trinity_sunday(self.year), False, "ST"),
            (EASTER_DATES[self.year] + timedelta(7*7+7+4), False, "CD"),
            (EASTER_DATES[self.year] + timedelta(7*7+7*2+5), False, "SCJ"),
            (date(self.year, 6, 29), False, "SPP"),
            (date(self.year, 8, 6), False, "TSF"),
            (date(self.year, 8, 15), False, "AM"),
            (date(self.year, 9, 8), False, "NVM"),
            (date(self.year, 9, 14), False, "EC"),
            (date(self.year, 11, 1), False, "OS"),
            (date(self.year, 12, 8), True, "IC"),
            (date(self.year, 6, 24), False, "NIB"),
            (advent_start(self.year)-timedelta(7), True, "CR"),
        ]
        if liturgical_year(EASTER_DATES[self.year] - timedelta(14)) == 'A':
            dates.append((EASTER_DATES[self.year] - timedelta(14), False, "LZR"))
        for i in range(len(dates)):
            (d, need_to_move, name) = dates[i]
            if need_to_move and is_strong_time(d) and d.isoweekday() == 7:
                if name == 'STJ':
                    if is_holy_week(d):
                        dates[i] = (dates[i][0] - timedelta(1), dates[i][1], dates [i][2])
                    else:
                        dates[i] = (dates[i][0] + timedelta(1), dates[i][1], dates [i][2])
                elif name == 'ANN':
                    if is_holy_week(d):
                        dates[i] = (EASTER_DATES[self.year] + timedelta(8), dates[i][1], dates [i][2])
                    else:
                        dates[i] = (dates[i][0] + timedelta(1), dates[i][1], dates [i][2])
                else:
                    dates[i] = (dates[i][0] + timedelta(1), dates[i][1], dates [i][2])

        # assert (EASTER_DATES[self.year] + timedelta(39)).weekday() == 3
        return dates

    def populate_sundays_and_feast_dates(self) -> list[tuple[date, str]]:
        inverted_dates_dict = dict(map(lambda x: (x[2], x[0]), self.feast_dates))
        dates_dict = dict(map(lambda x: (x[0], x[2]), self.feast_dates))
        
        current = date(self.year, 1, 1)
        current += timedelta(7-current.isoweekday())
        assert current.isoweekday() == 7
        if date(self.year, 1, 2) <= current <= date(self.year, 1, 5):
            assert current not in dates_dict
            dates_dict[current] = '2N'
            current += timedelta(7)
        dates_dict[current] = 'BD'
        
        if True: # Ordinary time
            current += timedelta(7)
            ord_count = 2
            while current < lent_start(self.year):
                if current not in dates_dict:
                    dates_dict[current] = f'{ord_count}TO'
                ord_count += 1
                current += timedelta(7)
        if True: # Lent
            current -= timedelta(4)
            # assert current not in dates_dict
            # dates_dict[current] = 'Mercoledì delle Ceneri'
            current += timedelta(4)
            assert current not in dates_dict
            dates_dict[current] = '1Q'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = '2Q'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = '3Q'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = '4Q'
            current += timedelta(7)
            if current not in dates_dict:
                dates_dict[current] = '5Q' # Lazzaro l'anno A
            current += timedelta(7)
            current += timedelta(7)
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = '2P'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = '3P'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = '4P'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = '5P'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = '6P'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = '7P'
            current += timedelta(7)


        if True: # Ordinary time
            current = advent_start(self.year) - timedelta(7)
            ord_count = 34
            while current > inverted_dates_dict['CD']:
                if current not in dates_dict:
                    dates_dict[current] = f'{ord_count}TO'
                ord_count -= 1
                current -= timedelta(7)
        if True: # Advent
            current = advent_start(self.year)
            assert current not in dates_dict
            dates_dict[current] = '1AD'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = '2AD'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = '3AD'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = '4AD'
        return list(dates_dict.items())
    
    def populate_sundays_and_feasts_names(self) -> dict[date, str]:
        inverted_dates_dict = dict(map(lambda x: (x[2], x[0]), self.feast_dates))
        dates_dict = dict(map(lambda x: (x[0], FEAST_NAMES[x[2]]), self.feast_dates))

        current = date(self.year, 1, 1)
        current += timedelta(7-current.isoweekday())
        assert current.isoweekday() == 7
        if date(self.year, 1, 2) <= current <= date(self.year, 1, 5):
            dates_dict[current] = 'II dopo Natale'
            current += timedelta(7)
        assert current not in dates_dict

        dates_dict[current] = 'Battesimo del Signore'
        
        if True: # Ordinary time
            current += timedelta(7)
            ord_count = 2
            while current < lent_start(self.year):
                if current not in dates_dict:
                    dates_dict[current] = f'{roman(ord_count)} Ordinario'
                ord_count += 1
                current += timedelta(7)
        if True: # Lent
            current -= timedelta(4)
            # assert current not in dates_dict
            # dates_dict[current] = 'Mercoledì delle Ceneri'
            current += timedelta(4)
            assert current not in dates_dict
            dates_dict[current] = 'I Quaresima'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = 'II Quaresima'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = 'III Quaresima'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = 'IV Quaresima – Laetare'
            current += timedelta(7)
            if current not in dates_dict:
                dates_dict[current] = 'V Quaresima' # Lazzaro l'anno A
            current += timedelta(7)
            assert current in dates_dict
            current += timedelta(7)
            assert current in dates_dict
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = 'II Pasqua – In albis'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = 'III Pasqua'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = 'IV Pasqua – Buon Pastore'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = 'V Pasqua'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = 'VI Pasqua'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = 'VII Pasqua'
            current += timedelta(7)
            assert current in dates_dict


        if True: # Ordinary time
            current = advent_start(self.year) - timedelta(7)
            ord_count = 34
            while current > inverted_dates_dict['CD']:
                if current not in dates_dict:
                    dates_dict[current] = f'{roman(ord_count)} Ordinario'
                ord_count -= 1
                current -= timedelta(7)
        if True: # Advent
            current = advent_start(self.year)
            assert current not in dates_dict
            dates_dict[current] = 'I Avvento'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = 'II Avvento'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = 'III Avvento – Gaudete'
            current += timedelta(7)
            assert current not in dates_dict
            dates_dict[current] = 'IV Avvento'
            
        return dates_dict

    
    def get_day_name(self, d: date) -> str:
        f_n_s_names = self.sundays_and_feasts_names
        if d in f_n_s_names:
            return f_n_s_names[d]
        
        # Italian weekday names
        weekday_names = {
            1: "Lunedì",
            2: "Martedì", 
            3: "Mercoledì",
            4: "Giovedì",
            5: "Venerdì",
            6: "Sabato",
            7: "Domenica"
        }
        
        weekday = d.isoweekday()
        weekday_name = weekday_names[weekday]
        
        # Handle Octaves first (special cases)
        if is_christmastide(d) and christmas(d.year) <= d <= christmas(d.year) + timedelta(7):
            return f"{weekday_name} nell'Ottava di Natale"
        
        if is_eastertide(d) and EASTER_DATES[d.year] <= d <= EASTER_DATES[d.year] + timedelta(7):
            return f"{weekday_name} nell'Ottava di Pasqua"
        
        # Handle different liturgical seasons
        if is_advent(d):
            return f"{weekday_name} nel Tempo di Avvento"
        if is_lent(d):
            if is_holy_week(d) and EASTER_DATES[d.year] != d:
                return f"{weekday_name} Santo"
            else:
                return f"{weekday_name} nel Tempo di Quaresima"
        if is_eastertide(d):
            return f"{weekday_name} nel Tempo di Pasqua"
        if is_christmastide(d):
            return f"{weekday_name} nel Tempo di Natale"
        # else:
        # Ordinary Time
        return f"{weekday_name} nel Tempo Ordinario"

    
    def get_feast_code(self, d: date) -> str:
        # Implement based on your feast_dates function
        # Returns the feast code if d is a feast day, otherwise empty string
        for feast_date, _, code in self.feast_dates:
            if feast_date == d:
                return code
        return ""
    
    def get_liturgical_color(self, d: date) -> str:
        # Fixed feast dates that determine color
        feast_colors = {
            # Red feasts (martyrs, Holy Spirit, Passion)
            'PTK': '#ff0000',    # Pentecost
            'SPP': '#ff0000',    # Saints Peter and Paul
            'PLM': '#ff0000',    # Palm Sunday
            'VS': '#ff0000',     # Good Friday
            'NIB': '#ff0000',    # Nativity of John the Baptist (martyr)
            'EC': '#ff0000',     # Exaltation of the Holy Cross
            
            # White feasts (Joy, Resurrection, Marian feasts)
            'XMAS': '#ffd200', # Christmas
            'PSQ': '#ffd200',  # Easter
            'AD': '#ffd200',   # Ascension
            'ST': '#ffd200',   # Trinity Sunday
            'CD': '#ffd200',   # Corpus Christi
            'MSMD': '#ffd200', # Mary Mother of God
            'AM': '#ffd200',   # Assumption
            'IC': '#ffd200',   # Immaculate Conception
            'TSF': '#ffd200',  # Transfiguration
            'CR': '#ffd200',   # Christ the King
            'ANN': '#ffd200',  # Annunciation
            'STJ': '#ffd200',  # St. Joseph
        }
        
        # Get Easter date for the year (you'll need to implement this or use your existing calculation)
        easter_date = EASTER_DATES[d.year]  # You have this in your EASTER_DATES
        
        # Check liturgical seasons
        if is_advent(d):
            return '#800080'
        
        if is_lent(d):
            return '#800080'
        
        if is_easter_octave(d) or is_christmas_octave(d):
            return '#ffd200'
        
        if is_eastertide(d):
            return '#ffd200'
        
        if is_christmastide(d):
            return '#ffd200'
        
        # Check if it's a feast day with specific color
        feast_code = self.get_feast_code(d)  # You'll need to implement this based on your feast_dates function
        if feast_code in feast_colors:
            return feast_colors[feast_code]
        
        if d.isoweekday() == 5:
            return '#800080'
        
        if d.isoweekday() == 7:
            return '#ffd200'
        
        # Default for Ordinary Time
        return '#ff0000'


class LiturgicalCalendars:
    def __init__(self):
        self.calendars: dict[int,LiturgicalCalendar] = {}
    
    def __getitem__(self, key: int):
        if not (key in self.calendars):
            self.calendars[key] = LiturgicalCalendar(key)
        return self.calendars[key]

    def is_feast(self, d: date) -> bool:
        return (d in dict(self[d.year].sundays_and_feasts).keys())
    
    def get_day_name(self, d: date) -> str:
        return self[d.year].get_day_name(d)
    
    
    def get_day_color(self, d: date) -> str:
        return self[d.year].get_liturgical_color(d)


def is_marian_feast(lc: LiturgicalCalendar, d: date) -> bool:
    return dict(lc.sundays_and_feasts)[d] in ['ANN', 'AM', 'MSMD', 'IC', 'NVM']