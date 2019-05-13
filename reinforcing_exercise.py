emotions = {
    "anger": int(input('anger on a level of 1 - 3: ')),
    "disgust": int(input('disgust on a level of 1 - 3: ')),
    "fear": int(input('fear on a level of 1 - 3: ')),
    "sadness": int(input('sadness on a level of 1 - 3: ')),
    "joy": int(input('joy on a level of 1 - 3: ')),
}

# emotions = {
#     "anger": 1,
#     "disgust": 2,
#     "fear": 3,
#     "sadness": 2,
#     "joy": 1
# }

class Person:
    """ This class represents a person object """

    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions

    def __str__(self):
        temp = []
        ratings = {
            '1': 'low',
            '2': 'medium',
            '3': 'high'
        }

        for emotion, amount in self.emotions.items():
            temp.append(f"I am feeling a {ratings[str(amount)]} amount of {emotion}")

        return '\n'.join(temp)

    # def find_emotions(self):
    #     for level in self.emotions.values():
    #         if level == 1:
    #             return 'low'
    #         elif level == 2:
    #             return 'medium'
    #         elif level == 3:
    #             return 'high'
    #         else:
    #             return 'invalid number'


brody = Person('Brody', emotions)

print(brody)

