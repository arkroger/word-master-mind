from datetime import date
import logging
from sqlalchemy import func
from models import Word, DailyWord
from database import db_session

class WordDAO:
    def __init__(self):
        logging.info("WordDAO Instance")

    def wordExists(self, word: str) -> bool:
        return Word.query.get(word) is not None

    def count(self) -> int:
        return db_session.query(func.count(Word.word)).scalar()

    def getOffset(self, offset: int) -> Word:        
        return Word.query.limit(0).offset(offset-1).first()
        
class WordOfDayDAO:
    def __init__(self):
        logging.info("WordOfDayDAO Instance")

    def findWordOfDay(self, date: date) -> DailyWord:
        return DailyWord.query.get(date)

    def save(self, word: str, date: date):        
        db_session.add(DailyWord(date=date,word=word))
        db_session.commit()        
        

word_dao = WordDAO()
wordOfDay_dao = WordOfDayDAO()