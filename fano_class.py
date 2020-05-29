import sys
import pandas as pd

class Fano:
    ''' Class for the Fano method representation '''
    def __init__(self):
        '''
        Initializes names, probabilities, partitions, codes
        '''
        self.names = None # Symbols
        self.probs = None # Probabilities
        self.code = [] # Fano code

    def coding(self):
        '''
        The main method which codes each element
        :return:
        '''

        for _ in range(len(self.names)):
            self.code.append('')

        def recurse(start, finish):
            '''
            Auxiliary recursion for function 'coding'
            :return:
            '''
            if finish - start == 1:
                return

            index = self.divide(self.probs[start: finish])
            for i in range(start, start + index):
                self.code[i] += '0'

            for i in range(start + index, finish):
                self.code[i] += '1'

            recurse(start, start + index)
            recurse(start + index, finish)

        recurse(0, len(self.names))

    @staticmethod
    def divide(probs):
        '''
        Return index in the list from which
        will be 1 (before this index will be 0).
        (Division the list in half)
        :return: int
        '''
        mid = sum(probs) / 2
        summ = probs[0]
        i = 1
        while summ + probs[i] < mid:
            summ += probs[i]
            i += 1
        # distance to the middle
        less = abs(mid - summ)  # lower number of letters
        more = abs(summ + probs[i] - mid)  # bigger number of letters

        # return the index of the element from which 1 starts
        if less < more:
            return i
        else:
            return i + 1

    def fano_len(self):
        '''
        Return average code length
        :return: float
        '''
        result = 0
        for i in range(len(self.probs)):
            result += self.probs[i] * len(self.code[i])
        return result

    def user_prob(self):
        '''
        Take user input with probabilities
        :return:
        '''
        while True:
            user = str(input('Enter probabilities divided by coma: '))
            if user == 'q':
                sys.exit()
            try:
                user = list(map(float, user.replace(' ', '').split(',')))
            except:
                continue
            if sum(sorted(user)) != 1 or sorted(user)[0] <= 0:
                continue
            else:
                break
        user.sort(reverse=True)
        names = []
        for i in range(1, len(user)+1):
            names.append('a' + str(i))

        self.names, self.probs = names, user

    def user_str(self):
        '''
        Take user input with sentence.
        :return:
        '''
        while True:
            user = str(input('Enter your sentence: '))
            if user == 'q':
                sys.exit()
            if user is None:
                continue
            if ' ' in user:
                while True:
                    spaces = str(input('Do you want to count spaces?(yes|no)'))
                    if spaces.lower() == 'yes' or spaces.lower() == 'y':
                        break
                    elif spaces.lower() == 'no' or spaces.lower() == 'n':
                        user = user.replace(' ', '')
                        break
            break

        length = len(user)
        result = {i: user.count(i)/length for i in set(user)}
        names, probs = [], []
        for name, prob in sorted(result.items(), key=lambda item: item[1], reverse=True):
            names.append(name)
            probs.append(prob)

        self.names, self.probs = names, probs

    def table(self):
        '''
        Create table which shows symbols, probabilities and Fano code.
        :return:
        '''
        diction = {'Symbol': self.names, 'Probability': self.probs, 'Code': self.code}
        df = pd.DataFrame(diction)
        df = df.set_index('Symbol')
        print(df)
