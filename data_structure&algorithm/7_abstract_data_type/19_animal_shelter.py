from deque import Deque


class AnimalShelterKp(object):
    def __init__(self):
        self.dog = Deque()
        self.cat = Deque()

    def enqueue(self, name, animal_type):
        if animal_type == "dog":
            self.dog.enqueue(name)
        elif animal_type == "cat":
            self.cat.enqueue(name)
        else:
            print("We do not care such animal type.")

    def dequeueDog(self):
        return self.dog.dequeue()

    def dequeueCat(self):
        return self.cat.dequeue()

    def _print(self):
        print("Cat:")


class Node(object):
    def __init__(self,
                 animalName=None,
                 animalKind=None,
                 pointer=None):
        self.animalName = animalName
        self.animalKind = animalKind
        self.pointer = pointer
        self.timestamp = 0


class AnimalShelter(object):
    def __init__(self):
        self.headCat = None
        self.headDog = None
        self.tailCat = None
        self.tailDog = None
        self.animalNumber = 0

    def enqueue(self, animalName, animalKind):
        self.animalNumber += 1
        newAnimal = Node(animalName, animalKind)
        newAnimal.timestamp = self.animalNumber

        if animalKind == "cat":
            if not self.headCat:
                self.headCat = newAnimal
            if self.tailCat:
                self.tailCat.pointer = newAnimal
            self.tailCat = newAnimal

        elif animalKind == "dog":
            if not self.headDog:
                self.headDog = newAnimal
            if self.tailDog:
                self.tailDog.pointer = newAnimal
            self.tailDog = newAnimal

    def dequeueDog(self):
        if self.headDog:
            newAnimal = self.headDog
            self.headDog = newAnimal.pointer
            return str(newAnimal.animalName)
        else:
            print("There is no dog.")

    def dequeueCat(self):
        if self.headCat:
            newAnimal = self.headCat
            self.headCat = newAnimal.pointer
            return str(newAnimal.animalName)
        else:
            print("There is no cat.")

    def dequeueAny(self):
        if self.headCat and not self.headDog:
            return self.dequeueCat()
        elif self.headDog and not self.headCat:
            return self.dequeueDog()
        elif self.headDog and self.headCat:
            if self.headDog.timestamp < self.headCat.timestamp:
                return self.dequeueDog()
            else:
                return self.dequeueCat()
        else:
            print("There is no animal.")

    def _print(self):
        print("Cat:")
        cats = self.headCat
        while cats:
            print("\t{0}".format(cats.animalName))
            cats = cats.pointer
        print("Dog:")
        dogs = self.headDog
        while dogs:
            print("\t{0}".format(dogs.animalName))
            dogs = dogs.pointer


if __name__ == "__main__":
    qs_kp = AnimalShelterKp()
    qs_kp.enqueue("Bob", "cat")
    qs_kp.enqueue("Mia", "cat")
    qs_kp.enqueue("Yoda", "dog")
    qs_kp.enqueue("Wolf", "dog")
    # qs_kp._print()

    print("Deque for a dog and a cat.")
    qs_kp.dequeueDog()
    qs_kp.dequeueCat()
    # qs_kp._print()

    print()

    qs = AnimalShelter()
    qs.enqueue("Bob", "cat")
    qs.enqueue("Mia", "cat")
    qs.enqueue("Yoda", "dog")
    qs.enqueue("Wolf", "dog")
    qs._print()

    qs.dequeueDog()
    qs.dequeueCat()
    qs._print()
