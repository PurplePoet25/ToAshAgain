from pygame import Rect

enemy_config = {
    1: {  # Act 1
        0: [  # Screen index
            {"type": "melee", "platform_index": 1, "sprite_path": "assets/enemies/act1/thornrat.png"},
        ],
        1: [  # Screen index
            {"type": "ranged", "x": 443, "y": 441, "sprite_path": "assets/enemies/act1/sporeling.png"}
        ],
        2: [  # Screen index
            {"type": "melee", "platform_index": 1, "sprite_path": "assets/enemies/act1/thornrat.png"},
            {"type": "ranged", "x": 573, "y": 189, "sprite_path": "assets/enemies/act1/sporeling.png"}
        ],
        3: [  # Screen index
            {"type": "ranged", "x": 385, "y": 315, "sprite_path": "assets/enemies/act1/sporeling.png"}
        ],
        4: [  # Screen index
            {"type": "ranged", "x": 399, "y": 75, "sprite_path": "assets/enemies/act1/sporeling.png"},
            {"type": "melee", "platform_index": 2, "sprite_path": "assets/enemies/act1/thornrat.png"}
        ],
        5: [  # Screen index
            {"type": "ranged", "x": 219, "y": 154, "sprite_path": "assets/enemies/act1/sporeling.png"}
        ],
        6: [  # Screen index
            {"type": "melee", "platform_index": 3, "sprite_path": "assets/enemies/act1/thornrat.png"}
        ],
        7: [  # Screen index
            {"type": "ranged", "x": 656, "y": 454, "sprite_path": "assets/enemies/act1/sporeling.png"}
        ],
        8: [  # Screen index
            {"type": "ranged", "x": 183, "y": 57, "sprite_path": "assets/enemies/act1/sporeling.png"},
            {"type": "melee", "platform_index": 3, "sprite_path": "assets/enemies/act1/thornrat.png"}
        ],
        9: [  # Screen index
            {"type": "ranged", "x": 177, "y": 63, "sprite_path": "assets/enemies/act1/sporeling.png"},
            {"type": "melee", "platform_index": 21, "sprite_path": "assets/enemies/act1/thornrat.png"}
        ],
    },
    2: {
        0: [
            {"type": "melee", "platform_index": 2, "sprite_path": "assets/enemies/act2/duskwing.png"}
        ],
        1: [
            {"type": "ranged", "x": 479, "y": 276, "sprite_path": "assets/enemies/act2/mistecho.png"}
        ],
        2: [
            {"type": "ranged", "x": 678, "y": 182, "sprite_path": "assets/enemies/act2/mistecho.png"}
        ],
        3: [
            {"type": "ranged", "x": 698, "y": 318, "sprite_path": "assets/enemies/act2/mistecho.png"},
            {"type": "melee", "platform_index": 3, "sprite_path": "assets/enemies/act2/duskwing.png"}
        ],
        4: [],
        5: [
            {"type": "ranged", "x": 353, "y": 321, "sprite_path": "assets/enemies/act2/mistecho.png"},
            {"type": "melee", "platform_index": 4, "sprite_path": "assets/enemies/act2/duskwing.png"}
        ],
        6: [
            {"type": "melee", "platform_index": 1, "sprite_path": "assets/enemies/act2/duskwing.png"},
            {"type": "melee", "platform_index": 2, "sprite_path": "assets/enemies/act2/duskwing.png"}
        ],
        7: [
            {"type": "ranged", "x": 538, "y": 130, "sprite_path": "assets/enemies/act2/mistecho.png"},
            {"type": "melee", "platform_index": 2, "sprite_path": "assets/enemies/act2/duskwing.png"}
        ],
        8: [
            {"type": "ranged", "x": 641, "y": 318, "sprite_path": "assets/enemies/act2/mistecho.png"},
            {"type": "melee", "platform_index": 5, "sprite_path": "assets/enemies/act2/duskwing.png"}
        ],
        9: [
            {"type": "ranged", "x": 722, "y": 343, "sprite_path": "assets/enemies/act2/mistecho.png"},
        ]
    },
    3: {  # Act 3
        0: [  # Screen index
            {"type": "melee", "platform_index": 2, "sprite_path": "assets/enemies/act3/sandcrawler.png"}
        ],
        1: [
            {"type": "ranged", "x": 240, "y": 62, "sprite_path": "assets/enemies/act3/mirageflame.png"},
            {"type": "melee", "platform_index": 3, "sprite_path": "assets/enemies/act3/sandcrawler.png"}
        ],
        2: [
            {"type": "ranged", "x": 315, "y": 83, "sprite_path": "assets/enemies/act3/mirageflame.png"},
            {"type": "ranged", "x": 505, "y": 330, "sprite_path": "assets/enemies/act3/mirageflame.png"}
        ],
        3: [
            {"type": "ranged", "x": 606, "y": 230, "sprite_path": "assets/enemies/act3/mirageflame.png"},
            {"type": "melee", "platform_index": 1, "sprite_path": "assets/enemies/act3/sandcrawler.png"}
        ],
        4: [
            {"type": "ranged", "x": 336, "y": 390, "sprite_path": "assets/enemies/act3/mirageflame.png"},
            {"type": "melee", "platform_index": 4, "sprite_path": "assets/enemies/act3/sandcrawler.png"}
        ],
        5: [
            {"type": "ranged", "x": 155, "y": 78, "sprite_path": "assets/enemies/act3/mirageflame.png"},
            {"type": "ranged", "x": 311, "y": 178, "sprite_path": "assets/enemies/act3/mirageflame.png"},
            {"type": "ranged", "x": 456, "y": 65, "sprite_path": "assets/enemies/act3/mirageflame.png"},
        ],
        6: [
            {"type": "melee", "platform_index": 3, "sprite_path": "assets/enemies/act3/sandcrawler.png"},
            {"type": "melee", "platform_index": 4, "sprite_path": "assets/enemies/act3/sandcrawler.png"}
        ],
        7: [
            {"type": "ranged", "x": 428, "y": 248, "sprite_path": "assets/enemies/act3/mirageflame.png"}
        ],
        8: [
            {"type": "ranged", "x": 114, "y": 135, "sprite_path": "assets/enemies/act3/mirageflame.png"},
            {"type": "melee", "platform_index": 5, "sprite_path": "assets/enemies/act3/sandcrawler.png"}
        ],
        9: [
            {"type": "ranged", "x": 693, "y": 205, "sprite_path": "assets/enemies/act3/mirageflame.png"}
        ]    
    },
    4: {  # Act 4
        0: [  # Screen index
            {"type": "melee", "platform_index": 3, "sprite_path": "assets/enemies/act4/embergolem.png"}
        ],
        1: [  # Screen index
            {"type": "melee", "platform_index": 19, "sprite_path": "assets/enemies/act4/embergolem.png"},
            {"type": "melee", "platform_index": 24, "sprite_path": "assets/enemies/act4/embergolem.png"},
            {"type": "ranged", "x": 293, "y": 136, "sprite_path": "assets/enemies/act4/lavapuff.png"}
        ],
        2: [
            {"type": "ranged", "x": 336, "y": 132, "sprite_path": "assets/enemies/act4/lavapuff.png"},
            {"type": "ranged", "x": 637, "y": 232, "sprite_path": "assets/enemies/act4/lavapuff.png"}
        ],
        3: [
            {"type": "ranged", "x": 627, "y": 258, "sprite_path": "assets/enemies/act4/lavapuff.png"},
            {"type": "melee", "platform_index": 1, "sprite_path": "assets/enemies/act4/embergolem.png"}
        ],
        4: [
            {"type": "ranged", "x": 470, "y": 140, "sprite_path": "assets/enemies/act4/lavapuff.png"},
            {"type": "ranged", "x": 627, "y": 282, "sprite_path": "assets/enemies/act4/lavapuff.png"},
            {"type": "melee", "platform_index": 1, "sprite_path": "assets/enemies/act4/embergolem.png"}
        ],
        5: [
            {"type": "ranged", "x": 634, "y": 270, "sprite_path": "assets/enemies/act4/lavapuff.png"},
            {"type": "ranged", "x": 187, "y": 230, "sprite_path": "assets/enemies/act4/lavapuff.png"},
            {"type": "melee", "platform_index": 2, "sprite_path": "assets/enemies/act4/embergolem.png"}
        ],
        6: [
            {"type": "ranged", "x": 319, "y": 144, "sprite_path": "assets/enemies/act4/lavapuff.png"},
            {"type": "ranged", "x": 430, "y": 400, "sprite_path": "assets/enemies/act4/lavapuff.png"},
            {"type": "melee", "platform_index": 5, "sprite_path": "assets/enemies/act4/embergolem.png"}
        ],
        7: [
            {"type": "ranged", "x": 352, "y": 186, "sprite_path": "assets/enemies/act4/lavapuff.png"},
            {"type": "melee", "platform_index": 2, "sprite_path": "assets/enemies/act4/embergolem.png"}
        ],
        8: [
            {"type": "ranged", "x": 218, "y": 195, "sprite_path": "assets/enemies/act4/lavapuff.png"},
            {"type": "melee", "platform_index": 1, "sprite_path": "assets/enemies/act4/embergolem.png"},
            {"type": "melee", "platform_index": 3, "sprite_path": "assets/enemies/act4/embergolem.png"}
        ]
    }
}
