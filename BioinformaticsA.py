def atContent(sequence):
    allCaps = sequence.upper()
    aN = allCaps.count('A')
    tN = allCaps.count('T')
    result = (aN + tN) / float(len(allCaps))
    return result
    
def HighAT(result):
    if result > 0.65:
        return(True)
    else:
        return(False)
        
def MedAT(result):
    if result >= 0.45 or result <= 0.65:
        return(True)
    else:
        return(False)
        
def LowAT(result):
    if result < 0.45:
        return(True)
    else:
        return(False)
        