

from sqlalchemy import Column, String, Date
from database import Base

class Word(Base):
    __tablename__ = 'word'
    word = Column(String, primary_key=True)

    def __init__(self, word=None):
        self.word = word        

    def __repr__(self):
        return f'<Word {self.word!r}>'


class DailyWord(Base):
    __tablename__ = 'daily_word'
    date = Column(Date, primary_key=True)
    word = Column(String)

    def __init__(self, date=None, word=None):
        self.date = date
        self.word = word

    def __repr__(self):
        return f'<DailyWord {self.date} - {self.word!r}>'        