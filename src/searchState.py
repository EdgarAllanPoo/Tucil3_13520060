class SearchState: # Menyimpan status dari langkah pencarian yang sedang ditelusuri

    def __init__(self, root, prevState, prevMove, level):
        self.root = root
        self.prevState = prevState
        self.prevMove = prevMove
        self.level = level