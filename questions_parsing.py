

def parsing_txt(path):
    question_list = list()

    try:
        with open("test.txt") as file_handler:
            for line in file_handler:
                print(line)
                if(line[1] == "R"):


    except IOError:
        print("An IOError has occurred!")


if __name__ == "__main__":
    parsing_txt("test.txt")
