from enums.WeaponType import WeaponType
from models.CharacterSheet import CharacterSheet
from models.Attributes import Attributes
from models.Talents import Talents
from models.Weapons import Weapons
from models.Equipment import Equipment
from models.Skills import Focus, Skills
from models.Truths import Truths

def add_verodu_character_sheet(session):
    try:


        weapons1 = Weapons(
            name = "Daggers (2)",
            weaponType = WeaponType.MELEE,
            range = "Reach 1",
            damage = 4,
            effects = "Piearcing 1, Hidden, Subtle"  
        )
        
        weapons2 = Weapons(
            name = "Spatha",
            weaponType = WeaponType.MELEE,
            range = "Reach 2",
            damage = 7,
            effects = "Piercing 1"
        )
        
        weapons3 = Weapons(
            name = "Spear (gaff hook)",
            weaponType = WeaponType.MELEE,
            range = "Reach 3",
            damage = 6,
            effects = "Piercing 1"
        )
        
        weapons4 = Weapons(
            name = "Plumbata (3)",
            weaponType = WeaponType.THROWN,
            range = "Close range",
            damage = 4,
            effects = "Piercing 1"
        )
        
        session.add_all([weapons1, weapons2, weapons3, weapons4])

        equipment1 = Equipment(
            name = "Scoundrel’s Tools (skill kit)",
            description = "A bag of scoundrel’s tools contains lock picks, chisels, a short crowbar and hammer, coal dust, and oils and lubricants to assist in breaking into and entering a secure location. This kit comes with enough supplies to provide 3 bonus Momentum for buying d20s."

        )
        
        equipment2 = Equipment(
            name = "Bronze Relic",
            description = "You possess a peculiar family relic made of patinated bronze that seems to writhe and twist in an effort to escape the gaze of an observer. There is some strange power in it you have yet to discover."
        )
        
        
        session.add_all([equipment1, equipment2])

        attributes = Attributes(
            agility=11,
            brawn=11,
            coordination=8,
            gravitas=7,
            insight=11,
            reason=6,
            will=7
        )
        session.add(attributes)

        skills = Skills(
            academia = 0,
            athletics = 3,
            crafting = 0,
            engineering = 0,
            fighting = 2,
            medicine = 0,
            observation = 3,
            persuasion = 2,
            resilience = 1,
            stealth = 4,
            survival = 2,
            tactics = 0
        )
        focus1 = Focus(
            skill_name = "athletics",
            focus_name = "Lifting"
        )
        
        focus2 = Focus(
            skill_name = "fighting",
            focus_name = "Melee Weapons"
        )
        
        focus3 = Focus(
            skill_name = "stealth",
            focus_name = "Concealment"
        )
        focus4 = Focus(
            skill_name = "stealth",
            focus_name = "Lock Picking"
        )

        skills.focus.extend([focus1, focus2, focus3, focus4])
        session.add_all([skills, focus1, focus2, focus3, focus4])
        
        talents1 = Talents(
            name = "Call of the Reef",
            description = "The knowledge you have accumulated gives you bursts of insight to deal with unexpected challenges. Once per scene, you may use Academia in place of another skill when you make a skill test, and you count as having an appropriate focus for that test."
        )
        
        talents2 = Talents(
            name = "Fade Away",
            description = "Once per scene as a minor action, you can generate 2 Threat for the GM’s Threat pool in order to slip from sight. You cannot be the target of an attack (other than attacks with the Area damage effect) until the start of your next turn. If you are in heavy cover (such as a large tree trunk or short stone wall) when you use this talent, you do not need to generate Threat."
        )
        
        talents3 = Talents(
            name = "Cunning Fighter",
            description = "When you fight, you use every dirty trick at your disposal, from throwing sand in your opponent’s eyes to kicking them in the mentula. When an enemy attempts a melee attack against you and fails to inflict any stress, they lose their Guard (see Reach and Guard, page 25) on your next attack against them. If your next attack targeting that enemy is successful, the attack inflicts a number of extra equal to your Athletics skill."
        )
        
        talents4 = Talents(
            name = "Low Profile",
            description = "When you gain Cover resistance, increase the total resistance gained by +1."
        )
        
        talents5 = Talents(
            name = "Undergoing All Dangers",
            description = "Some claim that the people of Gaul burn down their own homes prior to migration to destroy any hope of returning home, compelling them to face every hardship. You begin the game with +1 Courage resistance (included above)."
        )
        
        session.add_all([talents1, talents2, talents3, talents4, talents5])
        
        truths1 = Truths(
            description = "Gaul"
        )
        
        truths2 = Truths(
            description = "Born of the Waters"
        )
        
        truths3 = Truths(
            description = "Smuggler"
        )
        
        truths4 = Truths(
            description = "I Have a Secret"
        )

        
        session.add_all([truths1, truths2, truths3, truths4])
        
        # Dodawanie arkusza postaci
        character_sheet = CharacterSheet(
            name="Verodu",
            nickname = "MrGreen",
            description="""Gaulish Smuggler and Bandit (Scoundrel)
Now in their late twenties, Verodu has never thought of themself as a criminal, but crime has nonetheless often been their only means of survival. Originally from one of the tribes of Gaul, Verodu has proven to be a capable smuggler, mercenary, and occasional bandit along the rivers of the Germanic frontier. They lived in Bonna for a time but recently decided to seek better fortunes in Laurium, where their unique skills might be of use. Verodu knows their way around boats and feels as comfortable on the deck of a riverboat as they are walking a forest path. They are quite willing to fight to protect what they have earned, and they aren’t above fighting dirty.
Verodu was raised as a girl but is adaptable, viewing themself as neither man nor woman. This has offered some complications in the patriarchal societies Verodu moves in, but Verodu is happy in their own skin, and feels no particular pressure to conform to any one gender. They often change their presentation based on how they wish to be perceived. For a great deal of Verodu’s life as a nonviolent criminal, being seen as a woman was difficult, so Verodu became comfortable at feigning being a man, including adopting facial makeup to compensate for a lack of mustache or beard, which is otherwise seen as a mark of maturity among male Gauls.""",
            actualStress=0,
            maxStress=12,
            actualInjuries=0,
            maxInjuries=3,
            fatigue=0,
            armour=4,
            courage=1,
            languages="Celtic (Gaulish), Germanic (rudimentary), Greek (conversational), Latin (few phrases)",
            caste="Outcast",
            resources=0,
            background="Criminal",
            personalAgenda="Accumulate Wealth. Everyone needs money. You just need it more than most. When you make a skill test to acquire wealth through treachery, stealth, or deception, you may re-roll a single d20 on the test.",
            characteristic="Born of the Waters. In eons past, your family consorted with pestilent beings who dwelled beneath the waves and foam. Though this corruption has waned, you can still feel it within you, an echo of Paleogene antiquity that calls to you when you sleep.",
            attributes=attributes,
            equipment=[equipment1, equipment2],
            weapons=[weapons1, weapons2, weapons3, weapons4],
            talents=[talents1, talents2, talents3, talents4, talents5],
            truths=[truths1, truths2, truths3, truths4],
            skills=skills
        )
        session.add(character_sheet)


        session.commit()
        print("Record Vedoru added successfully")
    except Exception as e:
        print(f"Błąd dodawania rekordu Vedoru: {str(e)}")
        session.rollback()