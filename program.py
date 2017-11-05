import pandas as pd #a library for data reading
import string # a string library

class QA(object):
    """ QA class is to read the FAQ files and find the answer 
    """
    def __init__(self):
        """ initilization of the class
        :TODOS:
            :TODO: make it general for other files as well
        """
        self.data = self.read_prepare_data("Grad-Data-FAQ.xlsx")
    
    def read_prepare_data(self,filename):
        """ Read file and prepare the file
        :takes:
            :filename: the name of the file to read -> str
        :returns: file in memory -> dict
        """
        return pd.read_excel(filename)
    
    def get_answer(self,q):
        """ Find the answer by searching the question on the data
        :takes:
            :q: question -> str
        :returns: the answer -> str
        Algo
        the algo counts the appereance the words on q throughout the file and
        return the most related question's answer
        :TODOS: 
            :TODO: Remove it and use Guassian Classifier  
        """
        i = -1
        max_sim = 0
        q = q.split()
        for index, question in enumerate(self.data["Question"]):
            question = question.split()
            local_max =sum([1 for word in q if word in question]) # calculate similarity
            if local_max > max_sim:
                i = index
                max_sim = local_max
        # if max_sim is 0, then cannot answer!
        return self.data["Answer"][i] if max_sim>0 else "I cannot answer that question at that moment"

class Bot(object):

    def get_question(self):
        """ Gets the question and clean it
        :return: question(str)
        """
        q = input()
        if q == "exit":
            return q
        return "".join([i for i in q if not i in string.punctuation])

    def run(self):
        """ The main partf of the class. Basically, it runs the bot
        return: None
        """
        def intro():
            """ A function to write Introduction statements
            """
            print ("METU_NCC QR: Hello I am METU NCC Question Responder(METU_NCC QR)")
            print ("METU_NCC QR: If you are done with me, type \"exit\"")
            print("METU_NCC QR: How can I help you?") 
        qa = QA()
        intro()
        while True:
            print("Me: ", end="")
            q = self.get_question()
            if q == "exit":
                break
            print("METU NCC QR: ", qa.get_answer(q))
        print("METU NCC QR: Goodbye")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
