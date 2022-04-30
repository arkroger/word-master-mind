class WordNotFound(Exception):
    def __init__(self, message="Word Not Found"):        
        self.message = message
        super().__init__(self.message)