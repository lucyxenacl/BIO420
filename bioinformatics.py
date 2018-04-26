#programmed by marisa nickerson for bioinformatics
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