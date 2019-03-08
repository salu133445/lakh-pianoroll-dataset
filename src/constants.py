"""This file defines the mapping between the labels and the codes."""
LABEL_NUM_MAP = {
    'Big_Band': 0,
    'Blues_Contemporary': 1,
    'Country_Traditional': 2,
    'Dance': 3,
    'Electronica': 4,
    'Experimental': 5,
    'Folk_International': 6,
    'Gospel': 7,
    'Grunge_Emo': 8,
    'Hip_Hop_Rap': 9,
    'Jazz_Classic': 10,
    'Metal_Alternative': 11,
    'Metal_Death': 12,
    'Metal_Heavy': 13,
    'Pop_Contemporary': 14,
    'Pop_Indie': 15,
    'Pop_Latin': 16,
    'Punk': 17,
    'Reggae': 18,
    'RnB_Soul': 19,
    'Rock_Alternative': 20,
    'Rock_College': 21,
    'Rock_Contemporary': 22,
    'Rock_Hard': 23,
    'Rock_Neo_Psychedelia': 24
}

NUM_LABEL_MAP = {
    0: 'Big_Band',
    1: 'Blues_Contemporary',
    2: 'Country_Traditional',
    3: 'Dance',
    4: 'Electronica',
    5: 'Experimental',
    6: 'Folk_International',
    7: 'Gospel',
    8: 'Grunge_Emo',
    9: 'Hip_Hop_Rap',
    10: 'Jazz_Classic',
    11: 'Metal_Alternative',
    12: 'Metal_Death',
    13: 'Metal_Heavy',
    14: 'Pop_Contemporary',
    15: 'Pop_Indie',
    16: 'Pop_Latin',
    17: 'Punk',
    18: 'Reggae',
    19: 'RnB_Soul',
    20: 'Rock_Alternative',
    21: 'Rock_College',
    22: 'Rock_Contemporary',
    23: 'Rock_Hard',
    24: 'Rock_Neo Psychedelia'
}

CLEANSED_LABELS = [2, 3, 11, 14, 15, 16, 20, 21, 22, 23]

CLEANSED_NUM_LABEL_MAP = {
    0: 'Country_Traditional',  # 2
    1: 'Dance',                # 3
    2: 'Metal_Alternative',    # 11
    3: 'Pop_Contemporary',     # 14
    4: 'Pop_Indie',            # 15
    5: 'Pop_Latin',            # 16
    6: 'Rock_Alternative',     # 20
    7: 'Rock_College',         # 21
    8: 'Rock_Contemporary',    # 22
    9: 'Rock_Hard'             # 23
}

CLEANSED_LABEL_NUM_MAP = {
    'Country_Traditional': 0,  # 2
    'Dance': 1,                # 3
    'Metal_Alternative': 2,    # 11
    'Pop_Contemporary': 3,     # 14
    'Pop_Indie': 4,            # 15
    'Pop_Latin': 5,            # 16
    'Rock_Alternative': 6,     # 20
    'Rock_College': 7,         # 21
    'Rock_Contemporary': 8,    # 22
    'Rock_Hard': 9             # 23
}
