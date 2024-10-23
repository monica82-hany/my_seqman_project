inputFile = "exampledata/aamutiline.fasta"
from mod_folder.moduls import fastaread,GCcount


file = fastaread(inputFile)  

s= Count_GC_fun(file)
print(file)
print(s)

l
