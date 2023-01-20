class Signal:
    def __init__(self):
        self.start_n = 0
        # self.end_n = 10
        self.xn = []
        self.Xz = []

    def X_z(self, z):
        s = 0
        for n in range(len(self.xn)):
            s += (self.xn[n]) * (z ** (-1 *  (self.start_n + n)))
        return s


    def Z_Transform(self):
        for z in range(-1000, 1000):
            self.Xz.append([z, self.X_z(z)])
        

def main():
    music_sheet = Signal()



if __name__ == "__main__":
    main()
