#!/usr/bin/python
# -*- coding: utf-8 -*-

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

#    cur.execute('''CREATE TABLE pet(name text,
#       age int,
#       breed_name text,
#       species_name text,
#       shelter_name text,
#       adpoted int);''')
#    print "Table created successfully"
#
#    conn.commit()

    new_list = []

    data = open('add.csv', 'r')
    for line in data:
        newline = line.replace(", ", ",")
        new_list.append(newline.title())

    my_list = []

    #reader = csv.DictReader(open('add.csv'), delimiter=',')
    reader = csv.DictReader(new_list, delimiter=',')
    for line in reader:
        #print line
        my_list.append(line)


    #print my_list

    for group in my_list:
        cur.execute("""INSERT INTO pet(name,age,adopted) VALUES (%(Name)s, %(Age)s, %(Adopted)s)""", group)
        con.commit()
        print group
    

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
