inputFile = "exampledata/aamutiline.fasta"
from moduls_folder.moduls import fastaread,GCcount


file = fastaread(inputFile)  

s= GCcount(inputFile)
print(file)
print(s)


