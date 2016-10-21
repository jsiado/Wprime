# This file was automatically created by FeynRules 2.0.2
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (November 20, 2012)
# Date: Tue 21 Oct 2014 10:51:45



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

xi = Parameter(name = 'xi',
               nature = 'external',
               type = 'real',
               value = 0.1,
               texname = '\\xi',
               lhablock = 'FRBlock',
               lhacode = [ 1 ])

grhopWZ = Parameter(name = 'grhopWZ',
                    nature = 'external',
                    type = 'real',
                    value = -0.0051,
                    texname = '\\text{grhopWZ}',
                    lhablock = 'FRBlock',
                    lhacode = [ 2 ])

grhopWh = Parameter(name = 'grhopWh',
                    nature = 'external',
                    type = 'real',
                    value = 140,
                    texname = '\\text{grhopWh}',
                    lhablock = 'FRBlock',
                    lhacode = [ 3 ])

grhopud = Parameter(name = 'grhopud',
                    nature = 'external',
                    type = 'real',
                    value = -0.22,
                    texname = '\\text{grhopud}',
                    lhablock = 'FRBlock',
                    lhacode = [ 4 ])

grhoptb = Parameter(name = 'grhoptb',
                    nature = 'external',
                    type = 'real',
                    value = 0.1,
                    texname = '\\text{grhoptb}',
                    lhablock = 'FRBlock',
                    lhacode = [ 5 ])

grhopT23LbL = Parameter(name = 'grhopT23LbL',
                        nature = 'external',
                        type = 'real',
                        value = 0.1,
                        texname = '\\text{grhopT23LbL}',
                        lhablock = 'FRBlock',
                        lhacode = [ 6 ])

grhopX23LbL = Parameter(name = 'grhopX23LbL',
                        nature = 'external',
                        type = 'real',
                        value = 0.1,
                        texname = '\\text{grhopX23LbL}',
                        lhablock = 'FRBlock',
                        lhacode = [ 7 ])

grhopX53LX23L = Parameter(name = 'grhopX53LX23L',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grhopX53LX23L}',
                          lhablock = 'FRBlock',
                          lhacode = [ 8 ])

grhopX53RX23R = Parameter(name = 'grhopX53RX23R',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grhopX53RX23R}',
                          lhablock = 'FRBlock',
                          lhacode = [ 9 ])

grhopX53LtL = Parameter(name = 'grhopX53LtL',
                        nature = 'external',
                        type = 'real',
                        value = 0.1,
                        texname = '\\text{grhopX53LtL}',
                        lhablock = 'FRBlock',
                        lhacode = [ 10 ])

grhopX53RtR = Parameter(name = 'grhopX53RtR',
                        nature = 'external',
                        type = 'real',
                        value = 0.1,
                        texname = '\\text{grhopX53RtR}',
                        lhablock = 'FRBlock',
                        lhacode = [ 11 ])

grhopX53LT23L = Parameter(name = 'grhopX53LT23L',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grhopX53LT23L}',
                          lhablock = 'FRBlock',
                          lhacode = [ 12 ])

grhopX53RT23R = Parameter(name = 'grhopX53RT23R',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grhopX53RT23R}',
                          lhablock = 'FRBlock',
                          lhacode = [ 13 ])

grhopT23LB13L = Parameter(name = 'grhopT23LB13L',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grhopT23LB13L}',
                          lhablock = 'FRBlock',
                          lhacode = [ 14 ])

grhopT23RB13R = Parameter(name = 'grhopT23RB13R',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grhopT23RB13R}',
                          lhablock = 'FRBlock',
                          lhacode = [ 15 ])

grhoptLB13L = Parameter(name = 'grhoptLB13L',
                        nature = 'external',
                        type = 'real',
                        value = 0.1,
                        texname = '\\text{grhoptLB13L}',
                        lhablock = 'FRBlock',
                        lhacode = [ 16 ])

grhoptRB13R = Parameter(name = 'grhoptRB13R',
                        nature = 'external',
                        type = 'real',
                        value = 0.1,
                        texname = '\\text{grhoptRB13R}',
                        lhablock = 'FRBlock',
                        lhacode = [ 17 ])

