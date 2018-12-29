class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = self if next is None else next
        self.prev = self if prev is None else prev

    def insert(self, value):
        node = Node(value, self, self.next)
        self.next.prev = node
        self.next = node
        return node

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self.next


class Game:
    def __init__(self, players=1):
        self.marbles = Node(0)
        self.last = 0
        self.points = [0] * players

    def turn(self):
        value = self.last + 1

        if value % 23 == 0:
            self.marbles = self.marbles.prev.prev.prev.prev.prev.prev.prev
            player = (value - 1) % len(self.points)
            self.points[player] += value + self.marbles.value
            self.marbles = self.marbles.remove()
        else:
            self.marbles = self.marbles.next.insert(value)

        self.last = value

    def play_until(self, value):
        while self.last < value:
            self.turn()
        return self

    def get_marbles(self):
        n = self.marbles
        yield n.value
        n = n.next
        while n != self.marbles:
            yield n.value
            n = n.next


if __name__ == '__main__':
    print max(Game(players=476).play_until(71431).points)
