#!/usr/bin/env python3
# anthor : wangrui

import os
import csv
import sqlite3

def question_csv_walk(basedir):
	for root, dirs, files in os.walk(basedir):
		for name in files:
			if name.endswith(".csv"):
				yield name

def store_data(cur, file):
	question_type = file.split(".")[0]
	with open(file, "r", encoding="gbk") as csv_file:
		reader = csv.reader(csv_file)
		headers = next(reader)
		i = 1
		for row in reader:
			data = [question_type, *row[:8]]
			data[1] = i
			if data[-2] != '':
				try:
					data[-2] = "ABCD".index(data[-2][0])
				except Exception as e:
					print(data)
					print(data[-2])
					raise e
				cur.execute("INSERT INTO question VALUES (?,?,?,?,?,?,?,?,?)", data)
				i+=1

def main():
	conn = sqlite3.connect("../questions.db")
	cur = conn.cursor()
	cur.execute("""
CREATE TABLE question (
        type VARCHAR NOT NULL,
        id INTEGER NOT NULL,
        description VARCHAR,
        "choice_0" VARCHAR NOT NULL,
        "choice_1" VARCHAR NOT NULL,
        "choice_2" VARCHAR,
        "choice_3" VARCHAR,
        answer INTEGER NOT NULL,
        analysis VARCHAR,
        PRIMARY KEY (id, type)
);
		""")
	for file in question_csv_walk("./"):
		store_data(cur, file)
	conn.commit()
	conn.close()


if __name__ == '__main__':
	main()
