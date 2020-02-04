class Subscriber(object):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("{0}, {1}".format(self.name, message))


class Publisher(object):
    def __init__(self, events):
        self.subscribers = {event: dict() for event in events}

    def get_subscribers(self, event):
        return self.subscribers[event]

    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)


if __name__ == "__main__":
    pub = Publisher(["Lunch", "Go home"])

    astin = Subscriber("Astin")
    james = Subscriber("James")
    jeff = Subscriber("Jeff")

    pub.register("Lunch", astin)
    pub.register("Go home", astin)
    pub.register("Go home", james)
    pub.register("Lunch", jeff)

    pub.dispatch("Lunch", "Time for lunch.")
    pub.dispatch("Go home", "Time to go home.")

