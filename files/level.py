import pygame
from settings import *

# --- Core Screens (Main Hub, Pedestal, etc.) ---
core_platforms = [
    [   # 0: pedestal
        pygame.Rect(0, 540, 900, 10),
        pygame.Rect(329, 508, 93, 29),
        pygame.Rect(307, 487, 90, 23),
        pygame.Rect(284, 467, 85, 24),
        pygame.Rect(263, 449, 82, 20),
        pygame.Rect(183, 448, 79, 87),
        pygame.Rect(216, 430, 62, 15),
        pygame.Rect(223, 394, 46, 37),
        pygame.Rect(216, 376, 63, 18),
    ],
    [   # 1: normal ground (background-1.png)
        pygame.Rect(0, GROUND_LEVEL, 800, 5),
    ],
    [   # 2: ground + 3 platforms (background1.png)
        pygame.Rect(280, 420, 60, 5),
        pygame.Rect(500, 420, 85, 5),
        pygame.Rect(0, 365, 155, 5),
        pygame.Rect(0, GROUND_LEVEL, 900, 5),
    ],
    [   # 3: ground + 2 voids (background2.png)
        pygame.Rect(0, GROUND_LEVEL, 150, 5),
        pygame.Rect(300, GROUND_LEVEL, 180, 5),
        pygame.Rect(700, GROUND_LEVEL, 300, 5),
    ],
    [   # 4: teacup screen
        pygame.Rect(2, 294, 132, 22),
        pygame.Rect(214, 164, 116, 19),
        pygame.Rect(443, 235, 113, 20),
        pygame.Rect(46, 477, 754, 24),
    ]
]

# --- Act-Specific Platform Sets ---

# Act 1: green1, green2, green3, ...
act1_platforms = [
    [
    pygame.Rect(-2, 451, 297, 39),
    pygame.Rect(527, 392, 272, 39),
    ],
    [
    pygame.Rect(-2, 421, 178, 33),
    pygame.Rect(428, 526, 131, 30),
    pygame.Rect(540, 404, 260, 28),
    ],
    [
    pygame.Rect(-2, 418, 270, 39),
    pygame.Rect(169, 174, 195, 36),
    pygame.Rect(465, 283, 200, 34),
    pygame.Rect(589, 461, 210, 40),
    ],
    [
    pygame.Rect(-2, 351, 234, 25),
    pygame.Rect(230, 362, 12, 29),
    pygame.Rect(245, 409, 33, 29),
    pygame.Rect(298, 408, 32, 45),
    pygame.Rect(346, 410, 42, 37),
    pygame.Rect(406, 410, 40, 31),
    pygame.Rect(603, 284, 196, 24),
    pygame.Rect(554, 315, 17, 51),
    pygame.Rect(509, 528, 293, 26),
    ],
    [
    pygame.Rect(-2, 434, 176, 28),
    pygame.Rect(265, 474, 337, 52),
    pygame.Rect(591, 526, 210, 33),
    pygame.Rect(389, 153, 90, 13),
    pygame.Rect(294, 298, 52, 31),
    pygame.Rect(523, 299, 55, 27),
    ],
    [
    pygame.Rect(-2, 455, 216, 90),
    pygame.Rect(207, 534, 330, 32),
    pygame.Rect(494, 358, 225, 30),
    pygame.Rect(507, 388, 39, 147),
    pygame.Rect(165, 243, 126, 43),
    pygame.Rect(379, 50, 123, 44),
    pygame.Rect(676, 388, 16, 138),
    pygame.Rect(691, 521, 112, 37),
    ],
    [
    pygame.Rect(-2, 416, 250, 48),
    pygame.Rect(214, 463, 22, 112),
    pygame.Rect(235, 549, 269, 30),
    pygame.Rect(584, 494, 216, 31),
    pygame.Rect(598, 307, 205, 32),
    ],
    [
    pygame.Rect(-2, 416, 252, 46),
    pygame.Rect(431, 365, 367, 41),
    pygame.Rect(566, 549, 235, 49),
    pygame.Rect(226, 462, 13, 138),
    ],
    [
    pygame.Rect(-2, 461, 258, 31),
    pygame.Rect(50, 146, 200, 28),
    pygame.Rect(480, 399, 117, 29),
    pygame.Rect(613, 329, 158, 28),
    pygame.Rect(523, 538, 180, 29),
    ],
    [
    pygame.Rect(-2, 376, 208, 38),
    pygame.Rect(122, 414, 55, 27),
    pygame.Rect(114, 440, 33, 26),
    pygame.Rect(125, 465, 12, 97),
    pygame.Rect(137, 542, 213, 20),
    pygame.Rect(358, 432, 104, 30),
    pygame.Rect(375, 462, 105, 32),
    pygame.Rect(400, 494, 104, 28),
    pygame.Rect(420, 522, 110, 32),
    pygame.Rect(440, 555, 118, 43),
    pygame.Rect(347, 402, 126, 28),
    pygame.Rect(370, 370, 123, 28),
    pygame.Rect(390, 339, 124, 27),
    pygame.Rect(409, 309, 122, 27),
    pygame.Rect(431, 276, 131, 32),
    pygame.Rect(474, 209, 42, 57),
    pygame.Rect(469, 264, 59, 11),
    pygame.Rect(460, 193, 66, 13),
    pygame.Rect(41, 146, 203, 26),
    pygame.Rect(549, 307, 13, 35),
    pygame.Rect(562, 326, 240, 20),
    pygame.Rect(580, 485, 222, 23),
]
    # Add more here for green2, green3...
]