grhopX23LB13L = Parameter(name = 'grhopX23LB13L',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grhopX23LB13L}',
                          lhablock = 'FRBlock',
                          lhacode = [ 18 ])

grhopX23RB13R = Parameter(name = 'grhopX23RB13R',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grhopX23RB13R}',
                          lhablock = 'FRBlock',
                          lhacode = [ 19 ])

grho0WW = Parameter(name = 'grho0WW',
                    nature = 'external',
                    type = 'real',
                    value = 0.0044,
                    texname = '\\text{grho0WW}',
                    lhablock = 'FRBlock',
                    lhacode = [ 20 ])

grho0Zh = Parameter(name = 'grho0Zh',
                    nature = 'external',
                    type = 'real',
                    value = -160,
                    texname = '\\text{grho0Zh}',
                    lhablock = 'FRBlock',
                    lhacode = [ 21 ])

grho0ffL = Parameter(name = 'grho0ffL',
                     nature = 'external',
                     type = 'real',
                     value = 0.22,
                     texname = '\\text{grho0ffL}',
                     lhablock = 'FRBlock',
                     lhacode = [ 22 ])

grho0ffY = Parameter(name = 'grho0ffY',
                     nature = 'external',
                     type = 'real',
                     value = 0.0013,
                     texname = '\\text{grho0ffY}',
                     lhablock = 'FRBlock',
                     lhacode = [ 23 ])

grho0ttL = Parameter(name = 'grho0ttL',
                     nature = 'external',
                     type = 'real',
                     value = 0.22,
                     texname = '\\text{grho0ttL}',
                     lhablock = 'FRBlock',
                     lhacode = [ 24 ])

grho0bbL = Parameter(name = 'grho0bbL',
                     nature = 'external',
                     type = 'real',
                     value = -0.23,
                     texname = '\\text{grho0bbL}',
                     lhablock = 'FRBlock',
                     lhacode = [ 25 ])

grho0ttR = Parameter(name = 'grho0ttR',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{grho0ttR}',
                     lhablock = 'FRBlock',
                     lhacode = [ 26 ])

grho0bbR = Parameter(name = 'grho0bbR',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{grho0bbR}',
                     lhablock = 'FRBlock',
                     lhacode = [ 27 ])

grho0X53LX53L = Parameter(name = 'grho0X53LX53L',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grho0X53LX53L}',
                          lhablock = 'FRBlock',
                          lhacode = [ 28 ])

grho0X53RX53R = Parameter(name = 'grho0X53RX53R',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grho0X53RX53R}',
                          lhablock = 'FRBlock',
                          lhacode = [ 29 ])

grho0X23LX23L = Parameter(name = 'grho0X23LX23L',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grho0X23LX23L}',
                          lhablock = 'FRBlock',
                          lhacode = [ 30 ])

grho0X23RX23R = Parameter(name = 'grho0X23RX23R',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grho0X23RX23R}',
                          lhablock = 'FRBlock',
                          lhacode = [ 31 ])

grho0X23LtL = Parameter(name = 'grho0X23LtL',
                        nature = 'external',
                        type = 'real',
                        value = 0.1,
                        texname = '\\text{grho0X23LtL}',
                        lhablock = 'FRBlock',
                        lhacode = [ 32 ])

grho0X23RtR = Parameter(name = 'grho0X23RtR',
                        nature = 'external',
                        type = 'real',
                        value = 0.1,
                        texname = '\\text{grho0X23RtR}',
                        lhablock = 'FRBlock',
                        lhacode = [ 33 ])

grho0X23LT23L = Parameter(name = 'grho0X23LT23L',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grho0X23LT23L}',
                          lhablock = 'FRBlock',
                          lhacode = [ 34 ])

grho0X23RT23R = Parameter(name = 'grho0X23RT23R',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grho0X23RT23R}',
                          lhablock = 'FRBlock',
                          lhacode = [ 35 ])

grho0T23LT23L = Parameter(name = 'grho0T23LT23L',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grho0T23LT23L}',
                          lhablock = 'FRBlock',
                          lhacode = [ 36 ])

