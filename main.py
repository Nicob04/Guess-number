#GUESS THE NUMBER GAME IN PYTHON
from genera import rand
import random 
def main():
    print('ciao')
    print('Rule:\nGuess the number with wax 10 attemps')
    print('The rage in 0-100')
    print('GOOD LUCK')
    i = 0
    trovato = False
    n = rand()
    #print(n)
    while(i < 10):
        print('guess the number:')
        ans = int(input())
        if(ans > n):
            print('insert a low number')
            i+=1
            print('you have',10-i,'times left')
        if(ans < n):
            print('insert a upper number')    
            i+=1
            print('you have',10-i,'times left')
        if (ans == n):
            i+=1
            trovato = True
            break   
        
    if(trovato is True):
        print('CONGRATULATION YOU FOUND THE RIGTH NUMBER , WITH ' ,i,'ATTEMPS') 
    else:    
        print('you do not guess the rigth number sorry \nThe ritgh number was', n)

    
#richiamo main
if __name__ == "__main__":
    main()