# Act 2: blue1, blue2, ...
act2_platforms = [
    [
    pygame.Rect(-2, 459, 300, 46),
    pygame.Rect(298, 469, 11, 29),
    pygame.Rect(490, 461, 312, 45),
    ],
    [
    pygame.Rect(-2, 385, 108, 38),
    pygame.Rect(105, 394, 17, 29),
    pygame.Rect(167, 381, 113, 29),
    pygame.Rect(155, 242, 140, 24),
    pygame.Rect(190, 225, 64, 15),
    pygame.Rect(462, 390, 120, 33),
    pygame.Rect(446, 406, 19, 14),
    pygame.Rect(582, 407, 14, 15),
    pygame.Rect(485, 378, 77, 11),
    pygame.Rect(621, 71, 56, 9),
    pygame.Rect(601, 79, 89, 9),
    pygame.Rect(590, 87, 114, 27),
    pygame.Rect(574, 106, 145, 16),
    ],
    [
    pygame.Rect(77, 413, 106, 9),
    pygame.Rect(54, 420, 160, 20),
    pygame.Rect(47, 427, 172, 22),
    pygame.Rect(480, 405, 38, 8),
    pygame.Rect(464, 410, 82, 17),
    pygame.Rect(450, 426, 104, 21),
    pygame.Rect(571, 274, 187, 31),
    pygame.Rect(564, 284, 8, 20),
    pygame.Rect(606, 268, 44, 5),
    pygame.Rect(709, 268, 25, 7),
    ],
    [
    pygame.Rect(-2, 373, 210, 34),
    pygame.Rect(209, 376, 7, 26),
    pygame.Rect(268, 428, 141, 19),
    pygame.Rect(469, 338, 126, 24),
    pygame.Rect(466, 535, 130, 16),
    pygame.Rect(631, 418, 133, 27),
    ],
    [
    pygame.Rect(-2, 414, 130, 32),
    pygame.Rect(363, 454, 84, 20),
    pygame.Rect(380, 447, 52, 7),
    pygame.Rect(470, 410, 118, 28),
    pygame.Rect(458, 417, 12, 14),
    pygame.Rect(586, 412, 12, 21),
    ],
    [
    pygame.Rect(-2, 446, 172, 42),
    pygame.Rect(170, 450, 21, 36),
    pygame.Rect(343, 414, 114, 32),
    pygame.Rect(335, 423, 7, 16),
    pygame.Rect(570, 448, 232, 41),
    pygame.Rect(598, 434, 36, 12),
    pygame.Rect(648, 435, 43, 11),
    pygame.Rect(710, 434, 56, 12),
    ],
    [
    pygame.Rect(20, 340, 252, 34),
    pygame.Rect(341, 399, 213, 27),
    pygame.Rect(622, 456, 181, 33),
    ],
    [
    pygame.Rect(-2, 463, 298, 45),
    pygame.Rect(298, 472, 12, 27),
    pygame.Rect(355, 378, 183, 22),
    pygame.Rect(532, 232, 248, 20),
    pygame.Rect(569, 446, 197, 37),
    pygame.Rect(558, 457, 11, 21),
    ],
    [
    pygame.Rect(-2, 397, 223, 37),
    pygame.Rect(221, 404, 15, 28),
    pygame.Rect(294, 332, 209, 34),
    pygame.Rect(464, 280, 42, 50),
    pygame.Rect(461, 314, 5, 13),
    pygame.Rect(627, 198, 175, 32),
    pygame.Rect(613, 211, 15, 15),
    pygame.Rect(624, 420, 150, 19),
    pygame.Rect(634, 414, 128, 4),
    ],
    [
    pygame.Rect(-2, 434, 173, 38),
    pygame.Rect(298, 510, 164, 21),
    pygame.Rect(532, 250, 62, 14),
    pygame.Rect(537, 263, 49, 47),
    pygame.Rect(534, 310, 56, 12),
    pygame.Rect(517, 325, 118, 18),
    pygame.Rect(490, 344, 84, 18),
    pygame.Rect(474, 364, 84, 19),
    pygame.Rect(457, 385, 89, 20),
    pygame.Rect(440, 405, 88, 21),
    pygame.Rect(423, 425, 86, 19),
    pygame.Rect(405, 444, 89, 21),
    pygame.Rect(387, 465, 87, 19),
    pygame.Rect(371, 485, 86, 24),
    pygame.Rect(684, 434, 116, 35),
    pygame.Rect(673, 446, 12, 19),
    pygame.Rect(790, 6, 9, 582),
    ]
]