grho0T23RT23R = Parameter(name = 'grho0T23RT23R',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grho0T23RT23R}',
                          lhablock = 'FRBlock',
                          lhacode = [ 37 ])

grho0T23LtL = Parameter(name = 'grho0T23LtL',
                        nature = 'external',
                        type = 'real',
                        value = 0.1,
                        texname = '\\text{grho0T23LtL}',
                        lhablock = 'FRBlock',
                        lhacode = [ 38 ])

grho0T23RtR = Parameter(name = 'grho0T23RtR',
                        nature = 'external',
                        type = 'real',
                        value = 0.1,
                        texname = '\\text{grho0T23RtR}',
                        lhablock = 'FRBlock',
                        lhacode = [ 39 ])

grho0B13LB13L = Parameter(name = 'grho0B13LB13L',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grho0B13LB13L}',
                          lhablock = 'FRBlock',
                          lhacode = [ 40 ])

grho0B13RB13R = Parameter(name = 'grho0B13RB13R',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grho0B13RB13R}',
                          lhablock = 'FRBlock',
                          lhacode = [ 41 ])

grhoprhomZ = Parameter(name = 'grhoprhomZ',
                       nature = 'external',
                       type = 'real',
                       value = 0.55,
                       texname = '\\text{grhoprhomZ}',
                       lhablock = 'FRBlock',
                       lhacode = [ 42 ])

grhopWmrho0 = Parameter(name = 'grhopWmrho0',
                        nature = 'external',
                        type = 'real',
                        value = -0.63,
                        texname = '\\text{grhopWmrho0}',
                        lhablock = 'FRBlock',
                        lhacode = [ 43 ])

grhoprhomrho0 = Parameter(name = 'grhoprhomrho0',
                          nature = 'external',
                          type = 'real',
                          value = 0.1,
                          texname = '\\text{grhoprhomrho0}',
                          lhablock = 'FRBlock',
                          lhacode = [ 44 ])

ghWW = Parameter(name = 'ghWW',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{ghWW}',
                 lhablock = 'FRBlock',
                 lhacode = [ 45 ])

ghZZ = Parameter(name = 'ghZZ',
                 nature = 'external',
                 type = 'real',
                 value = 100,
                 texname = '\\text{ghZZ}',
                 lhablock = 'FRBlock',
                 lhacode = [ 46 ])

ghhWW = Parameter(name = 'ghhWW',
                  nature = 'external',
                  type = 'real',
                  value = 0.1,
                  texname = '\\text{ghhWW}',
                  lhablock = 'FRBlock',
                  lhacode = [ 47 ])

ghhZZ = Parameter(name = 'ghhZZ',
                  nature = 'external',
                  type = 'real',
                  value = 0.1,
                  texname = '\\text{ghhZZ}',
                  lhablock = 'FRBlock',
                  lhacode = [ 48 ])

gWT23LbL = Parameter(name = 'gWT23LbL',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{gWT23LbL}',
                     lhablock = 'FRBlock',
                     lhacode = [ 49 ])

gWX23LbL = Parameter(name = 'gWX23LbL',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{gWX23LbL}',
                     lhablock = 'FRBlock',
                     lhacode = [ 50 ])

gWtLB13L = Parameter(name = 'gWtLB13L',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{gWtLB13L}',
                     lhablock = 'FRBlock',
                     lhacode = [ 51 ])

gWtRB13R = Parameter(name = 'gWtRB13R',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{gWtRB13R}',
                     lhablock = 'FRBlock',
                     lhacode = [ 52 ])

gWX53LtL = Parameter(name = 'gWX53LtL',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{gWX53LtL}',
                     lhablock = 'FRBlock',
                     lhacode = [ 53 ])

gWX53RtR = Parameter(name = 'gWX53RtR',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{gWX53RtR}',
                     lhablock = 'FRBlock',
                     lhacode = [ 54 ])

gZT23LtL = Parameter(name = 'gZT23LtL',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{gZT23LtL}',
                     lhablock = 'FRBlock',
                     lhacode = [ 55 ])

