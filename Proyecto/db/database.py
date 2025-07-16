from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._setup()
        return cls._instance

    def _setup(self):
        # Path to books.db (one level up from this script)
        db_path = Path(__file__).resolve().parent.parent / "data_archibox.db"
        self.engine = create_engine(f"sqlite:///{db_path}", echo=False)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def get_session(self):
        return self.session

    def commit(self):
        self.session.commit()

    def close(self):
        self.session.close()
