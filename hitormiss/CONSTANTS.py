from typing import Optional

user_defaults = {
    "hp": 100,
    "accuracy": 10,
    "throws": 0,
    "hits": 0,
    "misses": 0,
    "kills": 0,
    "deaths": 0,
    "items": {"frag": 1},
}

global_defaults = {
    "items": {
        "Frag": {
            "price": 1000,
            "damage": 10,
            "uses": 1,
            "cooldown": 60,
            "accuracy": 15,
            "throwable": True,
            "emoji": "💣",
        },
        "WunderWaffle": {
            "price": 2500,
            "damage": 20,
            "uses": 1,
            "cooldown": 60,
            "accuracy": 15,
            "throwable": True,
            "emoji": "🔫",
        },
        "Ray Gun": {
            "price": 5000,
            "damage": 30,
            "uses": 2,
            "cooldown": 90,
            "accuracy": 20,
            "throwable": True,
            "emoji": "🔫",
        },
        "VR11": {
            "price": 7500,
            "damage": 40,
            "uses": 3,
            "cooldown": 120,
            "accuracy": 10,
            "throwable": True,
            "emoji": "🔫",
        },
        "Scorcher": {
            "price": 10000,
            "damage": 50,
            "uses": 3,
            "cooldown": 120,
            "accuracy": 10,
            "throwable": True,
            "emoji": "🪓",
        },
        "Stim": {
            "price": 5000,
            "damage": 40,  # here damage will actually be the amount it can heal.
            "uses": 1,
            "cooldown": 200,
            "accuracy": 30,  # here accuracy will be the chance of healing completely.
            "throwable": False,
            "emoji": "🩹",
        },
    }
}

dc_fields = [
    ("uses", int),
    ("damage", int),
    ("cooldown", int),
    ("accuracy", int),
    ("throwable", bool),
    ("price", int),
    ("emoji", Optional[str]),
]

lb_types = ["throws", "kills", "deaths", "hits", "misses", "kdr"]
