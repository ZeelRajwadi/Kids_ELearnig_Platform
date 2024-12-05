import tkinter as tk
from tkinter import messagebox
import random
import time

# Expanded lessons, quiz data, and detailed content
lessons_data = {
    "Math": {
        "Addition Basics": [
            ("What is 2 + 3?", ["4", "5", "6", "7"], "5"),
            ("What is 5 + 5?", ["10", "9", "11", "12"], "10"),
            ("What is 1 + 6?", ["7", "5", "8", "6"], "7"),
        ],
        "Multiplication Basics": [
            ("What is 2 x 2?", ["3", "4", "5", "6"], "4"),
            ("What is 3 x 5?", ["15", "12", "10", "8"], "15"),
            ("What is 7 x 6?", ["42", "36", "48", "54"], "42"),
        ],
    },
    "English": {
        "What is a Verb?": [
            ("Which of the following is a verb?", ["Run", "Table", "Car", "Dog"], "Run"),
            ("Pick the verb: 'She sings beautifully'", ["She", "Sings", "Beautifully", "None"], "Sings"),
            ("Identify the verb: 'I am reading a book'", ["I", "Reading", "Book", "Am"], "Reading"),
        ],
        "Find the Correct Spelling": [
            ("Which is the correct spelling?", ["Elephant", "Eliphant", "Elefant", "Elliphant"], "Elephant"),
            ("Which is the correct spelling?", ["Beautiful", "Beautifull", "Beutiful", "Butiful"], "Beautiful"),
            ("Which is the correct spelling?", ["Receive", "Recieve", "Recive", "Receve"], "Receive"),
        ]
    },
    "General Knowledge": {
        "Famous Landmarks": [
            ("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], "Paris"),
            ("Which is the largest ocean?", ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific"),
            ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], "Mars"),
        ]
    },
    "Nursery Rhymes": {
        "Popular Rhymes": [
            ("What is the first line of 'Twinkle Twinkle Little Star'?", ["Twinkle, twinkle, little star", "Row, row, row your boat", "Humpty Dumpty sat on a wall", "Baa, baa, black sheep"], "Twinkle, twinkle, little star"),
            ("In 'Baa, Baa, Black Sheep', what is asked?", ["Have you any wool?", "Are you sleeping?", "How much is that doggie?", "Is this the way to Amarillo?"], "Have you any wool?"),
            ("What is the color of the cat in 'Hey Diddle Diddle'?", ["Black", "White", "Gray", "Orange"], "Gray"),
        ]
    }
}

# Expanded detailed lesson content
lessons_content = {
    "Math": {
        "Addition Basics": "Addition is the process of bringing two or more numbers together to make a new total. For example, 2 + 3 = 5.",
        "Multiplication Basics": "Multiplication is a way of adding the same number repeatedly. For example, 2 x 3 means 2 added 3 times, which equals 6."
    },
    "English": {
        "What is a Verb?": "A verb is an action word. It tells us what someone is doing. For example, 'run', 'eat', and 'sleep' are all verbs.",
        "Find the Correct Spelling": "Here you have to select the correct spelling of the given word."
    },
    "General Knowledge": {
        "Famous Landmarks": "Famous landmarks are structures or sites that are well known and often represent a particular place.",
    },
    "Nursery Rhymes": {
        "Popular Rhymes": "Nursery rhymes are traditional poems or songs for children that often tell a story or teach a lesson."
    }
}

