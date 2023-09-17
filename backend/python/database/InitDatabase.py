import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, exists
from sqlalchemy.inspection import inspect


from models.Attributes import Base as AttributesBase
from models.Skills import Base as SkillsBase
from models.Talents import Base as TalentsBase
from models.CharacterSheet import Base as CharacterSheetBase
from models.Equipment import Base as EquipmentBase
from models.Weapons import Base as WeaponsBase

from models.CharacterSheet import CharacterSheet

from database.Akusaa import add_akussa_character_sheet
from database.Edigo import add_egino_character_sheet
from database.Cossus import add_cossus_character_sheet
from database.Herodion import add_herodion_character_sheet
from database.Verodu import add_verodu_character_sheet

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
            
        #COSSUS
        exists_query = session.query(exists().where(CharacterSheet.name == "Cossus Atrius Thamugadus"))
        if not session.execute(exists_query).scalar():
            add_cossus_character_sheet(session)
            
        character_sheet = session.query(CharacterSheet).filter_by(name = "Cossus Atrius Thamugadus").first()
        with open("cossus.json", "w") as json_file:
            json.dump(character_sheet.to_dict(), json_file)
            
        #HERODION
        exists_query = session.query(exists().where(CharacterSheet.name == "Herodion"))
        if not session.execute(exists_query).scalar():
            add_herodion_character_sheet(session)
            
        character_sheet = session.query(CharacterSheet).filter_by(name = "Herodion").first()
        with open("herodion.json", "w") as json_file:
            json.dump(character_sheet.to_dict(), json_file)
            
        #VERODU
        exists_query = session.query(exists().where(CharacterSheet.name == "Verodu"))
        if not session.execute(exists_query).scalar():
            add_verodu_character_sheet(session)
            
        character_sheet = session.query(CharacterSheet).filter_by(name = "Verodu").first()
        with open("verodu.json", "w") as json_file:
            json.dump(character_sheet.to_dict(), json_file)


        
    except Exception as e:
        print(f"Błąd inicjalizacji bazy danych: {str(e)}")
    finally:
        session.close()
        