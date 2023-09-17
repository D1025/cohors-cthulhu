import random
import re

def rollFromJson(message):
    num_dice = message['dice']
    attribute_value = message['attributeValue']
    skill_value = message['skillValue']
    focus = int(message['focus'])
    attribute_string = message['attribute']
    skill_string = message['skill']
    
    return rolld20(num_dice, attribute_value, skill_value, focus, attribute_string, skill_string)
    

def rollFromMessage(message):
    roll_pattern = r'^/roll\s+(\d+)\s+(\d+)\s+(\d+)\s*(0|1)?\s*(\w+)?\s*(\w+)?\s*$'
    match = re.match(roll_pattern, message)
    num_dice = int(match.group(1))
    attribute_value = int(match.group(2))
    skill_value = int(match.group(3))
    focus = int(match.group(4)) if match.group(4) is not None else 0
    attribute_string = match.group(5) if match.group(5) is not None else "default_attribute"
    skill_string = match.group(6) if match.group(6) is not None else "default_skill"
    
    return rolld20(num_dice, attribute_value, skill_value, focus, attribute_string, skill_string)

def rolld20(amount, attributeValue, skillValue, focus, attribute, skill):
    dice = []
    level = attributeValue+skillValue
    complication = 0
    successes = 0
    if focus == 1:
        focuslevel = skillValue
    else:
        focuslevel = 1
    for i in range(amount):
        score = random.randint(1,20)
        if score == 20:
            complication+=1
        if score <= focuslevel:
            successes+=2
        if score <= level:
            successes+=1
        dice.append(score)
        
    return returnRoll20Json(attributeValue, skillValue, focus, attribute, skill, dice, complication, successes)


def returnRoll20Json(attributeValue, skillValue, focus, attribute, skill, dice, complication, successes):
    data = {
        "type": "roll",
        "attributeValue": attributeValue,
        "skillValue": skillValue,
        "focus": bool(focus),
        "attribute": attribute,
        "skill": skill,
        "rolls": dice,
        "complication": complication,
        "successes": successes
    }
    return data
