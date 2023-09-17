
import random
import re


def damageFromText(message):
    match = re.search(r'/damage (\d+)', message)
    damage = int(match.group(1))
    
    return damageCount(damage)
    
    
def damageFromJson(message):
    damage = int(message['damage'])
    
    return damageCount(damage)
    
    
def damageCount(damage):
    dice = [1, 2, 0, 0, "effect", "effect"]
    total_damage = 0
    num_effects = 0
    thrown = []
    for i in range(damage):
        score = random.choice(dice)
        thrown.append(score)
        if score == "effect":
            num_effects += 1
            score = 1
        total_damage += score
        
    return toData(thrown, total_damage, num_effects)
        
        
def toData(dices, damage, effects):
    data = {
        "type": "damage",
        "damage": damage,
        "effects": effects,
        "rolls": dices
    }
    return data