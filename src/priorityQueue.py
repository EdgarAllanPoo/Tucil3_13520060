class PriorityQueue: # Implementasi dari priority queue

    # Konstruktor dengan input fungsi prioritas dari queue
    def __init__(self, priority_function):
        self.queue = []
        self.func = priority_function
    
    # Mengecek apakah queue kosong
    def isEmpty(self):
        return len(self.queue) == 0

    # Melihat elemen pertama
    def first(self):
        return self.queue[0]

    # Melihat elemen terakhir
    def last(self):
        return self.queue[len(self.queue) - 1]

    # Memasukkan element ke dalam priority queue
    def push(self, element):
        pos = 0
        found = False

        while(not found and pos < len(self.queue)):
            if(self.func(element, self.queue[pos])):
                found = True
            else:
                pos+=1
        
        self.queue.insert(pos, element)

    # Menghapus elemen terdepan
    def pop(self):
        self.queue.pop(0)