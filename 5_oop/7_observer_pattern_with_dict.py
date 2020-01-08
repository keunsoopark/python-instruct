class SubscriberOne(object):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("{0}, {1}".format(self.name, message))


class SubscriberTwo(object):
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print("{0}, {1}".format(self.name, message))


class Publisher(object):
    def __init__(self):
        self.subscribers = dict()

    # getattr(x, 'foobar') == x.foobar
    def register(self, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.subscribers[who] = callback

    def unregister(self, who):
        del self.subscribers[who]

    def dispatch(self, message):
        for subscriber, callback in self.subscribers.items():
            callback(message)


if __name__ == "__main__":
    pub = Publisher()

    astin = SubscriberOne("Astin")
    james = SubscriberTwo("James")
    jeff = SubscriberOne("Jeff")

    pub.register(astin, astin.update)
    pub.register(james, james.receive)
    pub.register(jeff)

    pub.dispatch("Time for lunch.")
    pub.unregister(jeff)
    pub.dispatch("Time to go home.")
