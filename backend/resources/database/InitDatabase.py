from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from backend.python.models.BaseDatabase import Base

engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)


def create_database():
    engine = create_engine('sqlite:///mydatabase.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        Base.metadata.create_all(engine)
        print("Baza danych została zainicjowana.")
    except Exception as e:
        print(f"Błąd inicjalizacji bazy danych: {str(e)}")
    finally:
        session.close()