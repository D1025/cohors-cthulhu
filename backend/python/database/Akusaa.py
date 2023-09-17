from enums.WeaponType import WeaponType
from models.CharacterSheet import CharacterSheet
from models.Attributes import Attributes
from models.Talents import Talents
from models.Weapons import Weapons
from models.Equipment import Equipment
from models.Skills import Focus, Skills
from models.Truths import Truths

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
            fatigue=0,
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