# Act 3: umber1, ...
act3_platforms = [
    [
    pygame.Rect(18, 405, 189, 29),
    pygame.Rect(206, 190, 134, 27),
    pygame.Rect(460, 465, 343, 26),
    ],
    [
    pygame.Rect(-2, 262, 181, 22),
    pygame.Rect(181, 148, 123, 22),
    pygame.Rect(268, 389, 122, 25),
    pygame.Rect(490, 464, 313, 28),
    ],
    [
    pygame.Rect(-2, 490, 237, 24),
    pygame.Rect(70, 295, 136, 23),
    pygame.Rect(240, 174, 126, 25),
    pygame.Rect(322, 520, 108, 18),
    pygame.Rect(498, 427, 68, 39),
    pygame.Rect(566, 446, 238, 20),
    ],
    [
    pygame.Rect(24, 467, 154, 27),
    pygame.Rect(249, 146, 134, 24),
    pygame.Rect(290, 376, 97, 14),
    pygame.Rect(581, 307, 103, 24),
    pygame.Rect(545, 451, 256, 31),
    pygame.Rect(533, 461, 13, 21),
    ],
    [
    pygame.Rect(-3, 421, 170, 25),
    pygame.Rect(55, 100, 120, 21),
    pygame.Rect(331, 171, 119, 22),
    pygame.Rect(286, 476, 119, 23),
    pygame.Rect(478, 532, 151, 25),
    pygame.Rect(610, 418, 192, 24),
    pygame.Rect(621, 442, 29, 127),
    pygame.Rect(611, 240, 82, 22),
    ],
    [
    pygame.Rect(-6, 519, 289, 31),
    pygame.Rect(64, 319, 107, 23),
    pygame.Rect(126, 164, 125, 23),
    pygame.Rect(310, 261, 60, 22),
    pygame.Rect(461, 154, 41, 29),
    pygame.Rect(622, 221, 25, 77),
    pygame.Rect(608, 242, 13, 66),
    pygame.Rect(596, 258, 10, 32),
    pygame.Rect(334, 548, 181, 51),
    pygame.Rect(513, 480, 26, 119),
    pygame.Rect(499, 459, 300, 31),
    ],
    [
    pygame.Rect(14, 407, 115, 29),
    pygame.Rect(102, 312, 101, 19),
    pygame.Rect(186, 183, 120, 22),
    pygame.Rect(441, 230, 361, 32),
    pygame.Rect(414, 474, 392, 32),
    ],
    [
    pygame.Rect(30, 350, 119, 26),
    pygame.Rect(98, 191, 127, 27),
    pygame.Rect(228, 471, 114, 27),
    pygame.Rect(350, 333, 140, 26),
    pygame.Rect(538, 437, 154, 28),
    pygame.Rect(670, 317, 131, 27),
    pygame.Rect(686, 343, 22, 39),
    pygame.Rect(698, 380, 11, 40),
    pygame.Rect(686, 418, 26, 45),
    ],
    [
    pygame.Rect(-2, 574, 151, 24),
    pygame.Rect(97, 220, 113, 25),
    pygame.Rect(272, 379, 144, 24),
    pygame.Rect(366, 116, 130, 26),
    pygame.Rect(600, 207, 201, 28),
    pygame.Rect(566, 493, 235, 34),
    ],
    [
    pygame.Rect(34, 332, 116, 27),
    pygame.Rect(162, 214, 141, 25),
    pygame.Rect(358, 465, 237, 27),
    pygame.Rect(431, 442, 71, 22),
    pygame.Rect(442, 391, 48, 52),
    pygame.Rect(434, 378, 65, 15),
    pygame.Rect(522, 444, 86, 19),
    pygame.Rect(542, 421, 86, 22),
    pygame.Rect(568, 399, 78, 20),
    pygame.Rect(586, 377, 75, 21),
    pygame.Rect(610, 357, 67, 21),
    pygame.Rect(629, 334, 68, 22),
    pygame.Rect(649, 310, 66, 25),
    pygame.Rect(693, 289, 112, 21),
    pygame.Rect(778, 6, 22, 581),
    ]
]

