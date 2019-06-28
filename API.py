class Question():
    """docstring"""

    def __init__(self):
        """Constructor"""
        self.question = ""
        self.answers_list = list()
        self.right_answer = ""

    def add_question(self, question):
        self.question = question
        """
        Stop the car
        """
    def add_answers_list(self, list):
        self.answers_list = list
        """
        Stop the car
        """

    def add_wrong_answer(self, wrong):
        self.answers_list.append(wrong)
        """
        Stop the car
        """
    def add_right_answer(self, right):
        self.right_answer = right
        """
        Stop the car
        """
    def print(self):
        print("Question: {0}\n".format(self.question))
        for i in range(len(self.answers_list)):
            print("{0}. {1}".format(i+1, self.answers_list[i]))
        print("{0}. {1}".format(i+1, self.right_answer))


if __name__ == "__main__":
    quest = Question()
    quest.add_question("Фамилия Паши?")
    quest.add_answers_list(["Сидоров", "Иванов"])
    quest.add_wrong_answer("378")
    quest.add_right_answer("Ганжела")
    quest.print()
