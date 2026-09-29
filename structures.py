class ActionStack:
    """Stack data structure to record actions for undo functionality."""
    def __init__(self):
        self._stack = []

    def push(self, action):
        self._stack.append(action)

    def pop(self):
        if not self.is_empty():
            return self._stack.pop()
        return None

    def is_empty(self):
        return len(self._stack) == 0


class ChoreQueue:
    """Queue data structure for fair round-robin chore distribution."""
    def __init__(self):
        self._queue = []

    def enqueue(self, roommate):
        self._queue.append(roommate)

    def dequeue(self):
        if not self.is_empty():
            return self._queue.pop(0)
        return None

    def rotate(self):
        if self._queue:
            person = self.dequeue()
            self.enqueue(person)
            return person
        return None

    def is_empty(self):
        return len(self._queue) == 0
