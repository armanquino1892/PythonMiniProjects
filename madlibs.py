print ("Mad Libs Game!")
print ("Provide the answers from a series of questions to complete the sentence.\n")

Fname = input("Your first name: ")
FavFood = input("Favorite Fall food (plural): ")
FamousPerson = input("Famous person: ")
Verb = input("Present tense verb: ")
Adjective = input("Adjective: ")
PluralNoun = input("Plural Noun: ")
FamousSinger = input("Famous Singer: ")
Number = input("Number: ")
Animal = input("Animal(Plural): ")

textBody = ("""\n\nThe Best Town in the World Has a Fall Festival\n\nEvery year my town, {0}ville hosts the Fall Festival of {1}. 
It's a really fun time. Everyone comes to the {2} Park to play games, eat delicious food, 
see all the animals, and {3} in the last of the {4} weather. 
My favorite booth is the one that serves fried {5} on a stick!\n
This year, the Festival was extra special because there was a surprise guest; 
{6} came to play on the {0}ville Stage! It was the best concert ever. 
While {6} played, {7} birds sang along. 
But that wasn't half as amazing as the fact that the birds sang better than {6}. 
At the awards ceremony that evening, all of the {8} won blue ribbons for their singing. 
It was the best Fall Festival ever!""").format(Fname, FavFood, FamousPerson, Verb, Adjective, PluralNoun, FamousSinger, Number, Animal)

print(textBody)