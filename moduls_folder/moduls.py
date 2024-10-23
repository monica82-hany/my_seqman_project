def fastaread(fastafile):
    seqs={}
    with open (fastafile,"r") as f:
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

    return seqs

def GCcount(fastafile):
    gc_continer={}
    for header, seq in fastafile.items():
        gc_continer[header]=(seq.count("G")+ seq.count("c")/len(seq))
    return gc_continertiner

