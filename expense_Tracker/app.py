import random
quiz = {
    "1dskgfk1224ef": {
        "What planet is known as the Red Planet?": {
            "options": {
                "A": "Venus",
                "B": "Mars",
                "C": "Jupiter",
                "D": "Saturn"
            },
            "answer": {
                "B": "Mars"
            }
        }
    },
    "2qwqwq2134ff": {
        "What is the largest ocean on Earth?": {
            "options": {
                "A": "Atlantic Ocean",
                "B": "Indian Ocean",
                "C": "Pacific Ocean",
                "D": "Arctic Ocean"
            },
            "answer": {
                "C": "Pacific Ocean"
            }
        }
    },
}
id_list = []
# for k in quiz.keys():
#     id_list.append(k)
# print(id_list)

id,question = random.choice(list(quiz.items()))
print(id,)