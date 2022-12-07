# text = "Rakshith"

# print("The great " + text)
# print("The great {}".format(text))
# print(f"The great {text}")

Adjective = input('Adjective: ')
Food1 = input('Foods (plural): ')
Verb = input('Verb: ')
Saying = input('Saying: ')
Noun = input('Noun: ')
Food2 = input('Foods (plural): ')
Color = input('Color: ')
Vehicle = input('Something you would ride in: ')
Animal = input('Animal: ')
Person = input('Person: ')

madlib = f"Today I went to my favourite food Stand called the {Adjective} {Animal}. Unlike most food stands, \
they cook and prepare the food in a {Vehicle} while you eating. The best thing on the menu is the {Color} {Noun}.\
 Instead of routine flavours they fill the taco with {Food2}, cheese, and top it off with a salsa made from {Food1}. \
If that doesn't make your mouth water, then it's just like {Person} always says: \
{Saying}!"


print(madlib)