gZT23RtR = Parameter(name = 'gZT23RtR',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{gZT23RtR}',
                     lhablock = 'FRBlock',
                     lhacode = [ 56 ])

gZX23LtL = Parameter(name = 'gZX23LtL',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{gZX23LtL}',
                     lhablock = 'FRBlock',
                     lhacode = [ 57 ])

gZX23RtR = Parameter(name = 'gZX23RtR',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{gZX23RtR}',
                     lhablock = 'FRBlock',
                     lhacode = [ 58 ])

ghT23LtR = Parameter(name = 'ghT23LtR',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{ghT23LtR}',
                     lhablock = 'FRBlock',
                     lhacode = [ 59 ])

ghtLT23R = Parameter(name = 'ghtLT23R',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{ghtLT23R}',
                     lhablock = 'FRBlock',
                     lhacode = [ 60 ])

ghX23LtR = Parameter(name = 'ghX23LtR',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{ghX23LtR}',
                     lhablock = 'FRBlock',
                     lhacode = [ 61 ])

ghtLX23R = Parameter(name = 'ghtLX23R',
                     nature = 'external',
                     type = 'real',
                     value = 0.1,
                     texname = '\\text{ghtLX23R}',
                     lhablock = 'FRBlock',
                     lhacode = [ 62 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

mrhop = Parameter(name = 'mrhop',
                  nature = 'external',
                  type = 'real',
                  value = 1800,
                  texname = '\\text{mrhop}',
                  lhablock = 'MASS',
                  lhacode = [ 9900213 ])

mrho0 = Parameter(name = 'mrho0',
                  nature = 'external',
                  type = 'real',
                  value = 1800,
                  texname = '\\text{mrho0}',
                  lhablock = 'MASS',
                  lhacode = [ 9900113 ])

MT23 = Parameter(name = 'MT23',
                 nature = 'external',
                 type = 'real',
                 value = 600,
                 texname = '\\text{MT23}',
                 lhablock = 'MASS',
                 lhacode = [ 8000001 ])

MB13 = Parameter(name = 'MB13',
                 nature = 'external',
                 type = 'real',
                 value = 600,
                 texname = '\\text{MB13}',
                 lhablock = 'MASS',
                 lhacode = [ 8000002 ])

MX53 = Parameter(name = 'MX53',
                 nature = 'external',
                 type = 'real',
                 value = 600,
                 texname = '\\text{MX53}',
                 lhablock = 'MASS',
                 lhacode = [ 8000003 ])

MX23 = Parameter(name = 'MX23',
                 nature = 'external',
                 type = 'real',
                 value = 600,
                 texname = '\\text{MX23}',
                 lhablock = 'MASS',
                 lhacode = [ 8000004 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00575308848,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

wrhop = Parameter(name = 'wrhop',
                  nature = 'external',
                  type = 'real',
                  value = 0.001,
                  texname = '\\text{wrhop}',
                  lhablock = 'DECAY',
                  lhacode = [ 9900213 ])

wrho0 = Parameter(name = 'wrho0',
                  nature = 'external',
                  type = 'real',
                  value = 0.001,
                  texname = '\\text{wrho0}',
                  lhablock = 'DECAY',
                  lhacode = [ 9900113 ])

WT23 = Parameter(name = 'WT23',
                 nature = 'external',
                 type = 'real',
                 value = 0.001,
                 texname = '\\text{WT23}',
                 lhablock = 'DECAY',
                 lhacode = [ 8000001 ])

WB13 = Parameter(name = 'WB13',
                 nature = 'external',
                 type = 'real',
                 value = 0.001,
                 texname = '\\text{WB13}',
                 lhablock = 'DECAY',
                 lhacode = [ 8000002 ])

WX53 = Parameter(name = 'WX53',
                 nature = 'external',
                 type = 'real',
                 value = 0.001,
                 texname = '\\text{WX53}',
                 lhablock = 'DECAY',
                 lhacode = [ 8000003 ])

WX23 = Parameter(name = 'WX23',
                 nature = 'external',
                 type = 'real',
                 value = 0.001,
                 texname = '\\text{WX23}',
                 lhablock = 'DECAY',
                 lhacode = [ 8000004 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

