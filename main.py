class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        print("My name is", name, "and I am", age, "and my tracks are", tracks, "and my scores are", score)
        # pass
        print("This is the speak function", self.name, "and this is the age", self.age, "and this is the tracks", tracks, "and this is the score", score)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
