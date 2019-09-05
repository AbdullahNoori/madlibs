word_list = list()
def madlibs():
   first_primaryColor = input('Enter primaryColor: ')
   word_list.append(first_primaryColor)

   verb_1 = input('Enter a verb: ')
   word_list.append(verb_1)

   adjective_2 = input('Enter an adjective: ')
   word_list.append(adjective_2)

   verb_2 = input('Enter a verb: ')
   word_list.append(verb_2)

   noun_1 = input('Enter an noun_1: ')
   word_list.append(noun_1)

   Reptile = input('Enter a Reptile: ')
   word_list.append(Reptile)

   freind_name = input('Enter freind_name: ')
   word_list.append(freind_name)

   verb_3 = input("Enter verb_3")
   word_list.append(verb_3)

   plural_noun = input('Enter a plural_noun: ')
   word_list.append(plural_noun)

   secondary_color = input('Enter secondary_color')
   word_list.append(secondary_color)

   favorite_food = input('favorite_food: ')
   word_list.append(favorite_food)


   print("Have you ever heard of {} Beard the Pirate? His freinds called him Pete, for short. He would {} the {} Seas. When people saw Pete coming they'd sceam,{} or he'll put you in a {}." "Everyone feared Pirate Pete and his pet{}, named {}. He didn't want to be feaered though, he just wanted to {}. To keep people from being scared, they put a pair of {} on the flag. The brand new {} flag flew high in the sky, and everyone felt much better. Pirate Pete and his pet invited everyone on his ship to have{}.".format(first_primaryColor, verb_1, adjective_2, verb_2, noun_1, Reptile, freind_name, verb_3, plural_noun, secondary_color, favorite_food))
# random.shuffle(adjective_1,adjective_3,adjective_5)
madlibs()
