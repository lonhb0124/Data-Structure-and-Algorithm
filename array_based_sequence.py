class GameEntry:


    def __init__(self, name, score):

        self._name = name
        self._score = score

    def get_name(self):
        return self._name
    
    def get_score(self):
        return self._score
    
    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)

class Scoreboard:

    def __init__(self, capacity = 10):

        self._board = [None] * capacity
        self._n = 0
    
    def __getitem__(self, k):
        
        return self._board[k]

    def __str__(self):
        
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):

        score = entry.get_score()

        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1
        
        j = self._n - 1
        # Adding an Entry
        while j > 0 and self._board[j - 1].get_score() < score:
            self._board[j] = self._board[j - 1]                 # Shift Etnry
            j -= 1
        self._board[j] = entry

if __name__ == "__main__":
    """
    A = [GameEntry("Mike", 1105)]
    A.append(GameEntry("Rob", 750))
    A.append(GameEntry("Paul", 720))
    A.append(GameEntry("Anna", 660))
    A.append(GameEntry("Rose", 590))
    A.append(GameEntry("Jack", 510))
    """
    A = [GameEntry("Mike", 1105)]
    A.append(GameEntry("Jack", 510))
    A.append(GameEntry("Anna", 660))
    A.append(GameEntry("Rob", 750))
    A.append(GameEntry("Rose", 590))
    A.append(GameEntry("Paul", 720))

    #for i in range(len(A)):
    #    print(A[i].__str__())


    B = Scoreboard()
    for j in range(len(A)):
        B.add(A[j])


    print(B.__str__())