# Act 4: red1, ...
act4_platforms = [
    [
    pygame.Rect(-3, 418, 311, 29),
    pygame.Rect(307, 424, 12, 38),
    pygame.Rect(319, 242, 135, 18),
    pygame.Rect(492, 342, 178, 20),
    pygame.Rect(492, 445, 311, 22),
    pygame.Rect(477, 458, 13, 12),
    ],
    [
    pygame.Rect(779, 258, 24, 11),
    pygame.Rect(769, 270, 37, 17),
    pygame.Rect(758, 286, 47, 18),
    pygame.Rect(740, 305, 62, 14),
    pygame.Rect(727, 322, 73, 16),
    pygame.Rect(715, 336, 85, 14),
    pygame.Rect(704, 350, 96, 12),
    pygame.Rect(691, 365, 107, 8),
    pygame.Rect(682, 376, 112, 13),
    pygame.Rect(673, 386, 128, 13),
    pygame.Rect(671, 402, 23, 42),
    pygame.Rect(669, 447, 21, 15),
    pygame.Rect(656, 460, 22, 15),
    pygame.Rect(646, 478, 24, 8),
    pygame.Rect(634, 488, 24, 17),
    pygame.Rect(619, 503, 46, 15),
    pygame.Rect(609, 516, 41, 25),
    pygame.Rect(542, 532, 76, 19),
    pygame.Rect(533, 542, 8, 23),
    pygame.Rect(77, 527, 277, 28),
    pygame.Rect(-4, 422, 87, 32),
    pygame.Rect(66, 454, 12, 91),
    pygame.Rect(50, 343, 131, 19),
    pygame.Rect(292, 234, 122, 20),
    pygame.Rect(467, 331, 120, 19),
    pygame.Rect(353, 536, 8, 20),
    ],
    [
    pygame.Rect(-5, 418, 110, 28),
    pygame.Rect(89, 446, 9, 84),
    pygame.Rect(97, 523, 220, 34),
    pygame.Rect(97, 480, 12, 46),
    pygame.Rect(146, 342, 152, 28),
    pygame.Rect(340, 231, 146, 28),
    pygame.Rect(614, 327, 193, 31),
    pygame.Rect(619, 358, 41, 19),
    pygame.Rect(634, 378, 33, 63),
    pygame.Rect(636, 440, 18, 50),
    pygame.Rect(620, 480, 18, 30),
    pygame.Rect(604, 497, 16, 25),
    pygame.Rect(543, 514, 63, 14),
    pygame.Rect(526, 522, 23, 62),
    ],
    [
    pygame.Rect(-3, 466, 317, 30),
    pygame.Rect(344, 249, 194, 31),
    pygame.Rect(474, 465, 244, 33),
    pygame.Rect(576, 350, 227, 33),
    pygame.Rect(710, 384, 32, 115),
    ],
    [
    pygame.Rect(-6, 400, 192, 38),
    pygame.Rect(147, 200, 176, 30),
    pygame.Rect(426, 237, 161, 20),
    pygame.Rect(611, 383, 191, 21),
    pygame.Rect(511, 540, 171, 30),
    pygame.Rect(617, 409, 74, 49),
    pygame.Rect(670, 455, 30, 111),
    ],
    [
    pygame.Rect(74, 331, 158, 23),
    pygame.Rect(-3, 503, 165, 27),
    pygame.Rect(321, 486, 179, 25),
    pygame.Rect(632, 363, 143, 25),
    pygame.Rect(679, 494, 124, 27),
    ],
    [
    pygame.Rect(-3, 441, 159, 27),
    pygame.Rect(154, 562, 145, 21),
    pygame.Rect(134, 469, 19, 108),
    pygame.Rect(267, 238, 120, 24),
    pygame.Rect(422, 495, 93, 19),
    pygame.Rect(548, 456, 198, 26),
    pygame.Rect(583, 331, 220, 25),
    ],
    [
    pygame.Rect(-2, 345, 172, 29),
    pygame.Rect(169, 350, 12, 18),
    pygame.Rect(132, 474, 170, 29),
    pygame.Rect(129, 374, 14, 102),
    pygame.Rect(278, 282, 124, 20),
    pygame.Rect(596, 460, 206, 26),
    pygame.Rect(587, 467, 10, 19),
    ],
    [
    pygame.Rect(-2, 466, 220, 59),
    pygame.Rect(216, 512, 182, 27),
    pygame.Rect(144, 286, 170, 26),
    pygame.Rect(458, 360, 176, 27),
    pygame.Rect(600, 449, 206, 25),
    ],
    [
    pygame.Rect(106, 202, 152, 28),
    pygame.Rect(-3, 474, 190, 27),
    pygame.Rect(316, 398, 162, 20),
    pygame.Rect(530, 278, 162, 24),
    pygame.Rect(619, 474, 182, 25),
    pygame.Rect(372, 388, 49, 9),
    pygame.Rect(378, 355, 36, 31),
    pygame.Rect(372, 339, 47, 14),
    ]
]

