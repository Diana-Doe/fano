import sys
from fano_class import Fano

if __name__ == "__main__":
    print("This program can convert your sentence or list of probabilities into Fano code.\n" +
           "You can enter either a sentence with any symbols and it will count probabilities \n" +
           "by itself, or just probabilities.\n" +
           "If you want to stop the program enter 'q'.\n")
    while True:
        fano = Fano()
        while True:
            user = input('What would you like to enter: sentence(1) or probabilities(2)? ')
            if user == '1':
                fano.user_str()
                break
            elif user == '2':
                fano.user_prob()
                break
            elif user == 'q':
                sys.exit()
        fano.coding()
        fano.table()
        print('Average code length: {}'.format(fano.fano_len()))
        while True:
            user = input('Would you like to continue?(yes/no)')
            if user.lower() == 'yes' or user.lower() == 'y':
                break
            elif user.lower() == 'no' or user.lower() == 'n':
                sys.exit()

