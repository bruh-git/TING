class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def is_empty(self):
        return self._data == []

    def dequeue(self):
        if not self.is_empty():
            return self._data.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("index out of range")
        return self._data[index]
