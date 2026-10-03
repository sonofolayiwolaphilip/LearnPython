import json
import uuid
import random

# Utility function to load data from the external JSON database file
def open_file():
    try:
        with open("quiz.json", "r") as file:
            quiz = json.load(file)
            return quiz
    except json.JSONDecodeError:
        return "JSON Decode Error"
    except FileNotFoundError:
        return "File Not Found"
    


def save_file(data):
    try:
        with open("quiz.json", "w") as file:
            json.dump(data, file, indent=4)
            print("Saved successfully")
    except Exception as e:
        print(f"Error saving file: {e}")



def fetch_question(score, answered_question):
    # Retrieve the parsed quiz dictionary from the JSON file
    quiz = open_file()

    # Create a list of keys that have not been answered
    unanswered_ids = [k for k in quiz.keys() if k not in answered_question]

    # checks if there are questions that not been answere
    # is unanswered_ids empty?
    if not unanswered_ids:
        print("You have answered all available questions")
        return score

    # Pick a random Id from the list
    random_id = random.choice(unanswered_ids)

    # Save the IDs immediate to answered_question list
    answered_question.append(random_id)

    #Fetch the question's dictionary data using the chosen ID
    random_dic = quiz[random_id]

        # Extract the literal question text and its nested metadata (options/answers)
    for quest, opt_ans in random_dic.items():
        print(f"{quest}")

        # Iterate through the options dictionary to print choices
        for option_id, options in opt_ans["options"].items():
                    
                    # Display the multiple-choice option key along with its text
                print(f"{option_id}. {options}")

                    # Capture user response and force it to lowercase for case-insensitive matching
        response = (input("Response A, B, C or D: ")).lower()
                
            # Extract the correct option key string from the Answer dict, then force to lowercase
        correct_letter = (list(opt_ans["answer"].keys())[0]).lower()
                
                    # Check if the player's input matches the expected answer key
        if response == correct_letter:
            print("Correct")
            score += 1
        else:
            print("Wrong")
        # Immediately exit the function and send the updated score back to the loop
        return score
    
    return score


def add_new_question():
    quiz = open_file()
    next_id = str(len(quiz) + 1)

    print(f"\n --- Adding Question #{next_id} ---")
    question_text = input("Enter the quiz question: ").strip()
    while not question_text:
        question_text = input("Enter the quiz question: ").strip()
    
    opt_a = input("Enter Option A").strip()
    while not opt_a:
        opt_a = input("Enter Option A").strip()
    
    opt_b = input("Enter Option B").strip()
    while not opt_b:
        opt_b = input("Enter Option B").strip()

    opt_c = input("Enter Option C").strip()
    while not opt_c:
        opt_c = input("Enter Option C").strip()

    opt_d = input("Enter Option D").strip()
    while not opt_d:
        opt_d = input("Enter Option D").strip()

    correct_answer = input("Answer: ").strip()
    while not correct_answer:
        correct_answer = input("Answer: ").strip()
    ans_key = ""
    if correct_answer == opt_a:
        ans_key = "A"
    elif correct_answer == opt_b:
        ans_key = "B"
    elif correct_answer == opt_c:
        ans_key = "C"
    elif correct_answer == opt_d:
        ans_key = "D"


    new_question_structure = {
            question_text :
                {
                    "options" : {
                        "A":opt_a,
                        "B":opt_b,
                        "C":opt_c,
                        "D":opt_d
                    },
                    "answer" :{
                        ans_key: correct_answer
                    }
                }
            }
    
    next_id = str(uuid.uuid4())
    quiz[next_id] = new_question_structure
    save_file(quiz)
    
def play_game():
    # Initialize the tracking variables for persistent game state
    score = 0
    play = True
    quiz = open_file()    

    if not quiz:
        print("\nNo questions available! Please add a question first.")
        return
    numb_of_question = len(quiz)
    answered_question = []

    while len(answered_question) < numb_of_question:
        score = fetch_question(score, answered_question)
        if score == -1:
            break

        print(f"Current Score is: {score}")
    print(f"\n === Game Over! Final Score is: {score}/{len(answered_question)} ===")


def main():
    state = "MAIN_MENU"

    while state != "EXIT":
        match state:
            case "MAIN_MENU":
                print("\n=== GENERAL QUIZ ===")
                print("1. Play Game")
                print("2. Add New Question")
                print("3. Exit")

                choice = input("Select an option (1-3): ").strip()
                match choice:
                    case "1":
                        state = "PLAY"
                        
                    case "2":
                        state = "ADD"
                    case "3":
                        state = "EXIT"
            case "PLAY":
                play_game()
                state = "MAIN_MENU"

            case "ADD":
                add_new_question()
                state = "MAIN_MENU"
            case _:
                state = "EXIT"
    else:
        print("\n Thanks for playing")
        
if __name__ == "__main__":
    main()