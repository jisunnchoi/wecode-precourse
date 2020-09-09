class Queue:
    def __init__(self):
        self.state = []

    def enqueue(self, data):
        self.state.append(data)

    def dequeue(self):
        return self.state.pop(0)

    def getFirst(self):
        return self.state[0]