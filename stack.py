class Stack:
    def __init__(self):
        self.state = []

    def push(self, data):
        self.state.append(data)
        return True

    def pop(self):
        return self.state.pop()

    def getPeak(self):
        peak = self.state[-1]
        return peak