class QuizApp:
    def __init__(self, master):
        self.master = master
        master.title("Quiz and Games App")
        master.geometry("800x500")
        master.config(bg="#e1f5fe")  # Light blue background for a kid-friendly appearance

        self.total_coins = 0  # Variable to store total coins earned
        self.badges = {
            "Perfect Score": "Congratulations! You answered all questions correctly!",
            "Great Job": "Well done! You answered at least 2 out of 3 questions correctly.",
            "Keep Trying": "Don't worry! Try again to improve your score."
        }

        self.round = 1  # Add a round tracker for the memory game
        self.total_quizzes = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.total_time_spent = 0  # Time spent in quizzes
        self.start_time = None  # Start time for the current quiz
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()

        # Display coins in the top-right corner
        self.coins_label = tk.Label(self.master, text=f"Coins: {self.total_coins}", font=("Arial", 16, 'bold'), bg="#e1f5fe", fg="#ffab00")
        self.coins_label.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

        title = tk.Label(self.master, text="Welcome to the Quiz and Games App", font=("Comic Sans MS", 24, 'bold'), bg="#e1f5fe", fg="#1565c0")
        title.pack(pady=20)

        lessons_button = tk.Button(self.master, text="Go to Lessons", command=self.show_lessons, width=20, bg="#29b6f6", fg="white", font=("Comic Sans MS", 14, 'bold'))
        lessons_button.pack(pady=10)

        # Memory Game Button
        memory_game_button = tk.Button(self.master, text="Memory Game", command=self.start_memory_game, width=20, bg="#ffca28", fg="black", font=("Comic Sans MS", 14, 'bold'))
        memory_game_button.pack(pady=10)

        # Scrabbling Game Button
        scrabbling_button = tk.Button(self.master, text="Scrabbling Game", command=self.scrabbling_game, width=20, bg="#ff5722", fg="white", font=("Comic Sans MS", 14, 'bold'))  # Changed color
        scrabbling_button.pack(pady=10)

        dashboard_button = tk.Button(self.master, text="Dashboard", command=self.show_dashboard, width=20, bg="#43a047", fg="white", font=("Comic Sans MS", 14, 'bold'))
        dashboard_button.pack(pady=10)

        quit_button = tk.Button(self.master, text="Quit", command=self.master.quit, bg="#d32f2f", fg="white", font=("Comic Sans MS", 14, 'bold'))
        quit_button.pack(pady=20)

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_frame()
        dashboard_title = tk.Label(self.master, text="Dashboard", font=("Comic Sans MS", 24, 'bold'), bg="#e1f5fe", fg="#1565c0")
        dashboard_title.pack(pady=20)

        dashboard_content = tk.Label(self.master, text=f"Total Coins: {self.total_coins}", font=("Arial", 16), bg="#e1f5fe")
        dashboard_content.pack(pady=10)

        # Statistics Table
        stats_frame = tk.Frame(self.master, bg="#e1f5fe")
        stats_frame.pack(pady=10)

        # Display statistics in a table format
        stats_label = tk.Label(stats_frame, text="Statistics", font=("Comic Sans MS", 18, 'bold'), bg="#e1f5fe", fg="#1565c0")
        stats_label.grid(row=0, columnspan=2, pady=(0, 10))

        tk.Label(stats_frame, text="Total Quizzes:", bg="#e1f5fe").grid(row=1, column=0, sticky="e")
        tk.Label(stats_frame, text=self.total_quizzes, bg="#e1f5fe").grid(row=1, column=1, sticky="w")

        tk.Label(stats_frame, text="Correct Answers:", bg="#e1f5fe").grid(row=2, column=0, sticky="e")
        tk.Label(stats_frame, text=self.correct_answers, bg="#e1f5fe").grid(row=2, column=1, sticky="w")

        tk.Label(stats_frame, text="Incorrect Answers:", bg="#e1f5fe").grid(row=3, column=0, sticky="e")
        tk.Label(stats_frame, text=self.incorrect_answers, bg="#e1f5fe").grid(row=3, column=1, sticky="w")

        tk.Label(stats_frame, text="Total Time Spent (s):", bg="#e1f5fe").grid(row=4, column=0, sticky="e")
        tk.Label(stats_frame, text=self.total_time_spent, bg="#e1f5fe").grid(row=4, column=1, sticky="w")

        back_button = tk.Button(self.master, text="Back to Main Menu", command=self.create_main_menu, bg="#29b6f6", fg="white", font=("Comic Sans MS", 14, 'bold'))
        back_button.pack(pady=20)

    # Memory Game
    
    def start_memory_game(self):
        self.memory_words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "orange"]  # Added more words
        self.round = 1  # Reset rounds for a new memory game
        self.show_memory_round()

    def show_memory_round(self):
        self.clear_frame()
        self.current_memory_words = random.sample(self.memory_words, 3 + self.round)  # Increase the number of words with rounds

        title = tk.Label(self.master, text="Memorize these words:", font=("Comic Sans MS", 24), bg="#e1f5fe")
        title.pack(pady=20)

        for word in self.current_memory_words:
            word_label = tk.Label(self.master, text=word, font=("Arial", 18), bg="#e1f5fe")
            word_label.pack(pady=5)

        self.master.after(5000, self.hide_memory_words)

    def hide_memory_words(self):
        self.clear_frame()
        title = tk.Label(self.master, text="What's on the list?", font=("Comic Sans MS", 24), bg="#e1f5fe")
        title.pack(pady=20)

        self.user_input = tk.Entry(self.master, font=("Arial", 18))
        self.user_input.pack(pady=10)

        submit_button = tk.Button(self.master, text="Submit", command=self.check_memory, bg="#81c784", fg="white", font=("Comic Sans MS", 14))
        submit_button.pack(pady=5)

    def check_memory(self):
        user_response = self.user_input.get().split(",")
        user_response = [word.strip().lower() for word in user_response]
        correct_answers = self.current_memory_words

        score = len(set(user_response) & set(correct_answers))  # Calculate score based on correct answers
        self.total_coins += score  # Add earned coins based on score

        if score >= len(correct_answers):
            message = "Perfect! You remembered all the words!"
        elif score >= len(correct_answers) // 2:
            message = "Great job! You remembered some words!"
        else:
            message = "Try again next time!"

        self.show_memory_result(message)

    def show_memory_result(self, message):
        self.clear_frame()
        title = tk.Label(self.master, text=message, font=("Comic Sans MS", 24), bg="#e1f5fe")
        title.pack(pady=20)

        coins_label = tk.Label(self.master, text=f"Coins: {self.total_coins}", font=("Arial", 16, 'bold'), bg="#e1f5fe", fg="#ffab00")
        coins_label.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

        next_round_button = tk.Button(self.master, text="Next Round", command=self.show_memory_round, bg="#ffca28", fg="black", font=("Comic Sans MS", 12))
        next_round_button.pack(pady=10)

        back_button = tk.Button(self.master, text="Back to Menu", command=self.create_main_menu, bg="#ffca28", fg="black", font=("Comic Sans MS", 12))
        back_button.pack(pady=10)

    # Scrabbling Game
    def scrabbling_game(self):
        self.clear_frame()
        self.words = ["elephant", "giraffe", "kangaroo", "platypus", "rhinoceros", "chimpanzee", "hippopotamus", "dolphin"]  # Added more words
        self.current_word = random.choice(self.words)
        self.scrambled_word = self.scramble_word(self.current_word)

        title = tk.Label(self.master, text="Unscramble the word:", font=("Comic Sans MS", 24), bg="#e1f5fe")
        title.pack(pady=20)

        scrambled_label = tk.Label(self.master, text=self.scrambled_word, font=("Arial", 18), bg="#e1f5fe")
        scrambled_label.pack(pady=10)

        self.user_guess = tk.Entry(self.master, font=("Arial", 18))
        self.user_guess.pack(pady=10)

        submit_button = tk.Button(self.master, text="Submit", command=self.check_scrabbling, bg="#81c784", fg="white", font=("Comic Sans MS", 14))
        submit_button.pack(pady=5)

        back_button = tk.Button(self.master, text="Back to Menu", command=self.create_main_menu, bg="#ffca28", fg="black", font=("Comic Sans MS", 12))
        back_button.pack(side=tk.BOTTOM, pady=20)

    def scramble_word(self, word):
        word = list(word)
        random.shuffle(word)
        return ''.join(word)

    def check_scrabbling(self):
        user_guess = self.user_guess.get().strip().lower()
        if user_guess == self.current_word:
            message = "Correct! You've unscrambled the word!"
            self.total_coins += 10
        else:
            message = f"Incorrect! The correct word was: {self.current_word}."

        self.show_scrabbling_result(message)

    def show_scrabbling_result(self, message):
        self.clear_frame()
        title = tk.Label(self.master, text=message, font=("Comic Sans MS", 24), bg="#e1f5fe")
        title.pack(pady=20)

        coins_label = tk.Label(self.master, text=f"Coins: {self.total_coins}", font=("Arial", 16, 'bold'), bg="#e1f5fe", fg="#ffab00")
        coins_label.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

        back_button = tk.Button(self.master, text="Back to Menu", command=self.create_main_menu, bg="#ffca28", fg="black", font=("Comic Sans MS", 12))
        back_button.pack(side=tk.BOTTOM, pady=20)

    def show_lessons(self):
        self.clear_frame()

        # Update coins label at the top-right corner
        self.coins_label = tk.Label(self.master, text=f"Coins: {self.total_coins}", font=("Arial", 16, 'bold'), bg="#e1f5fe", fg="#ffab00")
        self.coins_label.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

        title = tk.Label(self.master, text="Select a Subject", font=("Comic Sans MS", 24, 'bold'), bg="#e1f5fe", fg="#1565c0")
        title.pack(pady=20)

        subjects_frame = tk.Frame(self.master, bg="#e1f5fe")
        subjects_frame.pack(pady=10)

        # Subject buttons with different colors
        math_button = tk.Button(subjects_frame, text="Math", command=lambda: self.select_topic("Math"), bg="#1976d2", fg="white", font=("Comic Sans MS", 16, 'bold'))
        math_button.grid(row=0, column=0, padx=20, pady=10)

        english_button = tk.Button(subjects_frame, text="English", command=lambda: self.select_topic("English"), bg="#f44336", fg="white", font=("Comic Sans MS", 16, 'bold'))
        english_button.grid(row=0, column=1, padx=20, pady=10)

        gk_button = tk.Button(subjects_frame, text="General Knowledge", command=lambda: self.select_topic("General Knowledge"), bg="#4caf50", fg="white", font=("Comic Sans MS", 16, 'bold'))
        gk_button.grid(row=1, column=0, padx=20, pady=10)

        rhymes_button = tk.Button(subjects_frame, text="Nursery Rhymes", command=lambda: self.select_topic("Nursery Rhymes"), bg="#ff9800", fg="white", font=("Comic Sans MS", 16, 'bold'))
        rhymes_button.grid(row=1, column=1, padx=20, pady=10)

        back_button = tk.Button(self.master, text="Back to Main Menu", command=self.create_main_menu, bg="#29b6f6", fg="white", font=("Comic Sans MS", 14, 'bold'))
        back_button.pack(pady=20)

    def select_topic(self, subject):
        self.clear_frame()
        title = tk.Label(self.master, text=f"{subject} Topics", font=("Comic Sans MS", 24, 'bold'), bg="#e1f5fe", fg="#1565c0")
        title.pack(pady=20)

        topics_frame = tk.Frame(self.master, bg="#e1f5fe")
        topics_frame.pack(pady=10)

        for topic in lessons_data[subject]:
            topic_button = tk.Button(topics_frame, text=topic, command=lambda t=topic: self.start_quiz(subject, t), width=30, bg="#64b5f6", fg="white", font=("Comic Sans MS", 14, 'bold'))
            topic_button.pack(pady=5)

        back_button = tk.Button(self.master, text="Back to Subjects", command=self.show_lessons, bg="#29b6f6", fg="white", font=("Comic Sans MS", 14, 'bold'))
        back_button.pack(pady=20)

    def start_quiz(self, subject, topic):
        self.clear_frame()
        self.start_time = time.time()

        title = tk.Label(self.master, text=f"{subject}: {topic}", font=("Comic Sans MS", 24, 'bold'), bg="#e1f5fe", fg="#1565c0")
        title.pack(pady=20)

        # Add more details about the lesson
        lesson_details = lessons_content[subject][topic]
        lesson_label = tk.Label(self.master, text=lesson_details, font=("Arial", 14), bg="#e1f5fe", wraplength=600, justify="left")
        lesson_label.pack(pady=10)

        self.questions = lessons_data[subject][topic]
        self.current_question = 0
        self.correct_answers_in_quiz = 0
        self.incorrect_answers_in_quiz = 0
        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            question_text, options, correct_answer = question_data

            question_label = tk.Label(self.master, text=question_text, font=("Arial", 16), bg="#e1f5fe")
            question_label.pack(pady=20)

            options_frame = tk.Frame(self.master, bg="#e1f5fe")
            options_frame.pack(pady=10)

            for option in options:
                option_button = tk.Button(options_frame, text=option, command=lambda o=option: self.check_answer(o, correct_answer), width=20, bg="#42a5f5", fg="white", font=("Arial", 14))
                option_button.pack(pady=5)

        else:
            self.end_quiz()

    def check_answer(self, selected_option, correct_answer):
        if selected_option == correct_answer:
            messagebox.showinfo("Correct!", "Well done! You chose the correct answer.")
            self.correct_answers_in_quiz += 1
            self.correct_answers += 1
            self.total_coins += 10  # Add coins for correct answers
        else:
            messagebox.showerror("Incorrect!", f"Oops! The correct answer was: {correct_answer}")
            self.incorrect_answers_in_quiz += 1
            self.incorrect_answers += 1

        self.current_question += 1
        self.clear_frame()
        self.display_question()

    def end_quiz(self):
        end_time = time.time()
        time_spent = int(end_time - self.start_time)
        self.total_time_spent += time_spent

        if self.correct_answers_in_quiz == len(self.questions):
            badge = self.badges["Perfect Score"]
        elif self.correct_answers_in_quiz >= len(self.questions) // 2:
            badge = self.badges["Great Job"]
        else:
            badge = self.badges["Keep Trying"]

        # Update total quizzes
        self.total_quizzes += 1

        messagebox.showinfo("Quiz Completed", f"Quiz completed!\n{badge}\nTime spent: {time_spent} seconds\nYou earned {self.correct_answers_in_quiz * 10} coins.")
        self.create_main_menu()

# Main execution
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
