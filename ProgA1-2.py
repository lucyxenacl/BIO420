#Programmed by Marisa Nickerson for Bioinformatics
# question number 2
#DNA sequence fragments after being digested with EcoRI

DNA = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
ecoRI = "GAATTC"
cut = DNA.find(ecoRI) + 1
fragment1 = cut
fragment2 = len(DNA)-cut
print "Length of sequence with cut is %s" % fragment1
print "Length is sequence without cut is %s" % fragment2