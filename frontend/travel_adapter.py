from chatterbot.logic import LogicAdapter

answer = 'Employees are given a specific amount of hours for paid time off using a traditional vacation, holiday and sick time.'

class TravelAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['time off', 'sick time', 'vacation', 'travel', 'traveling']
        input = statement.text.split()

        for word in input:
            if word in words:
                return True
        return False
    def process(self, input_statement, additional_response_selection_parameters):
        import random
        from chatterbot.conversation import Statement

        """
        Calculate confidence:
        """
        input = input_statement.text.split()
        travelKewwords = ['time off', 'sick time', 'vacation', 'travel', 'traveling']

        wordsInList = 0
        for word in travelKewwords:
            if(word in input):
                wordsInList += 1

        confidence = 0
        if(wordsInList == 0):
            confidence = confidence
        else:
            confidence = (wordsInList/len(travelKewwords))

        """
        Set statement:
        We need to find an algorithm to set the  statement to an answer from a list of answers.
        As of now, this adapter only returns one answer if it can process the input statement
        """
        selected_statement = Statement(text=answer)
        selected_statement.confidence = confidence

        return selected_statement