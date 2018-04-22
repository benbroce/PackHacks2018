#note1 = note.Note(screen, 30, 0, 5, 60, (255, 255, 255))
#note2 = note.Note(screen, 100, 0, 5, 60, (255, 0, 255))

import note

class Song:
    def __init__(self, screen, filename, speed):
        self.screen = screen
        self.shown = []
        self.notes = []
        self.speed = speed
        self.hasCollided = False
        with open(filename, "r") as inFile:
            text = inFile.readlines()
        self.tempo = int(text[0]) #ms per beat
        for i in range(1, len(text)):
            self.notes.append(list(map(int, text[i].split())))

    def draw(self):
        for i in self.shown:
            for j in i:
                if j != 0:
                    j.draw()

    def next(self):
        if len(self.notes) == 0:
            return 0
        thisLine = self.notes.pop(0)
        if thisLine[0] == 1:
            thisLine[0] = note.Note(self.screen, 20, 0, 10, 60, note.green)
        if thisLine[1] == 1:
            thisLine[1] = note.Note(self.screen, 100, 0, 10, 60, note.red)
        if thisLine[2] == 1:
            thisLine[2] = note.Note(self.screen, 180, 0, 10, 60, note.yellow)
        if thisLine[3] == 1:
            thisLine[3] = note.Note(self.screen, 260, 0, 10, 60, note.blue)
        if thisLine[4] == 1:
            thisLine[4] = note.Note(self.screen, 340, 0, 10, 60, note.orange)
        self.shown.insert(0, thisLine)
        return 1

    def isCollided(self, minY, maxY):
        if len(self.shown) != 0:
            for i in self.shown[-1]:
                if i != 0:
                    lineY = i.getY()
            if (maxY >= lineY >= minY):
                self.hasCollided = True
                return True
            else:
                return False
                if self.hasCollided:
                    self.shown.pop(-1)
                    self.hasCollided = False
        return False

    def hit(self, key):
        if (self.shown[-1][key] != 0):
            self.hasCollided = False
            self.shown.pop(-1)
            return True
        else:
            return False
