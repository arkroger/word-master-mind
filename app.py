import re
import random

WORDS = [
    'COISA',
    'UREIA',
    'BILIS',
    'NARIZ',
    'CAIXA',
    'CIRCO',
    'PILHA',
    'PALHA'
]

WRONG = 'WRONG'
RIGHT = 'RIGHT'
ANOTHER_POSITION = 'HALF'

def checkWord(word: str, randomWord: str) -> bool:
    characteres = list(word)
    result = []
    for index, char in enumerate(characteres):
        state = getState(char, index, word, randomWord)        
        result.append({'char': char, 'state': state})
    
    return result

def getState(char: str, index: int, word: str, randomWord: str) -> int:
    if isRight(char, index, randomWord):
        return RIGHT
    
    elif isAnotherPosition(char, word, randomWord):
        return ANOTHER_POSITION

    return WRONG

def isRight(char, index, randomWord) -> bool:
    return randomWord[index] == char

def isAnotherPosition(char, word, randomWord) -> bool:    
    if char in randomWord:        
        anotherPositions = ([m.start() for m in re.finditer(char, randomWord)])

        resultPositionsRight = []
        for position in anotherPositions:
            resultPositionsRight.append(isRight(char, position, word))
        
        allIsRight = all(resultPositionsRight)

        return not allIsRight   

    return False

def getResultJson(result):
    resultDict = {}    
    for index, item in enumerate(result):        
        resultDict[index] = {'state': item['state']}
    return resultDict
        

def showResult(result):    
    for char in result:        
        color = getColor(char['state'])
        print(color + char['char'] + " ", end =""),
    print("\r\n\033[0m")

def isSuccess(result):
    return all(map(lambda char: char['state'] == RIGHT, result))

def getColor(state):
    return {
        WRONG: "\033[91m",
        RIGHT: "\033[92m",
        ANOTHER_POSITION: "\033[93m"
    }.get(state, "\033[0m")    

def generateWord() -> str:
    return WORDS[random.randint(0, len(WORDS)-1)]

def newtry(word: str, randomWord: str) -> bool:
    result = checkWord(word, randomWord)
    showResult(result)
    return isSuccess(result)

def console():

    count = 1
    max = 5
    letters = 5
    print(f'Você tem {max} tentativas. Boa Sorte!')
    randomWord = generateWord()
    while count<=max:
        print("===================================")
        
        word = input(f'Tentativa {count}/{max}: Qual a palavra: ').upper()
        if len(word) == letters:
            success = newtry(word, randomWord)
            if success:
                print("\033[92mParabéns, palavra correta")
                count = max
            else:
                if count == max:
                    print(f'\033[91mVocê Perdeu!!!! A palavra correta era \033[93m{randomWord}')
                
            count=count+1
            
        else:
            print("Digite ao menos 5 letras")    


    #showResult(checkWord('TESTE', generateWord()))
    #showResult(checkWord('SESTE', generateWord()))
    #showResult(checkWord('ATEST', generateWord()))
    #showResult(checkWord('ACSTS', generateWord()))
    #showResult(checkWord('TEST', generateWord()))