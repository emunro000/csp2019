def madlib():
    print('Welcome to Christmas with my family! ')
    print('I will ask you some questions, and then you can read the story you created!')
    
    # describing an aunt
    noun = raw_input("Type a women's name")
    verb = raw_input("Type a verb")
    adjective = raw_input("Type an adjective describing your aunt")
    
    #describing an uncle
    noun2 = raw_input("Type in a man's name")
    verb2 = raw_input("Type in another verb")
    adjective2 = raw_input("Type in another adjective")
    
    #describing you 
    adjective3 = raw_input("Type in another adjective")
    object1 = raw_input("Type in an object")
    
    print(' ')
    print('Merry Christmas! You walk into your aunt ' + noun + 's house. ')
    print('You see your aunt ' + noun + ' ' + verb +' to christmas music. How embarrasing for her.')
    print('Aunt ' + noun + ' has always been so ' + adjective + '.')
    print('Oh no...There is uncle ' + noun2 + ' ' + verb2 + '.')
    print('His sweater is so ' + adjective2 + '!')
    print('You walk over to your grandparents. Honestly thats the main reason your here. ')
    print('You give gramma a hug, and she says your too ' + adjective3 + '.')
    print('You know gramma, shes always been one to speak her mind!')
    print('Alright now you finally made your way to grandpa, and he says you look like a ' + object1 + '.')
    print('Well I hope you had a Merry Christmas. See ya next year!')
    
madlib()