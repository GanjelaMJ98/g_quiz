import sqlite3
from API import Question
conn = sqlite3.connect('G_QUIZ.sqlite')
cursor = conn.cursor()

def addRight(answer):
    n = False
    for row in cursor.execute("SELECT * from right_t"):
        if row[1] == answer:
            n = True
    if n == False:
        cursor.execute("INSERT INTO right_t VALUES (NULL, '{0}')".format(answer))
        print("Added right Answer: ", answer)
        return 1
    else:
        print("Right Answer already exists")
        return 0

def addWrongAnswer(answers, question):
    for answer in answers:
        question_sql = "(SELECT question_id FROM questions_t WHERE question =  '{0}')".format(question)
        sql = "INSERT INTO answers_t VALUES (NULL, '{0}',{1})".format(answer, question_sql)
        cursor.execute(sql)


def addQuestion(question):
    addRight(question.right_answer)

    right_sql = "(SELECT right_id FROM right_t WHERE right =  '{0}')".format(question.right_answer)
    sql = "INSERT INTO questions_t VALUES (NULL, '{0}',{1})".format(question.question, right_sql)
    # print(sql)
    cursor.execute(sql)
    addWrongAnswer(question.answers_list, question.question)
    conn.commit()






if __name__ == "__main__":
    quest = Question()
    quest.add_question("ФамилияПаши")
    quest.add_answers_list(["Сидоров", "Иванов"])
    quest.add_wrong_answer("378")
    quest.add_right_answer("Ганжела")
    addQuestion(quest)
    conn.commit()