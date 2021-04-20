import argparse
from unidecode import unidecode
import os
import csv

parser = argparse.ArgumentParser(description = "Remove unicode errors from file.")
parser.add_argument("file", metavar='f', type=str, help='The file for cleaning.')

args = parser.parse_args()
if len(args) < 1:
    print('No file specified')
#print(args)#

dirty_file = args.file

if not os.path.isfile(dirty_file):
    print('Specified file - {} - does not exist.'.format(dirty_file))

with open(dirty_file, encoding='utf-8') as dirty, open('cleaned_' + dirty_file, 'w') as clean:
    reader = csv.reader(dirty)
    writer = csv.writer(clean)
    for row in reader:
        print(row)
        writer.writerow(map(unidecode, row))
