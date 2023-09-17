import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, exists
from sqlalchemy.exc import OperationalError
from sqlalchemy.inspection import inspect


from models.Attributes import Base as AttributesBase
from models.Skills import Base as SkillsBase
from models.Talents import Base as TalentsBase
from models.CharacterSheet import Base as CharacterSheetBase
from models.Equipment import Base as EquipmentBase
from models.Weapons import Base as WeaponsBase

from enums.WeaponType import WeaponType
from models.CharacterSheet import CharacterSheet
from models.Attributes import Attributes
from models.Talents import Talents
from models.Weapons import Weapons
from models.Equipment import Equipment
from models.Skills import Focus, Skills
from models.Truths import Truths

from decouple import config

def create_database():
    engine = create_engine(config('DATABASE_URL'))
    Session = sessionmaker(bind=engine)
    session = Session()
    inspector = inspect(engine)
    
    try:
        if not inspector.has_table("skills"):
            SkillsBase.metadata.create_all(engine)
        if not inspector.has_table("attributes"):
            AttributesBase.metadata.create_all(engine)
        if not inspector.has_table("talents"):
            TalentsBase.metadata.create_all(engine)
        if not inspector.has_table("character_sheet"):
            CharacterSheetBase.metadata.create_all(engine)
        if not inspector.has_table("equipment"):
            EquipmentBase.metadata.create_all(engine)
        if not inspector.has_table("weapons"):
            WeaponsBase.metadata.create_all(engine)
        print("Baza danych została zainicjowana.")
        
        #EDIGO
        exists_query = session.query(exists().where(CharacterSheet.name == "Egino, Who Sees the Hidden"))
        if not session.execute(exists_query).scalar():
            add_egino_character_sheet(session)
        
        character_sheet = session.query(CharacterSheet).filter_by(name = "Egino, Who Sees the Hidden").first()
        with open("edigo.json", "w") as json_file:
            json.dump(character_sheet.to_dict(), json_file)
            
        #AKUSSA
        exists_query = session.query(exists().where(CharacterSheet.name == "Akusaa"))
        if not session.execute(exists_query).scalar():
            add_akussa_character_sheet(session)
            
        character_sheet = session.query(CharacterSheet).filter_by(name = "Akusaa").first()
        with open("akussa.json", "w") as json_file:
            json.dump(character_sheet.to_dict(), json_file)

        
    except Exception as e:
        print(f"Błąd inicjalizacji bazy danych: {str(e)}")
    finally:
        session.close()
        
        
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
        
