#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import codecs
from API import Question

def parsing_txt(path):
    question_list = list()
    try:
        with codecs.open('test.txt', 'r', 'utf-8') as file_handler:
            ques = Question()
            for line in file_handler:
                if(line[0] == "Q"):
                    ques.add_question(line[3:-2])
                if(line[0] == "A"):
                    ques.add_wrong_answer(line[3:-2])
                if(line[0] == "R"):
                    ques.add_right_answer(line[3:-2])
                if(line[0] == "_"):
                    question_list.append(ques)
                    ques = Question()
    except IOError:
        print("An IOError has occurred!")
    file_handler.close()
    return question_list


if __name__ == "__main__":
    l = parsing_txt("test.txt")
    print(l[0].print())
    print(l[0].is_right("2"))
    #print(l[1].print())
