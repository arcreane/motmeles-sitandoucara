#Loading required modules for the project
import string
import random
#from fpdf import FPDF

#Trial of the average version 15 x 7 - words are between 4 and 6 letters long
word_list = ["colère", "dallai", "marbre", "normes","solive","trésor"]
line = 15
column = 7

#random letter generator based on column and row
grid = [[random.choice(string.ascii_uppercase) for i in range(0,line)] for j in range(0,column)]
print("\n".join(map(lambda row: "  ".join(row), grid)))
print("Select Column : 7 \nSelect Line : 15")
