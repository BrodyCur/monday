emotions = {
    "anger": int(input('anger on a level of 1 - 3: ')),
    "disgust": int(input('disgust on a level of 1 - 3: ')),
    "fear": int(input('fear on a level of 1 - 3: ')),
    "sadness": int(input('sadness on a level of 1 - 3: ')),
    "joy": int(input('joy on a level of 1 - 3: ')),
}

class Person:
    """ This class represents a person object """

    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions

    def __str__(self):
        for emotion, level in self.emotions.items():
            return f"I am feeling a {self.find_emotions()} amount of {self.emotions}"

    def find_emotions(self):
        for level in self.emotions.values():
            if level == 1:
                return 'low'
            elif level == 2:
                return 'medium'
            elif level == 3:
                return 'high'
            else:
                return 'invalid number'


brody = Person('Brody', emotions)

print(brody)