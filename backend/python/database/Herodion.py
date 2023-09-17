from enums.WeaponType import WeaponType
from models.CharacterSheet import CharacterSheet
from models.Attributes import Attributes
from models.Talents import Talents
from models.Weapons import Weapons
from models.Equipment import Equipment
from models.Skills import Focus, Skills
from models.Truths import Truths

def add_herodion_character_sheet(session):
    try:


        weapons1 = Weapons(
            name = "Dagger",
            weaponType = WeaponType.MELEE,
            range = "Reach 1",
            damage = 3,
            effects = "Piercing 1, Hidden, Subtle"  
        )
        
        weapons2 = Weapons(
            name = "Sword",
            weaponType = WeaponType.MELEE,
            range = "Reach 2",
            damage = 5,
            effects = "Parrying"
        )
        
        session.add_all([weapons1, weapons2])

        equipment1 = Equipment(
            name = "Plain Traveling Clothes",

        )
        
        equipment2 = Equipment(
            name = "Suit of Fine Clothing"
        )
        
        equipment3 = Equipment(
            name = "Personal Library of Choice Reference Materials",
        )
        
        equipment4 = Equipment(
            name = "Pet Mouse",
            description = "A small gray mouse named Ruhig, often hidden in Akusaa’s clothing."
        )
        
        equipment5 = Equipment(
            name = "Satchel Containing Papers Including Identification for Checkpoints",
        )
        
        equipment6 = Equipment(
            name = "Papyrus Scroll (skill kit)",
            description = "Covering a range of material, scrolls can be found on nearly any subject from the history of the empire to the philosophical theories of an obscure thinker. This papyrus scroll contains enough knowledge to provide 3 bonus Momentum for buying d20s."
        )
            
        equipment7 = Equipment(
            name = "Lucky Charm",
            description = "This family heirloom is a small, egg-shaped ovoid of strange metal thought to have been blessed by Tyche. Once per adventure, you can invoke this good-luck charm the same way you would use a Fortune point.")
            
        
        session.add_all([equipment1, equipment2, equipment3, equipment4, equipment5, equipment6,equipment7])

        attributes = Attributes(
            agility=9,
            brawn=9,
            coordination=9,
            gravitas=10,
            insight=8,
            reason=8,
            will=8
        )
        session.add(attributes)

        skills = Skills(
            academia = 2,
            athletics = 2,
            crafting = 0,
            engineering = 0,
            fighting = 2,
            medicine = 0,
            observation = 4,
            persuasion = 3,
            resilience = 2,
            stealth = 3,
            survival = 0,
            tactics = 0
        )
        focus1 = Focus(
            skill_name = "academia",
            focus_name = "Finance"
        )
        
        focus2 = Focus(
            skill_name = "observation",
            focus_name = "Hearing"
        )
        
        focus3 = Focus(
            skill_name = "persuasion",
            focus_name = "Deception"
        )
        focus4 = Focus(
            skill_name = "persuasion",
            focus_name = "Negotiation"
        )
        focus5 = Focus(
            skill_name = "stealth",
            focus_name = "Sneak"
        )

        skills.focus.extend([focus1, focus2, focus3, focus4, focus5])
        session.add_all([skills, focus1, focus2, focus3, focus4, focus5])
        
        talents1 = Talents(
            name = "Bizarre Insight",
            description = " Your mind often shows you glimpses of things you couldn’t otherwise know. Once per scene, you may generate 1 Threat for the GM’s Threat pool to Obtain Information (ask the GM a question; see Common Uses for Momentum, page 17) without succeeding on a skill test."
        )
        
        talents2 = Talents(
            name = "Et Tu?",
            description = "You know the best method of attack is with an open hand in front and a dagger clenched behind your back. When you have made a successful Persuasion-based skill test to influence or deceive an enemy during a scene, if you make a successful surprise attack against them (see Surprise Attack, page 25), you may roll +1 on that attack for every effect [ ]; effects [ ] rolled on these additional dice do not themselves produce additional [ ]."
        )
        
        talents3 = Talents(
            name = "Practiced Listener",
            description = "Your homeland is rife with the great thinkers of the age, each with their own unique perspective on truth. Hearing their words in the streets of Greece and at the forum has given you a keen mind for insight. When performing an Insight-based test to determine the honesty of someone speaking, you may re-roll each d20 that fails to result in a success."
        )
        
        talents4 = Talents(
            name = "Suspicious",
            description = "You are suspicious of everything and everyone. You treat every suspicious character (or suspect thicket of brambles) like they might be a threat to your life. In the first round of combat, any hostile character who targets you with an attack before your turn increases the difficulty of their action by +1."
        )

        session.add_all([talents1, talents2, talents3, talents4])
        
        truths1 = Truths(
            description = "Greek"
        )
        
        truths2 = Truths(
            description = "Atlantean Ancestry"
        )
        
        truths3 = Truths(
            description = "Former Servant"
        )
        
        truths4 = Truths(
            description = "I Have a Secret"
        )
        
        session.add_all([truths1, truths2, truths3, truths4])
        
        # Dodawanie arkusza postaci
        character_sheet = CharacterSheet(
            name="Herodion",
            nickname = "Kaszydo",
            description="""Greek Courier (Schemer)
Herodion is a Greek man in his early thirties who has led an interesting but sometimes difficult life, having overcome a number of obstacles through his intelligence and determination. In his youth, he survived as an orphaned urchin in the streets and was later enslaved, but he was eventually able to purchase his freedom. His memories of his family are hazy, but he has held onto one of being told his ancestors once lived in Atlantis, before it fell
As a youth, he received enough education to prove his worth as a favored servant during his enslavement to a wealthy Roman family in Colonia. He attained a ready mastery of letters and numbers, eventually securing a position as a clerk. Since acquiring his freedom, he has more often worked as a courier and messenger. He is pragmatic and morally flexible, quite willing to take advantage of situations to ensure his survival. He is skilled with a blade and prepared to use it, though he prefers to talk his way out of trouble.
Key to turning his fortunes around in Colonia was garnering the attention of a secret patron who spotted his potential and recruited him to join a branch of the Fingers of Dawn. He is still a junior and largely uninformed member of this cult, but he is ready to answer the call when its people reach out to him. He is also eager to acquire any information that might be of use to them, in order to improve his standing. Many of his courier jobs are connected to this group, including a recent task to bring important missives to the town of Laurium.""",
            actualStress=0,
            maxStress=11,
            actualInjuries=0,
            maxInjuries=3,
            fatigue=0,
            armour=1,
            courage=0,
            languages="Greek, Latin (conversational)",
            caste="Plebian",
            resources=2,
            background="Urchin",
            personalAgenda="Uncover Secrets. You set out to learn the secrets of everyone you encounter.",
            characteristic=" Atlantean Ancestry. Your lineage traces back to the civilization of Atlantis, giving you certain exceptional insights and abilities. You might receive visions or experience inexplicable phenomena related to your Atlantean ties.",
            attributes=attributes,
            equipment=[equipment1, equipment2, equipment3, equipment4, equipment5, equipment6],
            weapons=[weapons1, weapons2],
            talents=[talents1, talents2, talents3, talents4],
            truths=[truths1, truths2, truths3, truths4],
            skills=skills
        )
        session.add(character_sheet)


        session.commit()
        print("Record Herodion added successfully")
    except Exception as e:
        print(f"Błąd dodawania rekordu Herodion: {str(e)}")
        session.rollback()