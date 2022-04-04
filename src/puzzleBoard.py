#import numpy as np
import copy
from priorityQueue import PriorityQueue

class PuzzleBoard:

    # Konstruktor dengan input berupa path testcase
    def __init__(self, path, cc):
        self.board = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
        if(cc == 1) :
            print("gajadi")
            #mat = np.arange(0,16)
            #np.random.shuffle(mat)
            #self.board = np.reshape(mat, (4, 4))
        else :
            f = open(path, "r")
            rowCount = 0
            for line in f:
                row = line.split()
                for i in range(4):
                    self.board[rowCount][i] = int(row[i])
                rowCount+=1

    # Mengubah board 2D jadi 1D
    def board1D(self):
        arr = [0 for i in range(16)]
        idx = 0

        for i in range(4):
            for j in range(4):
                arr[idx] = self.board[i][j]
                idx+=1

        return arr    

    # Mencari index slot yang kosong
    def findBlankIdx(self):
        for i in range(4) :
            for j in range(4) :
                if(self.board[i][j] == 16) :
                    return (i, j)

    # Menghitung total Kurang[i]
    def checkKurang(self):
        arr = self.board1D()
        kurang = [0 for i in range(16)]

        sum = 0
        for i in range(16):
            for j in range(i+1, 16):
                if(arr[i] > arr[j]):
                    sum+=1
                    kurang[int(arr[i])-1]+=1
        
        print("Pengecekan nilai fungsi Kurang[i] : ")
        for i in range(16):
            print("Kurang["+str(i+1)+"] =", kurang[i])
        print()
        print("ΣKurang[i] =", sum)

        return sum 

    # Mengecek posisi blank apakah di slot diarsir
    def checkX(self):
        (r, c) = self.findBlankIdx()
        x = (r+c) % 2

        print("X =", x)

        return x

    # Mengecek apakah puzzle solvable
    def isSolveable(self):
        Total = self.checkKurang() + self.checkX()
        
        print("Total (ΣKurang[i] + X) =", Total)
        print()

        return Total % 2 == 0

    # Memindahkan posisi blank ditambah dengan masukan units x dan y
    def move(self, x, y):
        (r, c) = self.findBlankIdx()

        if(r+x>=0 and r+x<4 and c+y>=0 and c+y<4):
            newPuzzle = copy.deepcopy(self)
            newPuzzle.board[r][c], newPuzzle.board[r+x][c+y] = newPuzzle.board[r+x][c+y], newPuzzle.board[r][c]
            return newPuzzle
        else:
            return None

    # Mencetak board
    def printBoard(self):
        for i in range(4):
            for j in range(4):
                if(self.board[i][j] == 16) :
                    print(" -", end="  ")
                elif(self.board[i][j] < 10) :
                    print("",self.board[i][j], end="  ")
                else :
                    print(self.board[i][j], end="  ")
            print()

