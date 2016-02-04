#Parsing and answer evaluation for Nudi HTML 
#Author: Ravichandra Enaganti (raviechandra@gmail.com)
#Date: 4-Feb-2016
#Versiob: 1.0

from HTMLParser import HTMLParser
import sys

nudi_answer = []


#Extracts the filled cells from raw HTML
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data != 'X' and data != '\n':
            nudi_answer.append(data+"\n")

#Check if got the key file, and the input file as arguments
if len(sys.argv) < 3:
    print "Incorrect usage!"
    print "Correct usage: python nudi.py key.txt input1.txt"
else:
    nudi_key = []
    with open(sys.argv[1], "r") as key_file:
        nudi_key = key_file.readlines()
    if len(nudi_key) == 0:
        print "Unable to read key from the file"
    else:
        with open(sys.argv[2], "r") as html_answer:
            parser = MyHTMLParser()
            parser.feed("".join(html_answer.readlines()))
            if len(nudi_answer) == 0:
                print "Unable to read answer from the input file"
            elif len(nudi_key) != len(nudi_answer):
                print "Incomplete answer!. Key length and answer length does not match"
                print "Expected length:", len(nudi_key), "found: ", len(nudi_answer)
            else:
                wrong = 0
                for i in range(len(nudi_key)):
                    if nudi_key[i] != nudi_answer[i]:
                        print "expected ", nudi_key[i], " found ", nudi_answer[i]
                        wrong += 1
                if wrong > 0:
                    print "Wrong answer, ", wrong, " incorrect answers"
                else:
                    print "All correct!"
