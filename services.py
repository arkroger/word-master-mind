from datetime import datetime
import logging
import random

from dao import word_dao, wordOfDay_dao
from app import checkWord, getResultJson
from exceptions import WordNotFound

class WordService:

    def __init__(self):        
        logging.info("WordService Instance")

    def validateWordMaster(self, word: str) -> str:
        wordExists = word_dao.wordExists(word)
        if not wordExists:
            raise WordNotFound  

        wordOfDay = self.findWordOfDay()        

        result = checkWord(word, wordOfDay)        

        return {'letters': getResultJson(result)}
    
    def findWordOfDay(self) -> str:    
        wordOfDay = wordOfDay_dao.findWordOfDay(datetime.now().date())
        if not wordOfDay:
            randomWord = self.randomWord()            
            wordOfDay_dao.save(randomWord, datetime.now().date())
            return randomWord
        else:
            return wordOfDay.word
    
    def randomWord(self) -> str:
        count = word_dao.count()
        intRandom = random.randint(1, count)
        return word_dao.getOffset(intRandom).word


word_service = WordService()