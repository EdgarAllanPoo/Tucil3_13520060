# Nama  : Rheza Rizqullah Ecaldy
# NIM   : 13520060
# Kelas : K03

import time
import argparse
from bnbFunction import checkFungsiG
from bnbFunction import isSolution
from bnbFunction import findSolutionRoute
from puzzleBoard import PuzzleBoard
from priorityQueue import PriorityQueue
from searchState import SearchState

# Main Menu
print("SELAMAT DATANG DI 15 PUZZLE SOLVER REZMAN")
print()
print("Terdapat 2 tipe input: ")
print("1. Random generated matrix")
print("2. Input file txt")
print()
choice = int(input("Tipe input pilihan anda: "))
print()

if (choice == 1) :
    #root = SearchState(PuzzleBoard("../test/", 1), None, "", 0)
    print("gajadi")
elif (choice == 2) :    
    # Input nama file
    filename = input("Masukkan nama file: ")
    print()

    # Menginisiasi startNode/root
    root = SearchState(PuzzleBoard("../test/" + filename, 2), None, "", 0)
else :
    print("Error gan")
    exit()

# mencetak hasil input
print("Puzzle :")
root.root.printBoard()
print()

# mengecek apakah puzzle bisa diselesaikan
if(not root.root.isSolveable()):
    print("Puzzle tidak bisa diselesaikan.")
    exit()

print("Puzzle bisa diselesaikan.")
print()

# Menetapkan fungsi g(i) sebagai fungsi prioritas dari priority queue
costFunction = checkFungsiG

# Menginisiasi priority queue
pq = PriorityQueue(lambda x,y : x.level + costFunction(x.root) <= y.level + costFunction(y.root))

# Memasukkan root puzzle
pq.push(root)

# Menginisiasi jenis moves yang bisa dilakukan
movesUnits = [(-1,0), (0,-1), (1,0), (0,1)]
movesNames = ["Up", "Left", "Down", "Right"]

# Menginisisasi perhitungan node dan state solusi
solutionState = None
nodeCount = 1

# Menghitung waktu mulai
timeStart = time.process_time_ns()

# Algoritma branch and bound untuk mencari solusi puzzle
while(not pq.isEmpty()):
    
    # Menetapkan elemen pertama pada priority queue menjadi state yang ditelusuri
    current = pq.first()
    pq.pop()

    # Mengecek apakah state yang ditelusuri sudah merupakan solusi
    if(isSolution(current.root)):
        solutionState = current
        break

    # Menelusuri semua gerakan yang mungkin
    for i, (dr, dc) in enumerate(movesUnits):
        # Mengecek apakah gerakan kebalikan dari gerakan sebelumnya
        if(movesNames[(i+2)%4] != current.prevMove):
            # Membangkitkan node baru
            nextNode = SearchState(current.root.move(dr, dc), prevState=current, prevMove=movesNames[i], level=current.level+1)

            # Mengecek apabila node selanjutnya valid
            if(nextNode != None and nextNode.root != None):
                nodeCount += 1
                pq.push(nextNode)

# Menyimpan rute solusi
solution = findSolutionRoute(solutionState)

# Menghitung waktu selesai
timeEnd = time.process_time_ns()

# Mencetak langkah solusi
print("Solusi puzzle :")
for index, state in enumerate(solution):
    print("-----","Langkah", str(index+1) + ":", state.prevMove , "-----")
    state.root.printBoard()
    print()

# Mencetak waktu running program
time = timeEnd - timeStart
print("Waktu program berjalan :",time / 1000000, "ms")

# Mencetak total gerakan
print("Total langkah :", len(solution))

# Mencetak jumlah simpul yang dibangkitkan
print("Jumlah simpul dibangkitkan :",nodeCount)