#Programmed by marisa nickerson for bioinformatics
import BIO420
# imports the function

print BIO420.PctOfProtein("msrslllrfllfllllpplp", ["L"])
print BIO420.PctOfProtein("MSRSLLLRFLLFLLLLPPLP", ["M"]) 
print BIO420.PctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) 
print BIO420.PctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['F', 's', 'L']) 
#prints the calculated percentage from the pieces of protein that were specified in the list