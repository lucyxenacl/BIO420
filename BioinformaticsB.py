def atContent(sequence):
    allCaps = sequence.upper()
    aN = allCaps.count('A')
    tN = allCaps.count('T')
    result = (aN + tN) / float(len(allCaps))
    return result
    
def extractExon(dna, start, stop):
    exon = dna[start-1:stop]
    return exon
    