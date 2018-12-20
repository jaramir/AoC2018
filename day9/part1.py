class Game:
    def __init__(self, players=1):
        self.marbles = [0]
        self.current = 0
        self.last = 0
        self.points = [0] * players

    def turn(self):
        value = self.last + 1

        if value % 23 == 0:
            index = self.current - 7
            if index < 0:
                index += len(self.marbles)

            player = (value - 1) % len(self.points)
            self.points[player] += value + self.marbles[index]

            del self.marbles[index]
        else:
            index = self.current + 2

            if index > len(self.marbles):
                index -= len(self.marbles)

            self.marbles.insert(index, value)

        self.current = index
        self.last = value

    def play_until(self, value):
        while self.last < value:
            self.turn()
        return self


if __name__ == '__main__':
    print max(Game(players=476).play_until(71431).points)
