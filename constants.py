# offsets/ addresses you need to read the gamememory

PROCESS_NAME = 'League of Legends.exe'

oTFTObject = 0x2491BC8
oName = 0x54
oCheck = 0x58
oX = 0xD8
oY = 0xE0
oX2 = 0xE4
oY2 = 0xEC

oTFTAction = 0x2491B40

oTFTChamps = 0x1842D4C
TFTC = 0x4

field = {
        1: {

                (3628, 24880): '', (4060, 24880): '', (4488, 24880): '', (4916, 24880): '',
                (5344, 24880): '', (5776, 24880): '', (6204, 24880): '',
                (3844, 24508): '', (4272, 24508): '', (4704, 24508): '', (5132, 24508): '',
                (5560, 24508): '', (5988, 24508): '', (6420, 24508): '',
                (3628, 24136): '', (4060, 24136): '', (4488, 24136): '', (4916, 24136): '',
                (5344, 24136): '', (5776, 24136): '', (6204, 24136): '',
                (3844, 23764): '', (4272, 23764): '', (4704, 23764): '', (5132, 23764): '',
                (5560, 23764): '', (5988, 23764): '', (6420, 23764): '',
                (3408, 23280): '', (3784, 23280): '', (4156, 23280): '', (4532, 23280): '',
                (4904,  23280): '', (5280,  23280): '',  (5652, 23280): '', (6028, 23280): '', (6396, 23280): '',
        },
        2: {
                (13628, 24880): '', (14060, 24880): '', (14488, 24880): '', (14916, 24880): '',
                (15340, 24880): '', (15772, 24880): '', (16200, 24880): '',
                (13844, 24508): '', (14272, 24508): '', (14704, 24508): '', (15128, 24508): '',
                (15556, 24508): '', (15984, 24508): '', (16416, 24508): '',
                (13628, 24136): '', (14060, 24136): '', (14488, 24136): '', (14916, 24136): '',
                (15344, 24136): '', (15772, 24136): '', (16200, 24136): '',             # may not correct (15344, 24136)
                (13844, 23764): '', (14272, 23764): '', (14704, 23764): '', (15128, 23764): '',
                (15556, 23764): '', (15984, 23764): '', (16416, 23764): '',
                (13408, 23280): '', (13784, 23280): '', (14156, 23280): '', (14532, 23280): '',
                (14904, 23280): '', (15276, 23280): '', (15648, 23280): '', (16024, 23280): '', (16395, 23280): '',
        },

        3: {
                (23624, 24880): '', (24056, 24880): '', (24484, 24880): '', (24912, 24880): '',
                (25340, 24880): '', (25772, 24880): '', (26200, 24880): '',
                (23840, 24508): '', (24268, 24508): '', (24700, 24508): '', (25128, 24508): '',
                (25556, 24508): '', (25984, 24508): '', (26416, 24508): '',
                (23624, 24136): '', (24056, 24136): '', (24484, 24136): '', (24912, 24136): '',
                (25340, 24136): '', (25772, 24136): '', (26200, 24136): '',
                (23840, 23764): '', (24268, 23764): '', (24700, 23764): '', (25128, 23764): '',
                (25556, 23764): '', (25984, 23764): '', (26416, 23764): '',
                (23404, 23280): '', (23780, 23280): '', (24152, 23280): '', (24528, 23280): '',
                (24900, 23280): '', (25276, 23280): '', (25648, 23280): '', (26024, 23280): '', (26396, 23280): '',
        },
        4: {
                (3628, 14884): '', (4060, 14884): '', (4488, 14884): '', (4916, 14884): '',
                (5344, 14884): '', (5776, 14884): '', (6204, 14884): '',
                (3844, 14512): '', (4272, 14512): '', (4704, 14512): '', (5132, 14512): '',
                (5560, 14512): '', (5988, 14512): '', (6420, 14512): '',
                (3628, 14140): '', (4060, 14140): '', (4488, 14140): '', (4916, 14140): '',
                (5344, 14140): '', (5776, 14140): '', (6204, 14140): '',
                (3844, 13768): '', (4272, 13768): '', (4704, 13768): '', (5132, 13768): '',
                (5560, 13768): '', (5988, 13768): '', (6420, 13768): '',
                (3408, 13284): '', (3784, 13284): '', (4156, 13284): '', (4532, 13284): '',
                (4904, 13284): '', (5280, 13284): '', (5652, 13284): '', (6028, 13284): '', (6396, 13284): '',
        },
        5: {
                (23624, 14884): '', (24056, 14884): '', (24484, 14884): '', (24912, 14884): '',
                (25340, 14884): '', (25772, 14884): '', (26200, 14884): '',
                (23840, 14512): '', (24268, 14512): '', (24700, 14512): '', (25128, 14512): '',
                (25556, 14512): '', (25984, 14512): '', (26415, 14512): '',
                (23624, 14140): '', (24056, 14140): '', (24484, 14140): '', (24912, 14140): '',
                (25340, 14140): '', (25772, 14140): '', (26200, 14140): '',
                (23840, 13768): '', (24268, 13768): '', (24700, 13768): '', (25128, 13768): '',
                (25556, 13768): '', (25984, 13768): '', (26416, 13768): '',
                (23404, 13284): '', (23780, 13284): '', (24152, 13284): '', (24528, 13284): '',
                (24900, 13284): '', (25276, 13284): '', (25648, 13284): '', (26024, 13284): '', (26396, 13284): '',
        },
        6: {
                (3628, 4884): '', (4060, 4884): '', (4488, 4884): '', (4916, 4884): '',
                (5344, 4884): '', (5776, 4884): '', (6204, 4884): '',
                (3844, 4512): '', (4272, 4512): '', (4704, 4512): '', (5132, 4512): '',
                (5560, 4512): '', (5988, 4512): '', (6420, 4512): '',
                (3628, 4140): '', (4060, 4140): '', (4488, 4140): '', (4916, 4140): '',
                (5344, 4140): '', (5776, 4140): '', (6204, 4140): '',
                (3844, 3768): '', (4272, 3768): '', (4704, 3768): '', (5132, 3768): '',
                (5560, 3768): '', (5988, 3768): '', (6420, 3768): '',
                (3408, 3284): '', (3784, 3284): '', (4156, 3284): '', (4532, 3284): '',
                (4904, 3284): '', (5280, 3284): '', (5652, 3284): '', (6028, 3284): '', (6396, 3284): '',
        },
        7: {
                (13628, 4884): '', (14060, 4884): '', (14488, 4884): '', (14916, 4884): '',
                (15340, 4884): '', (15772, 4884): '', (16200, 4884): '',
                (13844, 4512): '', (14272, 4512): '', (14704, 4512): '', (15128, 4512): '',
                (15556, 4512): '', (15984, 4512): '', (16416, 4512): '',
                (13628, 4140): '', (14060, 4140): '', (14488, 4140): '', (14916, 4140): '',
                (15340, 4140): '', (15772, 4140): '', (16200, 4140): '',
                (13844, 3768): '', (14272, 3768): '', (14704, 3768): '', (15128, 3768): '',
                (15556, 3768): '', (15984, 3768): '', (16416, 3768): '',
                (13408, 3284): '', (13784, 3284): '', (14156, 3284): '', (14532, 3284): '',
                (14904, 3284): '', (15276, 3284): '', (15648, 3284): '', (16024, 3284): '', (16396, 3284): '',
        },
        8: {
                (23624, 4884): '', (24056, 4884): '', (24484, 4884): '', (24912, 4884): '',
                (25340, 4884): '', (25772, 4884): '', (26200, 4884): '',
                (23840, 4512): '', (24268, 4512): '', (24700, 4512): '', (25128, 4512): '',
                (25556, 4512): '', (25984, 4512): '', (26416, 4512): '',
                (23624, 4140): '', (24056, 4140): '', (24484, 4140): '', (24911, 4140): '',
                (25340, 4140): '', (25772, 4140): '', (26200, 4140): '',
                (23840, 3768): '', (24268, 3768): '', (24700, 3768): '', (25127, 3768): '',
                (25556, 3768): '', (25984, 3768): '', (26416, 3768): '',
                (23404, 3284): '', (23780, 3284): '', (24152, 3284): '', (24528, 3284): '',
                (24900, 3284): '', (25276, 3284): '', (25648, 3284): '', (26024, 3284): '', (26396, 3284): ''
        }
}