def add_akussa_character_sheet(session):
    try:


        weapons1 = Weapons(
            name = "Cudgel",
            weaponType = WeaponType.MELEE,
            range = "Reach 2",
            damage = 3,
            effects = "Stun"  
        )
        
        weapons2 = Weapons(
            name = "Sling",
            weaponType = WeaponType.THROWN,
            range = "Medium range",
            damage = 5,
            effects = "Stun, Innacurate, Subtle"
        )
        
        session.add_all([weapons1, weapons2])

        equipment1 = Equipment(
            name = "Plain Traveling Clothes",

        )
        
        equipment2 = Equipment(
            name = "Suit of Fine Clothing (stowed)"
        )
        
        equipment3 = Equipment(
            name = "Personal Library",
            description = "Choice tomes and reference materials."
        )
        
        equipment4 = Equipment(
            name = "Pet Mouse",
            description = "A small gray mouse named Ruhig, often hidden in Akusaa’s clothing."
        )
        
        equipment5 = Equipment(
            name = "Writing Materials and Tools",
            description = "Includes vellum or papyrus scrolls and books"
        )
        
        equipment6 = Equipment(
            name = "Stylus and Wax Tablet",
            description = "To make quick, impermanent notes, writers often employ a bronze stylus with a point on one end and a flat spade on the other, scribing into sheets of wax contained in a wooden or metal box. When a record is no longer needed, they use the stylus’s spade to wipe out the markings."
        )
            
        
        session.add_all([equipment1, equipment2, equipment3, equipment4, equipment5, equipment6])

        attributes = Attributes(
            agility=6,
            brawn=6,
            coordination=9,
            gravitas=9,
            insight=11,
            reason=11,
            will=10
        )
        session.add(attributes)

        skills = Skills(
            academia = 4,
            athletics = 0,
            crafting = 2,
            engineering = 2,
            fighting = 0,
            medicine = 2,
            observation = 3,
            persuasion = 2,
            resilience = 2,
            stealth = 0,
            survival = 0,
            tactics = 1
        )
        focus1 = Focus(
            skill_name = "academia",
            focus_name = "History"
        )
        
        focus2 = Focus(
            skill_name = "academia",
            focus_name = "Linguistics"
        )
        
        focus3 = Focus(
            skill_name = "academia",
            focus_name = "Religion"
        )
        focus4 = Focus(
            skill_name = "observation",
            focus_name = "Sight"
        )

        skills.focus.extend([focus1, focus2, focus3, focus4])
        session.add_all([skills, focus1, focus2, focus3, focus4])
        
        talents1 = Talents(
            name = "Applied Knowledge",
            description = "The knowledge you have accumulated gives you bursts of insight to deal with unexpected challenges. Once per scene, you may use Academia in place of another skill when you make a skill test, and you count as having an appropriate focus for that test."
        )
        
        talents2 = Talents(
            name = "Fade Away",
            description = "Once per scene as a minor action, you can generate 2 Threat for the GM’s Threat pool to slip from sight. If you do so, you cannot be the target of an attack (other than attacks with the Area damage effect) until the start of your next turn. If you are behind heavy cover (such as a large tree trunk or short stone wall) when you use this talent, you do not need to generate Threat."
        )
        
        talents3 = Talents(
            name = "Foreboding Survival",
            description = "Every so often, it feels like you narrowly avoid disaster thanks to an unknown guiding hand. How you avoid these fates is unknown, but bad luck seems to befall those around you. Once per session when you are dealt an injury, you may generate 3 Threat for the GM’s Threat pool in order to avoid suffering that injury. At the GM’s discretion, you may receive opportunities to avoid other misfortune as well in exchange for generating 3 Threat."
        )
        
        talents4 = Talents(
            name = "Vero Nihil Verius",
            description = "You have a keen eye that can spot the truth of a matter. Whenever you make a skill test to detect danger or hidden enemies, reduce the difficulty by 1."
        )
        
        talents5 = Talents(
            name = "Writ in Stone",
            description = "Your homeland is known for its long history, some of which is etched into stone on the faces of ancient walls. When you make an Academia-based test to recall a bit of relevant history or lore, you can re-roll any dice that fail to produce a success. "
        )
        
        session.add_all([talents1, talents2, talents3, talents4, talents5])
        
        truths1 = Truths(
            description = "Aegyptus"
        )
        
        truths2 = Truths(
            description = "Dreamwalker"
        )
        
        truths3 = Truths(
            description = "Seeking the Lost"
        )
        
        truths4 = Truths(
            description = "Student of the Occult"
        )
        
        truths5 = Truths(
            description = "I Have a Secret"
        )
        
        session.add_all([truths1, truths2, truths3, truths4, truths5])
        
        # Dodawanie arkusza postaci
        character_sheet = CharacterSheet(
            name="Akusaa",
            nickname = "Aldis",
            description="""Aegyptus Scholar and Occultist (Sage)
A highly knowledgeable linguist and occultist originally from Aegyptus, Akusaa is a woman in her early thirties who left that area under some duress. She was accused of stealing sacred tomes, a crime she did not actually commit, and is now an outcast from her homeland. She supports herself by taking work as a translator but is more interested in seeking out lore regarding Germanic mysticism in the frontier region, which is what has brought her to the Laurium area. She is on the hunt for mystically potent relics to investigate a theory she has on the ways the gods empower and guide favored mortals.
Akusaa is polite and well-spoken, though prone to conversing a touch too formally and made uncomfortable by some of the rugged and unfamiliar habits of those living in the frontier region. She prefers to adopt an androgynous appearance and feels uneasy when people focus on her femininity. 
She has had some small brushes with the supernatural, particularly in her dreams, which have taken her to strange and vividly inexplicable places. She is convinced the gods are active participants in mortal affairs, not always to mortals’ benefit. She finds conflict distasteful and seeks others to help her defend herself against threats that may arise in the course of her pursuits.""",
            actualStress=0,
            maxStress=11,
            actualInjuries=0,
            maxInjuries=3,
            armour=0,
            courage=2,
            languages=" Coptic, Aramaic, Celtic, Germanic, Greek, Latin, Punic",
            caste="Outcast",
            resources=0,
            background="Scholar",
            personalAgenda="Acquire an Object. An important item or relic has gone missing in the wilderness, and you aim to locate it.",
            characteristic="Dreamwalker. Sleep is a mere gateway, and even as a child you wandered the Dreamlands.",
            attributes=attributes,
            equipment=[equipment1, equipment2, equipment3, equipment4, equipment5, equipment6],
            weapons=[weapons1, weapons2],
            talents=[talents1, talents2, talents3, talents4, talents5],
            truths=[truths1, truths2, truths3, truths4, truths5],
            skills=skills
        )
        session.add(character_sheet)


        session.commit()
        print("Record Akussa added successfully")
    except Exception as e:
        print(f"Błąd dodawania rekordu Akussa: {str(e)}")
        session.rollback()

