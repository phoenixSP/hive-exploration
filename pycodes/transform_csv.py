# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 15:59:17 2019

@author: shrey
"""

import sys
import string
import csv

with open('L_CARRIER_HISTORY.csv') as csv_file, open('test.csv', mode = 'w') as write_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_writer = csv.writer(write_file, delimiter = ',')
    line_count = 0
    for row in csv_reader:
	if line_count == 0: 
	    csv_writer.writerow(['Code', 'Description', 'Start_year', 'End_year'])
	    line_count += 1
	else:
            description = string.strip(row[1], "\n ")
            print 'This is des' + description
            year_string = description[description.rfind("(")+1:description.rfind(")")].strip()
            print line_count
            print year_string
            start_year, end_year = string.split(year_string, "-")
            start_year = start_year.strip()
            end_year = end_year.strip() 
            if end_year == '':
	        end_year = '2019'

            csv_writer.writerow([row[0], row[1],start_year, end_year])
	    print 'row1' +row[0]+'  row2   '+row[1]
	    line_count += 1