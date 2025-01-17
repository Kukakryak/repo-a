
class State(ABC):
    def open(self, door):
        raise NotImplementedError()

    def close(self, door):
        raise NotImplementedError()


class OpenedState(State):
    def open(self, door):
        print("The door is already open.")

    def close(self, door):
        print("Closing the door...")
        door.change_state(ClosedState())


class ClosedState(State):
    def open(self, door):
        print("Opening the door...")
        door.change_state(OpenedState())

    def close(self, door):
        print("The door is already closed.")


class Door:
    def __init__(self):
        self.state = ClosedState()

    def change_state(self, state):
        self.state = state

    def open(self):
        self.state.open(self)

    def close(self):
        self.state.close(self)


def tests():
    door = Door()
    door.open()
    door.close()
    # Попытка закрыть закрытую дверь
    door.close()
    door.open()
    # Попытка открыть открытую дверь
    door.open()
    door.close()

if __name__ == '__main__':
    tests()
