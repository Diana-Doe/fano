class Fano:
    def __init__(self):
        '''
        Initializes names, probabilities, partitions, codes
        '''
        self.names = None # Букви
        self.probs = None # Імовірність появи букв
        self.breaking = None # Розбиття множини букв
        self.code = None # Елементраний код

    def user_prob(self):
        '''
        Take user input with probabilities
        :return:
        '''
        while True:
            user = str(input('Enter probabilities divided by coma: '))
            if user == 'q':
                return
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
                return
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
