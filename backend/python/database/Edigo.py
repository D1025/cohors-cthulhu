from enums.WeaponType import WeaponType
from models.CharacterSheet import CharacterSheet
from models.Attributes import Attributes
from models.Talents import Talents
from models.Weapons import Weapons
from models.Equipment import Equipment
from models.Skills import Focus, Skills
from models.Truths import Truths

      
def add_egino_character_sheet(session):
    try:


        weapons1 = Weapons(
            name = "Dagger",
            weaponType = WeaponType.MELEE,
            damage = 2,
            effects = "Piercing 1, Hidden, Subtle"  
        )
        
        weapons2 = Weapons(
            name = "War Axe",
            weaponType = WeaponType.MELEE,
            damage = 4,
            effects = "Vicious"
        )
        
        session.add_all([weapons1, weapons2])

        equipment1 = Equipment(
            name = "Traveling Clothes",

        )
        
        equipment2 = Equipment(
            name = "Ritual Vestments"
        )
        
        equipment3 = Equipment(
            name = "Ritual Tools (skill kit)",
            description = "A kit of basic ritual tools contains an athame (ritual blade), incense, oil lamp, parchment paper, and ink. It includes the basic needs for any occultist who wishes to perform a ritual. This kit has enough supplies to provide 3 bonus Momentum for buying d20s."
        )
        
        equipment4 = Equipment(
            name = "Amulet of Tiwaz",
            description = "This heirloom once belonged to your ancestor, a famous tribal champion thought to be favored of Tiwaz. A character wearing an amulet may spend a Fortune point when they are targeted by a supernatural power, a spell, the evil eye, or a mental attack from a Mythos being or other supernatural creature. The amulet prevents the negative repercussions of the power, spell, or effect. The player then rolls 1 . If the result is an effect [ ], the amulet remains effective and can be used again; otherwise, it is rendered useless and must be replaced. This amulet also serves as a good-luck charm. Once per adventure, you can invoke the good-luck charm the same way you would use a Fortune point."
        )
        
        session.add_all([equipment1, equipment2, equipment3, equipment4])

        attributes = Attributes(
            agility=6,
            brawn=6,
            coordination=7,
            gravitas=11,
            insight=10,
            reason=10,
            will=11
        )
        session.add(attributes)

        skills = Skills(
            academia = 4,
            athletics = 0,
            crafting = 0,
            engineering = 0,
            fighting = 1,
            medicine = 2,
            observation = 2,
            persuasion = 5,
            resilience = 2,
            stealth = 1,
            survival = 0,
            tactics = 1
        )
        focus1 = Focus(
            skill_name = "academia",
            focus_name = "Religion"
        )
        
        focus2 = Focus(
            skill_name = "medicine",
            focus_name = "Field Treatment"
        )
        
        focus3 = Focus(
            skill_name = "persuation",
            focus_name = "Charm"
        )
        focus4 = Focus(
            skill_name = "persuation",
            focus_name = "Invocation"
        )
        
        focus5 = Focus(
            skill_name = "resilience",
            focus_name = "Fortitude"
        )
        skills.focus.extend([focus1, focus2, focus3, focus4, focus5])
        session.add_all([skills, focus1, focus2, focus3, focus4, focus5])
        
        talents1 = Talents(
            name = "Cool under Pressure (Medicine)",
            description = "When the situation gets tough, you take a deep breath and get the job done. When you make a Medicine-based test, you may spend a Fortune point to automatically pass that skill test, but you generate no Momentum"
        )
        
        talents2 = Talents(
            name = "Envy and Attention",
            description = "You hold considerable status in society, and while that comes with numerous benefits, it can cause challenges and complications to arise as well. You cannot move around unnoticed easily, and those who wish to see your downfall or to usurp your position conspire against you. The GM begins each adventure with +2 additional Threat to represent these potential problems. This talent cannot be retrained unless you lose your position as a member of the Noble caste."
        )
        
        talents3 = Talents(
            name = "Gods Guide You",
            description = "Witnessing the actions of fate and the gods in everything, you can guide the hands of your comrades toward the ordained order. You are a spellcaster (see Magic, page 28). Additionally, once per round as a reaction, you can generate 2 Threat for the GM’s Threat pool to assist an ally when that ally takes an Attack major action or makes a Reason + Academia test."
        )
        
        talents4 = Talents(
            name = "Silver Tongued",
            description = "You’re blessed with a silver tongue, allowing you to influence people to adopt your views quickly and effectively. When you attempt to sway someone to your way of thinking or haggle over the price of an item, you reduce the difficulty of your Persuasion-based test by 1."
        )
        
        talents5 = Talents(
            name = "Unyielding",
            description = " You are made of sterner stuff than most. You increase your maximum stress by +3 (included above)."
        )
        
        session.add_all([talents1, talents2, talents3, talents4, talents5])
        
        truths1 = Truths(
            description = "Germanic Tribe (Bructeri)"
        )
        
        truths2 = Truths(
            description = "Child of Greatness"
        )
        
        truths3 = Truths(
            description = "Tribal Elder (Politician)"
        )
        
        truths4 = Truths(
            description = "I Have a Secret"
        )
        
        session.add_all([truths1, truths2, truths3, truths4])
        
        # Dodawanie arkusza postaci
        character_sheet = CharacterSheet(
            name="Egino, Who Sees the Hidden",
            nickname = "dawid",
            description="""Germanic Priest of Tiwaz (Mystic)
Born of the Bructeri tribe, Egino is a true holy man who reveres many Germanic gods but is especially devoted to Tiwaz, known to some as Tyr. Egino is an older man, in his late fifties, and has served his people for his entire life, being descended from a noted lineage famed for its memorable Mystics, including Egino’s father. Egino has been recognized as an elder of his tribe and has been involved in a number of important meetings regarding its well-being. Recent years have been difficult for his people, as their villages have been afflicted with some sort of curse, which Egino has been desperate but so far unable to solve. He suspects some nefarious cult might be behind this misfortune.
Though he might have been more physically formidable in his youth, Egino has since become a somewhat frail older man, one who is not particularly well suited for battle or strife. Nevertheless, he has true mystical power achieved through prayers to his gods and the power of runecraft. Exhibiting a noble demeanor and being both well-spoken and persuasive, Egino has been able to solve most of the challenges facing him with the help of his quick wit and silver tongue. Versed in some of the healing arts, he has spent time easing the suffering of others, earning him more friends than enemies. He has come to the Laurium region hoping to find allies and information that might prevent the doom of his people.""",
            actualStress=0,
            maxStress=16,
            actualInjuries=0,
            maxInjuries=3,
            armour=1,
            courage=2,
            languages="Germanic, Celtic, Latin (just enough to get by)",
            caste="Noble",
            resources=2,
            background="Politician",
            personalAgenda="Claim Vengeance for a Wrongdoing. Someone has wronged you or someone you care about. You won’t rest until they meet justice.",
            characteristic="Child of Greatness. Growing up in the shadow of a significant forebear—a tribal champion—has put pressure on you to excel in order to meet your family’s lofty expectations.",
            attributes=attributes,
            equipment=[equipment1, equipment2, equipment3, equipment4],
            weapons=[weapons1, weapons2],
            talents=[talents1, talents2, talents3, talents4, talents5],
            truths=[truths1, truths2, truths3, truths4],
            skills=skills
        )
        session.add(character_sheet)


        session.commit()
        print("Record Egino added successfully")
    except Exception as e:
        print(f"Błąd dodawania rekordu Edigo: {str(e)}")
        session.rollback()