win_platforms = [
    [
    pygame.Rect(0, 522, 802, 27),
    pygame.Rect(723, 392, 39, 55),
    pygame.Rect(648, 279, 33, 23),
    pygame.Rect(562, 494, 24, 26),
    pygame.Rect(336, 430, 166, 36),
    pygame.Rect(155, 406, 97, 46),
    pygame.Rect(122, 279, 112, 30),
    pygame.Rect(155, 250, 47, 28),
    ],   
    [
        pygame.Rect(-2, 530, 801, 14)
    ],
    [
        pygame.Rect(212, 460, 382, 38),
        pygame.Rect(226, 195, 26, 40),
        pygame.Rect(555, 188, 27, 43),
        pygame.Rect(602, 214, 36, 40)
    ]
]

cutscene_platforms = [
    [
    pygame.Rect(-64, 507, 604, 19),
    pygame.Rect(598, 440, 207+60, 23),
    ],
    [
    pygame.Rect(-64, 553, 800+60, 25)
    ],
    [
    pygame.Rect(-64, 526, 800+60, 20)
    ]
]

act1_spikes = {
    5: [pygame.Rect(226, 493, 294, 42)],
    6: [pygame.Rect(242, 506, 250, 44)],
    7: [pygame.Rect(453, 322, 153, 40)],
    8: [pygame.Rect(558, 506, 124, 32)],
    9: [pygame.Rect(164, 499, 161, 43)]
}

act3_spikes = {
    4: [pygame.Rect(626, 398, 137, 24)],
    5: [pygame.Rect(342, 503, 128, 48)],
    6: [
        pygame.Rect(107, 263, 90, 51),
        pygame.Rect(646, 437, 100, 39), 
    ],
    7: [
        pygame.Rect(246, 438, 78, 35),
        pygame.Rect(702, 286, 73, 35),
    ],
    8: [pygame.Rect(599, 178, 177, 31)],
    9: []

}

act4_spikes = {
    1: [    
        pygame.Rect(89, 442, 257, 86),
        pygame.Rect(546, 483, 35, 51),
        pygame.Rect(572, 441, 43, 78),
        pygame.Rect(610, 407, 61, 52),
    ],
    2: [
        pygame.Rect(167, 459, 143, 64),
        pygame.Rect(555, 426, 47, 90),
        pygame.Rect(588, 394, 48, 75),
    ],
    3: [pygame.Rect(519, 423, 148, 47)],
    4: [pygame.Rect(535, 452, 119, 86)],
    6: [pygame.Rect(172, 522, 124, 46)],
    7: [pygame.Rect(446, 426, 121, 73)]
}