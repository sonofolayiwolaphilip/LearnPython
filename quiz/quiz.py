import json
import uuid
import random
import getpass

USER_FILE = "users.json"
QUIZ_FILE = "myquiz.json"

# ============================
# FILE I/O OPERATIONS
# ============================
def load_open_json(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_json(filename, data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data {e}")

# ===============================
# AUTHENTICATION ENGINE
# ===============================

def register_user():
    print("\n --- Create Account ---")
    users = load_open_json(USER_FILE)

    username = input("Enter a unique username: ").strip()
    if not username:
        print("Username cannot be empty. ")
        return None

    if username in users:
        print("Username already exists! Try logging in. ")
        return None

    password = getpass.getpass("Enter a password: ").strip()
    if not password:
        print("Password cannot be Empty. ")
        return None

    users[username] = {
        "password": password,
        "highsocre": 0
    }
    save_json(USER_FILE, users)
    print("REGISTRATION SUCCESSFUL!")
    return username

def login_user():
    print("\n --- Login ----")
    users = load_open_json(USER_FILE)

    username = input("Username: ").strip()
    password = getpass.getpass("Password: ").strip()

    if username in users and users[username]["password"] == password:
        print(f"Welcome back, {username}!")
        return username
        
    print("Invalid username or password.")
    return None
"""
# =======================================
|           CORE GAME ALGORITHM          |
# =======================================

"""

def fetch_question(score, answered_questions):
    quiz = load_open_json(QUIZ_FILE)
    unanswered_ids = [k for k in quiz.keys() if k not in answered_questions]

    if not unanswered_ids:
        print("\n🎉 Spectacular! You have answered all available questions")
        return score, False

    random_id = random.choice(unanswered_ids)
    answered_questions.append(random_id)

    question_data = quiz[random_id]
    print(question_data)

    print(f"\n📝 {question_data['question']}")
    for option_id, option_text in question_data["options"].items():
        print(f" {option_id}. {option_text}")

    response = input("\nYour answer(A,B,C,D) or 'q' to quit: ").strip().upper()

    if response == "Q":
        print("Quitting current game session...")
        return score, False

    correct_letter = question_data["answer"]

    if response == correct_letter:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {correct_letter}") 

    return score, True

def update_highscore(username, final_score):
    users = load_open_json(USER_FILE)
    if username in users:
        current_record = users[username].get("highscore", 0)
        if final_score > current_record:
            print(f"🏆 New Personal High Score! Old: {current_record} ➔ New: {final_score}")
            users[username]["highscore"] = final_score
            save_json(USER_FILE, users)

def add_new_question():
    quiz = load_open_json(QUIZ_FILE)
    print(f"\n --- Adding Question #{len(quiz) + 1} ---")

    question_text = input("Enter the Quiz Question: ").strip()
    while not question_text:
        question_text = input("Question cannot be blank: ").strip()

    options = {}
    for letter in ["A", "B", "C", "D"]:
        opt = input(f"Enter Option {letter}: ").strip()
        while not opt:
            opt = input(f"Option {letter} cannot be blank").strip()
        options[letter] = opt
    correct_answer = input("Enter the correct option Letter (A, B,C, D): ").strip()
    while correct_answer not in ["A", "B", "C", "D"]:
        correct_answer = input("Invalid choice. Please enter A,B,C or D").strip()

    new_question_structure = {
        "question": question_text,
        "options": options,
        "answer": correct_answer
    }

    quiz[str(uuid.uuid4())] = new_question_structure
    save_json(QUIZ_FILE, quiz)
    print("Question added successfully")


def play_game(username):
    quiz = load_open_json(QUIZ_FILE)
    if not quiz:
        print("\n⚠️ No questions available! Please ask an administrator to add questions first.")
        return

    score = 0
    answered_questions = []
    total_pool = len(quiz)

    print(f"\n🎬 Game started! Player: {username}")
    while len(answered_questions) < total_pool:
        score, keep_playing = fetch_question(score, answered_questions)
        if not keep_playing:
            break
        print(f"Current Score: {score}")
    print(f"\n === game Over! Final Score: {score}/{len(answered_questions)}===")
    if username:
        update_highscore(username, score)

 # ======================================
#|            MANIN ROUTER               |#
 # ======================================

def main():
    current_user = None

    while True:
        if not current_user:
            print("\n=== GENERAL QUIZ ===")
            print("1. Login")
            print("2. Register New Account")
            print("3. Play as Guest")
            print("4. View leaderboard")
            print("5. Add New Question")
            print("6. Exit")

            choice = input("Select an option (1-6): ").strip()
            if choice == "1":
                current_user = login_user()
            elif choice == "2":
                current_user = register_user()
            elif choice == "3":
                play_game(username=None)
            # elif choice == "4":
            #     show_leaderboard()
            elif choice == "5":
                add_new_question()
            elif choice == "6":
                print("\n Thanks for playing! Goodbye")
                break
        else:
            print(f"\n=== LOGGED IN AS: {current_user} ===")
            print("1. Play Quiz")
            print("2. View Leaderboard")
            print("3. Add New Question")
            print("4. Logout")
            print("5. Exit")

            choice = input("Select an option (1 - 5): ").strip()
            if choice == "1":
                play_game(current_user)
            # elif choice == "2":
            #     show_leaderboard()
            elif choice == "3":
                add_new_question()
            elif choice == "4":
                print(f"Logged out from {current_user}.")
                current_user = None
            elif choice == "5":
                print("\nThanks for playing! Goodbye.")
                break

if __name__ == "__main__":
    main()
