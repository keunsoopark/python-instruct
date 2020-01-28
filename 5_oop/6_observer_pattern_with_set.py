class Subscriber(object):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("{0}, {1}".format(self.name, message))


class Publisher(object):
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


if __name__ == "__main__":
    pub = Publisher()

    guy1 = Subscriber("Guy1")
    guy2 = Subscriber("Guy2")
    guy3 = Subscriber("Guy3")

    pub.register(guy1)
    pub.register(guy2)
    pub.register(guy3)

    pub.dispatch("Time to lunch")
    pub.unregister(guy2)
    pub.dispatch("Time to go home")
