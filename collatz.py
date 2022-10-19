from random import randint
import matplotlib.pyplot as plt

class Collatz:
    def __init__(self, number):
        self.original = number
        self.current = None
        self.next_number = self.original
        self.last_number = self.current
        self.current = self.next_number
        self.last = None
        self.numbers = [number]
        self.step = len(self.numbers)
        self.solved = False
        self.isStopped = False
    
    def _showself(self):
        color = ""
        symbol = ""
        if self.current % 2:color = "\033[36m"
        else:color = "\033[32m"
        if self.current < self.last:symbol = "⬇️"
        else:symbol = "⬆️"
        print(f"{color}{self.current}\033[0m {symbol}")
        

    def next(self, verbose=True):
        if self.solved == True:
            self.current = 2
        self.isStopped = False
        self.last = self.current

        if self.current % 2 == False:
            next_number = self.current / 2
            self.current = next_number
        else:
            next_number = self.current * 3
            self.current = next_number+1
        if verbose==True:
            self._showself()

        self.numbers.append(self.current)
    
    def solve(self, verbose=True):
        if self.solved == False:
            while (self.current != 2):
                self.next(verbose)
            self.solved = True
        else:
            self.solved = False
            self.current = self.original
            self.solve()

    
    def showCurrent(self):
        print(self.current)

    def showLast(self):
        print(self.last)
    
    def showNext(self):
        current = self.current
        if self.current == 2:
            return 1
        elif current%2 == False:
            next_val = current / 2
            return next_val
        else:
            next_val = current * 3
            next_val = next_val + 1
            return next_val
    
    def back(self):
        if self.isStopped == False: 
            self.stopped = enumerate(self.numbers)
            self.isStopped = True
        for index, x in self.stopped:
            if self.current == x:
                self.current_index = int(index)
        self.last_index = self.current_index - 1
        self.current = self.stopped[self.last_index]

        self.current = self.last

class CollatzGraph:
    def __init__(self, integer_list:list):
        self.sequences = {}
        self.max = 1
        self.x_axis = []
        self.y_axis = []
        for index, x in enumerate(integer_list):
            y = int(x)
            colz = Collatz(y)
            colz.solve()
            self.sequences[f"{x}"] = colz.numbers
            for c in colz.numbers:
                z = int(c)
                if z > self.max:
                    self.max = z
        self.nseq = self.sequences.values()
        self.is100 = False
        while self.is100 == False:
            self.max+=1
            print(self.max)
            if self.is100%100 == True:
                continue
            else:
                self.is100 = True
        myx = 0
        while myx != self.max:
            self.x_axis.append(myx)
            self.y_axis.append(myx)
            myx = myx + 1
        self.colors = ["green", "red", "blue", "yellow", "black", "orange", "magenta"]
        self.colors_max = len(self.colors)
        self.seqmax = 1
        self.total_sequences = len(integer_list)
        for index, sequence in enumerate(self.nseq):
            ri = randint(0,9)
            xcolor = f"C{ri}"
            xax = []
            yax = []
            for line_index, number in enumerate(sequence):
                xax.append(line_index)
                yax.append(number)
            plt.plot(xax, yax, color=xcolor, linestyle='solid',marker=f'o', markerfacecolor=xcolor, markersize=5)

        plt.xlim = (0,self.seqmax)
        plt.ylim = (0, self.max)
        plt.xlabel("steps")
        plt.ylabel("values")
        plt.title("Collatz Conjecture Graph")
    
    def line(self):
        plt.show()
     
cgraph = CollatzGraph([112,134,5,8,78,70,71,72,73])
    

cgraph.line()        
