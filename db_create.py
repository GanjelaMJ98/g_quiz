import sqlite3
conn = sqlite3.connect('G_QUIZ.sqlite')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE `right_t` (
	`right_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`right`	TEXT NOT NULL
) """)

cursor.execute("""CREATE TABLE `questions_t` (
	`question_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`question`	TEXT NOT NULL,
	`right_id`  INTEGER,
	FOREIGN KEY(`right_id`) REFERENCES `right_t`(`right_id`)
) """)


cursor.execute("""CREATE TABLE `answers_t` (
	`answer_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`answer`	TEXT NOT NULL,
	`question_id`  INTEGER,
	FOREIGN KEY(`question_id`) REFERENCES `question_t`(`question_id`)
)""")


conn.close()