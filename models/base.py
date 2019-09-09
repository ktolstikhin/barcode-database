from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base


ModelBase = declarative_base()


def session(filename):
    engine = create_engine(f'sqlite:///{filename}')
    ModelBase.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    return Session()

