class HasReachedTheMessagesLimitException(Exception):
    def __init__(self):
        self.message = "Has reached the messages limit"
        super().__init__(self.message)