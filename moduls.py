def fastaread(fastafile):
    seqs={}
    with open (inputFile,"r") as f:
        header=None
        for line in f :
            line=line.strip()
            if len(line) == 0 :
                continue
            if line.startswith(">"):
                header=line[1:].split()[0]
                seqs[header]=""
            else:
                seqs[header]+=line

    return(seqs)