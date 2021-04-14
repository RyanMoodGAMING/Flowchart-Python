# Writing / Working with text files.

text_file = open("olympic_games.txt", "w")
print("(Debug) olympic_games.txt has been crated/opended and is ready to be writen in.")
text_file.write("This is a list of each city that has held more than 1 Olympic Games. \n")
text_file.write("Athens ->      1908, 1948, 2012 \n")
text_file.write("London ->      1896, 2004, \n")
text_file.write("Paris ->       1948, 2012 \n")
text_file.write("Los Angeles -> 1932, 1984 \n")
text_file.write(" \n")
text_file.close()

text_file = open("olympic_games.txt", "r")
print("(Debug) olympic_games.txt has been opened in read mode.")
print(text_file.read())
text_file.close()

text_file = open("olympic_games.txt", "a")
text_file.write("Lake Placid -> 1932, 1980 \n")
text_file.write("Innsbruck ->   1964, 1976\n")
text_file.write("St Moritz ->   1928, 1948\n")

text_file.close()

##olymics = text_file.read()
##print(text_file.read().count("1"))
##print(olymics.count("1"))
##text_file.close()

