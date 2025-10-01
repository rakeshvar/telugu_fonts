"""
File contains the properties of available Telugu Fonts as a dictionary.
This is the product of the repository github.com/rakeshvar/telugu_fonts
The fonts here can be explored in detail in that repository.
Fields:
    Font Name
    Size of the font to get target x-height of 40 px
    Style of gho (Kannada/Telugu)
    Style of repha (Bottom/Left/Right) క్రోత్రక్రైత్రైత్త్రక్క్రక్క్రై
    Has Special form for ppu
    Required Letter Spacing (Single/Double)
    Abbreviation
    Has Bold
"""

SIZE, GHO, REPHA, PPU, SPACING, BOLD, ABBR, = range(7)
font_properties = {
'Akshar Unicode':           [40, 'K', 'BB', 0, 1, 1, 'Akshar',  ],
'Annamayya':                [40, 'K', 'LBR', 1, 1, 1, 'Annamaya',],
'Chathura':                 [56, 'T', 'LBR', 0, 1, 0, 'Chathura',],
'Dhurjati':                 [42, 'K', 'BB', 1, 1, 1, 'Dhurjati',],
'e-Telugu OT':              [48, 'T', 'BR', 1, 1, 1, 'e-Telugu',  ],
'Gautami':                  [42, 'K', 'BB', 0, 1, 1, 'Gautami', ],
'Gidugu':                   [54, 'K', 'BR', 1, 1, 1, 'Gidugu',  ],
'GIST-TLOTAmma':            [28, 'K', 'LR', 1, 1, 1, 'Amma',    ],
'GIST-TLOTAmruta':          [28, 'K', 'LR', 1, 1, 0, 'Amruta',  ],
'GIST-TLOTAtreya':          [28, 'K', 'LR', 1, 1, 1, 'Atreya',  ],
'GIST-TLOTChandana':        [28, 'K', 'LR', 1, 1, 0, 'Chandana',],
'GIST-TLOTDeva':            [28, 'K', 'LR', 1, 1, 0, 'Deva',    ],
'GIST-TLOTDraupadi':        [28, 'K', 'LR', 1, 1, 1, 'Draupadi',],
'GIST-TLOTGolkonda':        [28, 'K', 'LR', 1, 1, 0, 'Golkonda',],
'GIST-TLOTKrishna':         [28, 'K', 'LR', 1, 1, 1, 'Krishna', ],
'GIST-TLOTManu':            [28, 'K', 'LR', 1, 1, 1, 'Manu',    ],
'GIST-TLOTMenaka':          [30, 'K', 'LR', 1, 1, 1, 'Menaka',  ],
'GIST-TLOTPavani':          [28, 'K', 'LR', 1, 1, 0, 'Pavani',  ],
'GIST-TLOTPriya':           [22, 'K', 'LR', 1, 1, 0, 'Priya',   ],      # XHt reduced cuz Going Too Wide
# 'GIST-TLOTRajan':           [28, 'K', 'LR', 1, 1, 0, 'Rajan',   ],      # Border Font
'GIST-TLOTRajani':          [30, 'K', 'LR', 1, 1, 0, 'Rajani',  ],
'GIST-TLOTSanjana':         [28, 'K', 'LR', 1, 1, 0, 'Sanjana', ],
'GIST-TLOTSitara':          [28, 'K', 'LR', 1, 1, 0, 'Sitara',  ],
'GIST-TLOTSwami':           [28, 'K', 'LR', 1, 1, 0, 'Swami',   ],
'GIST-TLOTVennela':         [28, 'K', 'LR', 1, 1, 1, 'Vennela', ],
'Gurajada':                 [54, 'K', 'BR', 1, 1, 1, 'Gurajada',],
'JIMS':                     [54, 'T', 'LBR', 1, 1, 1, 'JIMS',      ],
'Kanaka Durga':             [52, 'K', 'LB', 1, 1, 1, 'Kanaka',    ],
'LakkiReddy':               [40, 'K', 'BB', 0, 1, 1, 'LakkiReddy',],
'Lohit Telugu':             [36, 'K', 'BB', 0, 1, 1, 'Lohit',   ],
'Mallanna':                 [40, 'T', 'BB', 1, 1, 1, 'Mallanna',],
'Mandali':                  [36, 'T', 'LB', 1, 1, 1, 'Mandali', ],
# 'Nandakam':                 [40, 'T', 'BB', 1, 1, 1, 'Nandakam',  ],   # Border Font
'Nandini3':                 [36, 'K', 'LL', 0, 1, 1, 'Nandini3',  ],
'NATS':                     [48, 'K', 'BR', 1, 1, 1, 'NATS',    ],
'Nirmala UI':               [36, 'K', 'LL', 0, 1, 1, 'Nirmala',   ],
'Noto Sans Telugu':         [40, 'K', 'BR', 0, 1, 1, 'Noto',    ],
'NTR':                      [42, 'K', 'BB', 1, 1, 1, 'NTR',     ],
'Peddana':                  [40, 'K', 'BR', 0, 1, 1, 'Peddana', ],
'Ponnala':                  [40, 'K', 'BB', 0, 1, 1, 'Ponnala', ],
'Pothana2000':              [40, 'K', 'BR', 1, 1, 1, 'Pothana', ],
'Potti Sreeramulu':         [48, 'K', 'BB', 1, 1, 1, 'Potti',     ],
'Purushothamaa':            [48, 'T', 'LB', 1, 1, 1, 'Purushothamaa',  ],
'Ramabhadra':               [48, 'T', 'BB', 0, 1, 1, 'Ramabhadra',],
'RamaneeyaWin':             [40, 'K', 'BB', 0, 1, 1, 'Ramaneeya',   ],
'Ramaraja':                 [42, 'K', 'BB', 0, 1, 1, 'Ramaraja',    ],
'RaviPrakash':              [48, 'K', 'BB', 0, 1, 1, 'RaviPrakash', ],
'Sree Krushnadevaraya':     [48, 'T', 'BB', 0, 1, 1, 'Krushnadeva', ],
'Subhadra':                 [36, 'T', 'BB', 0, 1, 1, 'Subhadra',    ],
'Suguna':                   [48, 'T', 'BR', 1, 2, 1, 'Suguna',  ],
'Suranna':                  [40, 'T', 'LBR', 1, 1, 1, 'Suranna', ],
'SuraVara_Samhita':         [42, 'K', 'BB', 0, 1, 1, 'Samhita', ],
'SURAVARA_Swarna':          [42, 'K', 'BB', 0, 1, 1, 'Swarna',  ],
'Suravaram':                [48, 'K', 'BR', 1, 1, 1, 'Suravaram',],
'Syamala Ramana':           [48, 'K', 'LB', 1, 1, 1, 'Syamala', ],
'TenaliRamakrishna':        [48, 'K', 'BB', 0, 1, 1, 'Tenali',  ],
'Timmana':                  [48, 'K', 'BB', 0, 1, 0, 'Timmana', ],
'Vajram':                   [44, 'K', 'BB', 0, 1, 1, 'Vajram',  ],
'Vani':                     [36, 'K', 'BR', 0, 1, 1, 'Vani',    ],
'Vemana2000':               [36, 'K', 'BR', 1, 1, 1, 'Vemana',  ],
}

font_properties_list = list(font_properties.items())

def random_font():
    import random
    font, properties = random.choice(font_properties_list)
    style = random.randrange(4)
    return font, properties[SIZE], style
