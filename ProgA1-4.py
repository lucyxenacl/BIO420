#Programmed by Marisa Nickerson for Bioinformatics
#DNA sequence is taken apart to view the two exon and one intron strands

DNA = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = DNA[0:64].upper()
exon2 = DNA[91:].upper()
intron = DNA[64:91].lower()
print "The first Exon is %s" % exon1
print "The second Exon is %s" % exon2
print "The Intron is %s" % intron