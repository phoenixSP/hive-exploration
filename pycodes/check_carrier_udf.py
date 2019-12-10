#!/usr/bin/env python
import sys
import string
import csv


while True:
    line = sys.stdin.readline()
    if not line:
        break
    
    line = string.strip(line, "\n ")
    year_string = line[line.rfind("(")+1:line.rfind(")")].strip()
    print(year_string)
    start_year, end_year = string.split(year_string, "-")
    start_year = start_year.strip()
    end_year = end_year.strip() 
    if end_year == '':
	end_year = '2019'
    print "\t".join([start_year, end_year])
