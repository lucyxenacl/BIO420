#Programmed by Marisa Nickerson
#4/24/2018
#For Bioinformtics
#Code translates a DNA sequence into codon strings and uses the amino acid gencode dictionary to read and return a letter 
gencode = {
 'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
 'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
 'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
 'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
 'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
 
#gencode was given with the assignment

def translate_dna(sequence):
    codons=[]
    #codons hold codons
    amninoacid=[]
    #aminocid holds the amino acids sequences from the dictionary
    codons=[sequence[i:i+3] for i in range(0, len(sequence), 3)]
    #splits the string into codons to be read by the program in threes 
    
    for a in codons:
        amninoacid.append(gencode.get(a))
    return amninoacid
    
#a in loop gets amino acids sequences from the dictionary


# line 1 defines the function
# line 2 changes the protein to uppercase so that the code isn't case sensitive
# aa is amino acid and that is changed to upper from the list defined by codes
# c is the count of codes within the protein 
# the program should return the percentage of the list that was in the protein sequence
def PctOfProtein(Protein, codes):
    Protein=Protein.upper()
    c=0 
    for aa in codes:
        aa=aa.upper()
        c = c+Protein.count(aa)
    return(c/float(len(Protein))*100)
    
#codes and counts AT content
def atContent(sequence):
    allCaps = sequence.upper()
    aN = allCaps.count('A')
    tN = allCaps.count('T')
    result = (aN + tN) / float(len(allCaps))
    return result
    
#returns high AT content    
def HighAT(result):
    if result > 0.65:
        return(True)
    else:
        return(False)
 
#Returns med AT content      
def MedAT(result):
    if result >= 0.45 or result <= 0.65:
        return(True)
    else:
        return(False)
        
#returns low AT content
def LowAT(result):
    if result < 0.45:
        return(True)
    else:
        return(False)
    
def extractExon(dna, start, stop):
    exon = dna[start-1:stop]
    return exon