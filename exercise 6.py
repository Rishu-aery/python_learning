import random
comp=['Rock','Paper','Sicssor']
# print(comp_choice)

user_score=0
comp_score=0
i=1
while i<=6:
    comp_choice = random.choice(comp)
    print('*** ROUND',i,'***')
    user_choice = input('Press (r) for rock (p) for paper and (s) for scissor:')
    if user_choice == 'r':
        if comp_choice == 'Rock':
            print('Both choose rock, this is a tie')
            print('user_score=', user_score)
            print('comp_score=', comp_score)


        elif comp_choice == 'Paper':
            print('Comp_choice=', comp_choice, ',User_choice=', user_choice)
            comp_score += 1
            print('user_score=', user_score)
            print('comp_score=', comp_score)


        elif comp_choice == 'Sicssor':
            print('Comp_choice =', comp_choice, ',User_choice=', user_choice)
            user_score += 1
            print('user_score=', user_score)
            print('comp_score=', comp_score)


    elif user_choice == 'p':
        if comp_choice == 'Rock':
            print('Comp_choice =', comp_choice, ',User_choice=', user_choice)
            user_score += 1
            print('user_score=', user_score)
            print('comp_score=', comp_score)


        elif comp_choice == 'Paper':
            print('Both choose paper, this is a tie')
            print('user_score=', user_score)
            print('comp_score=', comp_score)


        elif comp_choice == 'Sicssor':
            print('Comp_choice =', comp_choice, ',User_choice=', user_choice)
            comp_score += 1
            print('user_score=', user_score)
            print('comp_score=', comp_score)


    elif user_choice == 's':
        if comp_choice == 'Rock':
            print('Comp_choice =', comp_choice, ',User_choice=', user_choice)
            comp_score += 1
            print('user_score=', user_score)
            print('comp_score=', comp_score)


        elif comp_choice == 'Paper':
            print('Comp_choice =', comp_choice, ',User_choice=', user_choice)
            user_score += 1
            print('user_score=', user_score)
            print('comp_score=', comp_score)


        elif comp_choice == 'Sicssor':
            print('Both choose scissor, this is a tie')
            print('user_score=', user_score)
            print('comp_score=', comp_score)

    else:
        print('Invalid Choice...please try again')
    i+=1
    print('\n' * 2)
    # choice=input('Do you want to play again, if yes press (y) if no press (n):')
    # if choice=='y':
    #     continue
    # elif choice=='n':
    #     exit()







