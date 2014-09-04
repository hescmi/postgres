#!/usr/bin/python

import psycopg2
import sys
import csv

con = None

try:
    con = psycopg2.connect(database='pets', user='postgres')
    cur = con.cursor()
    cur.execute('SELECT * from pet')
    ver = cur.fetchone()
    print ver

    new_list = []

    data = open('add.csv', 'r')
    for line in data:
        if ",," in line:
            line = line.replace(",,", ", Null,")
        elif " , " in line:
            line = line.replace(" , ", " 0,")
        newline = line.replace(", ", ",")
        new_list.append(newline.lower())

    my_list = []

    #reader = csv.DictReader(open('add.csv'), delimiter=',')
    reader = csv.DictReader(new_list, delimiter=',')
    for line in reader:
        #print line
        my_list.append(line)
        #print my_list

    for x in my_list:
        x['shelter name'] = x['shelter name'].upper()
        for y in ['name', 'breed name', 'species name']:
            x[y] = x[y].capitalize()

    my_list[2]['breed name'] = "Labrador Retriever"

    for group in my_list:
        cur.execute("""INSERT INTO pet(name,age,adopted,dead) VALUES (%(name)s, %(age)s, %(adopted)s, '0')""", group)
        con.commit()
        print group

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if con:
        con.close()
