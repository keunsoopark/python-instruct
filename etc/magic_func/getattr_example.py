# a realistic example to add scala functionality in Python tuple
"""
    In Scala, the element in tuple can be accessed like
        val a_tuple = ("z", 3, “Python”, -1)
        println(a_tuple._1) // “z”
        println(a_tuple._3) // “Python”
"""

class Tuple(tuple):
    def __getattr__(self, name):
        def _int(val):
            try:
                return int(val)
            except ValueError:
                return False

        if not name.startswith("_") or not _int(name[1:]):
            raise AttributeError("'tuple' object has no attribute '%s'" % name)
        index = _int(name[1:]) - 1
        return self[index]


t = Tuple(["z", 3, "Python", -1])
print(t._1)
print(t._2)
print(t._3)
