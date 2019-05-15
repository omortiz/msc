from chatterbot.logic import LogicAdapter

answer = 'Your benefits plan includes a package called the Child Benefits Grant Program. This program provides employees with a grant that undergraduate tuition expenses incurred by children of eligible employees for full-time study at any accredited college or university.'

class BenefitsAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['benefit', 'benefits', 'retirement', 'medical', 'dental', 'vision', 'insurance', 'tuition', 'help', 'pay']
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
        This is probably not the correct way but is sufficient for now.
        """
        input = input_statement.text.split()
        benefitsKewwords = ['benefit', 'benefits', 'medical', 'dental', 'vision', 'insurance', 'help', 'pay']

        wordsInList = 0
        for word in benefitsKewwords:
            if(word in input):
                wordsInList += 1

        confidence = 0
        if(wordsInList == 0):
            confidence = confidence
        else:
            confidence = (wordsInList/len(benefitsKewwords))

        """
        Set statement:
        We need to find an algorithm to set the  statement to an answer from a list of answers.
        As of now, this adapter only returns one answer if it can process the input statement
        """
        selected_statement = Statement(text=answer)
        selected_statement.confidence = confidence

        return selected_statement