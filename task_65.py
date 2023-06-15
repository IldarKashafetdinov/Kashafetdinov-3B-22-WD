import random
import math

TEN_PERCENT_MULTIPLIER = 1.1
HIT_TYPES = {
    "HEAD": 30,
    "BODY": 10,
    "LEGS": 5
}


def get_random_hit():
    keys_of_hit_types = list(HIT_TYPES.keys())
    rand = random.randint(0, len(keys_of_hit_types)-1)
    rand_hit_type = keys_of_hit_types[rand]

    return HIT_TYPES[rand_hit_type]


class Fighter:
    def __init__(self, name, level, health, attack, protection):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.protection = protection

    def health_change(self, health):
        self.health -= health

    def level_up(self):
        self.attack = math.floor(self.attack * TEN_PERCENT_MULTIPLIER)
        self.level = math.floor(self.level * TEN_PERCENT_MULTIPLIER)
        self.health = math.floor(self.health * TEN_PERCENT_MULTIPLIER)
        self.attack = math.floor(self.attack * TEN_PERCENT_MULTIPLIER)
        self.protection = math.floor(self.protection * TEN_PERCENT_MULTIPLIER)

    def hit(self):
        return {
            'type': get_random_hit(),
            'attack': self.attack
        }

    def block_hit(self):
        return {
            'type': get_random_hit(),
            'protection': self.protection
        }


def battle(first, second):
    random_fighter = random.randint(0, 1)
    if random_fighter == 1:
        return {
            'from': first.hit(),
            'to': second.block_hit(),
            'enemy': second
        }
    else:
        return {
            'from': second.hit(),
            'to': first.block_hit(),
            'enemy': first
        }


def check_aoe(act):
    if act['from']['type'] == act['to']['type']:
        if act['from']['attack'] < act['to']['protection']:
            return False
        else:
            return True
    else:
        return True


def health_update(act):
    health = math.floor(act['from']['type'] * act['from']['attack'])
    act['enemy'].health_change(health)


def fight(first, second):
    while bool(first.health > 0) & bool(second.health > 0):
        battle_act = battle(first, second)

        if check_aoe(battle_act):
            health_update(battle_act)

        print(
            'first:', first == battle_act['enemy'],
            'health', first.health,
            '; second:', second == battle_act['enemy'],
            'health', second.health
        )

    print('====')

    if first.health > second.health:
        return first
    else:
        return second


kms = Fighter('fighter-1', 1, 100, 1, 1)
ms = Fighter('fighter-1', 1, 100, 1, 1)
i = 1

while i <= 3:
    print('round №', i, kms.health, ms.health)
    winner = fight(kms, ms)

    if winner == kms:
        kms = Fighter('fighter-1', 1, 100, 1, 1)
        ms = Fighter('fighter-1', 1, 100, 1, 1)
        kms.level_up()
        print('WINNER KMS!!!')
    else:
        ms = Fighter('fighter-1', 1, 100, 1, 1)
        kms = Fighter('fighter-1', 1, 100, 1, 1)
        ms.level_up()
        print('WINNER MS!!!')

    i += 1
