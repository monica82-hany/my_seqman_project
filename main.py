inputFile = "exampledata/aamutiline.fasta"
# from moduls_folder.moduls import fastaread,GCcount

 
seqs={}
with open (inputFile,"r") as f:
        header=None
        for line in f :
            line=line.strip()
            if len(line) == 0 :
                continue
            if line.startswith(">"):
                header=line[1:]
                header=line.split()[0]
                seqs[header]=""
                print(line)
            else:
                seqs[header]+=line
# file = fastaread(inputFile)  

# s= GCcount(inputFile)
# print(file)
# print(s)


