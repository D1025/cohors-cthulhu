from enums.WeaponType import WeaponType
from models.CharacterSheet import CharacterSheet
from models.Attributes import Attributes
from models.Talents import Talents
from models.Weapons import Weapons
from models.Equipment import Equipment
from models.Skills import Focus, Skills

def add_egino_character_sheet(session):
    try:
        new_character = CharacterSheet(
            name="Egino, Who Sees the Hidden",
            description="""Germanic Priest of Tiwaz (Mystic)
            Born of the Bructeri tribe, Egino is a true holy man who reveres many Germanic gods but is especially devoted to Tiwaz, known to some as Tyr. Egino is an older man, in his late fifties, and has served his people for his entire life, being descended from a noted lineage famed for its memorable Mystics, including Egino’s father. Egino has been recognized as an elder of his tribe and has been involved in a number of important meetings regarding its well-being. Recent years have been difficult for his people, as their villages have been afflicted with some sort of curse, which Egino has been desperate but so far unable to solve. He suspects some nefarious cult might be behind this misfortune.
            Though he might have been more physically formidable in his youth, Egino has since become a somewhat frail older man, one who is not particularly well suited for battle or strife. Nevertheless, he has true mystical power achieved through prayers to his gods and the power of runecraft. Exhibiting a noble demeanor and being both well-spoken and persuasive, Egino has been able to solve most of the challenges facing him with the help of his quick wit and silver tongue. Versed in some of the healing arts, he has spent time easing the suffering of others, earning him more friends than enemies. He has come to the Laurium region hoping to find allies and information that might prevent the doom of his people.""",
            actualStress=0,
            maxStress=16,
            actualInjuries=0,
            maxInjuries=3,
            armour=1,
            courage=2,
            caste="Noble",
            resources=2,
            background="Politician",
            personalAgenda="Claim Vengeance for a Wrongdoing. Someone has wronged you or someone you care about. You won’t rest until they meet justice.",
            characteristic="Child of Greatness. Growing up in the shadow of a significant forebear—a tribal champion—has put pressure on you to excel in order to meet your family’s lofty expectations.",
        )

        attributes = Attributes(
            agility=6,
            brawn=6,
            coordination=7,
            gravitas=11,
            insight=10,
            reason=10,
            will=11
        )
        
        skills = Skills(
            academia=4,
            athletics=0,
            crafting=0,
            engineering=0,
            fighting=1,
            medicine=2,
            observation=2,
            persuasion=5,
            resilience=2,
            stealth=1,
            survival=0,
            tactics=1
        )

        focus1 = Focus(skill_name="academia", focus_name="Religion")
        focus2 = Focus(skill_name="medicine", focus_name="Field Treatment")
        focus3 = Focus(skill_name="persuasion", focus_name="Charm")
        focus4 = Focus(skill_name="persuasion", focus_name="Invocation")
        focus5 = Focus(skill_name="resilience", focus_name="Fortitude")

        skills.focus.extend([focus1, focus2, focus3, focus4, focus5])

        session.add(skills)
        session.add_all([focus1, focus2, focus3, focus4, focus5])

        talents = Talents(
            name = "Cool under Pressure (Medicine)",
            description = "When the situation gets tough, you take a deep breath and get the job done. When you make a Medicine-based test, you may spend a Fortune point to automatically pass that skill test, but you generate no Momentum"
        )

        weapons = Weapons(
            name = "Dagger",
            weaponType = WeaponType.Melee,
            range = "Close",
            damage = 2,
            effects = "Piercing 1, Hidden, Subtle"  
        )

        equipment = Equipment(
            name = "Traveling Clothes",
            description = "A sturdy cloak and boots, a belt with a pouch, and a set of common clothes."
        )

        session.add(new_character)
        session.add(attributes)
        session.add(talents)
        session.add(weapons)
        session.add(equipment)

        session.commit()
        print("Record Egino added successfully")
    except Exception as e:
        print(f"Błąd dodawania rekordu CharacterSheet i danych: {str(e)}")
        session.rollback()
