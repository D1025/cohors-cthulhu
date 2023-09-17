from enums.WeaponType import WeaponType
from models.CharacterSheet import CharacterSheet
from models.Attributes import Attributes
from models.Talents import Talents
from models.Weapons import Weapons
from models.Equipment import Equipment
from models.Skills import Focus, Skills
from models.Truths import Truths

def add_cossus_character_sheet(session):
    try:
        
        weapons1 = Weapons(
            name = "Gladius",
            weaponType = WeaponType.MELEE,
            range = "Reach 2",
            damage = 6,
            effects = "Piercing 1, Parrying"  
        )
        
        weapons2 = Weapons(
            name = "Pilum (3)",
            weaponType = WeaponType.THROWN,
            range = "Close range",
            damage = 6,
            effects = "Piercing 1, Special: On an effect [ ] result, after damage is dealt, the pilum is rendered unusable and if the target is carrying a shield, the pilum has embedded in the shield and lowers the shield’s Cover resistance by 1"
        )
        
        weapons3 = Weapons(
            name = "Large Shield",
            weaponType = WeaponType.MELEE,
            range = "Reach 1",
            damage = 5,
            effects = "Shield 3"  
        )
        
        session.add_all([weapons1, weapons2, weapons3])

        equipment1 = Equipment(
            name = "Hooded Cloak",
            description = "In addition to providing warmth and protection from the elements, this cloak has a deep hood that can help conceal a person’s identity. This cloak was looted on campaign and has become a favored and treasured item. It also serves as a good-luck charm. Once per adventure, you can invoke the good-luck charm the same way you would use a Fortune point."

        )
        
        equipment2 = Equipment(
            name = "Soldier’s Kit (skill kit)",
            description = "Contains spare clothing, food rations, a small spade and cooking vessel, and supplies for making camp. This kit contains enough supplies to provide 3 bonus Momentum for buying d20s."
        )
        
        session.add_all([equipment1, equipment2])

        attributes = Attributes(
            agility=9,
            brawn=11,
            coordination=9,
            gravitas=7,
            insight=10,
            reason=7,
            will=8
        )
        session.add(attributes)

        skills = Skills(
            academia = 0,
            athletics = 3,
            crafting = 0,
            engineering = 0,
            fighting = 3,
            medicine = 0,
            observation = 1,
            persuasion = 0,
            resilience = 4,
            stealth = 0,
            survival = 4,
            tactics = 2
        )
        focus1 = Focus(
            skill_name = "fighting",
            focus_name = "Melee Weapons"
        )
        
        focus2 = Focus(
            skill_name = "fighting",
            focus_name = "Thrown Weapons"
        )
        
        focus3 = Focus(
            skill_name = "resilience",
            focus_name = "Discipline"
        )
        focus4 = Focus(
            skill_name = "resilience",
            focus_name = "Fortitude"
        )

        skills.focus.extend([focus1, focus2, focus3, focus4])
        session.add_all([skills, focus1, focus2, focus3, focus4])
        
        talents1 = Talents(
            name = "Alea Lacta Est (“The die is cast”)",
            description = "Once per scene when an NPC suffers a complication, you can use this talent to increase the Threat cost to cancel the complication to 4 Threat."
        )
        
        talents2 = Talents(
            name = "Iron Hide",
            description = "You possess great fortitude and can bear horrible injuries without showing it. For the purpose of increasing your complication range, you ignore the first injury suffered. In addition, you are defeated after suffering 4 injuries instead of 3."
        )
        
        talents3 = Talents(
            name = "Legionary Training",
            description = "You may re-roll one d20 on any Fighting-based test you make with a spear, gladius, or pilum, though the second result stands."
        )
        
        talents4 = Talents(
            name = "Skin of Your Teeth",
            description = "You have a knack for (just barely) avoiding the worst injuries. Once per scene, you may spend a Fortune point when you are dealt an injury, in order to avoid suffering that injury."
        )
        
        session.add_all([talents1, talents2, talents3, talents4])
        
        truths1 = Truths(
            description = "Roman Citizen"
        )
        
        truths2 = Truths(
            description = "Campaign Veteran"
        )
        
        truths3 = Truths(
            description = "Sole Survivor"
        )
        
        truths4 = Truths(
            description = "I Have a Secret"
        )
        
        session.add_all([truths1, truths2, truths3, truths4])
        
        # Dodawanie arkusza postaci
        character_sheet = CharacterSheet(
            name="Cossus Atrius Thamugadus",
            nickname = "Jan",
            description="""North African Legionary (Soldier, Legionary Specialization)
Cossus, a soldier in his twenties, is a Roman citizen and legionary, though he is originally from northern Africa and descends from ancestors who fought on the side of Carthage in the Punic Wars. He knows of these legends and enjoys speaking of the military exploits of his ancestors, but he is nonetheless a proud Roman, seeing his service with the I Minerva Legion along the frontier as fostering the extension of a great civilization. He is technically attached to one of the barracks closer to Bonna, but his superiors gave him leave to attend to personal matters. He has been seeking information regarding his brother, a fellow soldier who was posted to the garrison in Laurium but has gone missing under suspicious circumstances.
Cossus is young but has seen some real action and has participated in some difficult battles, including one in which his squad was nearly entirely wiped out by Germanic rebels. The circumstances were such that he cannot blame the rebels for wanting to defend their territory, and the officer in charge made several blunders that led to the conflict, but nonetheless he is wary around more militant locals. He has a friendly demeanor and feels it is his job as a soldier to defend those who cannot protect themselves. He has sought to avoid involvement in any punitive actions taken by his legion against ordinary civilians.""",
            actualStress=0,
            maxStress=15,
            actualInjuries=0,
            maxInjuries=4,
            fatigue=0,
            armour=5,
            courage=0,
            languages="Latin, Greek (simple conversations), Punic",
            caste="Plebian",
            resources=2,
            background="Campaign Veteran",
            personalAgenda="Protect the Innocent. You use your strength to protect those who need it. When you perform actions to protect those who cannot defend themselves, you can re-roll 1d20 on opposed tests for which you are the reactive character.",
            characteristic="Sole Survivor. You didn’t get a good look at who— or what—slaughtered nearly every living thing in the settlement, but for reasons you can’t fathom, you alone were spared.",
            attributes=attributes,
            equipment=[equipment1, equipment2],
            weapons=[weapons1, weapons2],
            talents=[talents1, talents2, talents3, talents4],
            truths=[truths1, truths2, truths3, truths4],
            skills=skills
        )
        session.add(character_sheet)


        session.commit()
        print("Record Cossus added successfully")
    except Exception as e:
        print(f"Błąd dodawania rekordu Cossus: {str(e)}")
        session.rollback()