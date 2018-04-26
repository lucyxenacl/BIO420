# programmed by Marisa Nickerson 
# program finds fragment sites and returns where each site is
import re
DNA = open("dna.txt", "r")
for line in DNA:
# abcI = ANT/AAT N = any base
# abcII = GCRW/TG R= A or G W= A or T
    all_cuts = [0]
#add cut positions for abcI
    for match in re.finditer(r"A[ATGC]TAAT", line):
        all_cuts.append(match.start() + 3)

#add cut positions for abcII    
    for match in re.finditer(r"GC[AG][AT]TG", line):
         all_cuts.append(match.start() + 4)
sortedlist = sorted(all_cuts)
print sortedlist   
print "one fragment size is %s in length" % (sortedlist[1] - sortedlist[0])
print "one fragment size is %s in length" % (sortedlist[2] - sortedlist[1])
print "one fragment size is %s in length" % (sortedlist[3] - sortedlist[2])
print "one fragment size is %s in length" % (sortedlist[4] - sortedlist[3])
print "one fragment size is %s in length" % (len(line) - sortedlist[4] - 1)
