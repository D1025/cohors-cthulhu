from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


from models.Attributes import Base as AttributesBase
from models.Skills import Base as SkillsBase
from models.Talents import Base as TalentsBase
from models.CharacterSheet import Base as CharacterSheetBase
from models.Equipment import Base as EquipmentBase
from models.Weapons import Base as WeaponsBase

def create_database():
    engine = create_engine('sqlite:///mydatabase.sqlite')
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        SkillsBase.metadata.create_all(engine)
        AttributesBase.metadata.create_all(engine)
        TalentsBase.metadata.create_all(engine)
        CharacterSheetBase.metadata.create_all(engine)
        EquipmentBase.metadata.create_all(engine)
        WeaponsBase.metadata.create_all(engine)
        
        print("Baza danych została zainicjowana.")
    except Exception as e:
        print(f"Błąd inicjalizacji bazy danych: {str(e)}")
    finally:
        session.close()