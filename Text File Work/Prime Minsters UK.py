# (7) Prime Miniers of the UK

textFile = open("UKPrimeMiniser.txt", "w")

#print("(Debug) Writing to UKPrimeMinister.txt") # Debug --> Tells your if the code gets to this point

textFile.write("Last seven UK Prime Minisers and term of office. \n")
textFile.write("\n")
textFile.write("Boris Johnson    ->   2019 - current \n")
textFile.write("Theresa May      ->   2016 - 2019 \n")
textFile.write("David Cameron    ->   2010 - 2016 \n")
textFile.write("Gordon Brown     ->   2007 - 2010 \n")
textFile.write("Tony Blair       ->   1997 - 2007 \n")
textFile.write("John Major       ->   1990 - 1997 \n")
textFile.write("Mararet Thatcher ->   1979 - 1990 \n")
#print("(Debug) Writen to UKPrimeMinister.txt") # Debug --> Tells your if the code gets to this point
textFile.close()

textFile = open("UKPrimeMiniser.txt", "r")
#print("(Debug) Reading to UKPrimeMinister.txt") # Debug --> Tells your if the code gets to this point
print(textFile.read())
textFile.close()
