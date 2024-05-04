from calculations import calcScore
from highscores import HighScores
#import numpy as np
import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Entry, Radiobutton, IntVar, Button

reticule_path = ("./imgs/reticule.png")
reticule_dot_path = ("./imgs/reticuleAndDot.png")
dot_path = ("./imgs/dot.png")
three_dot_path = ("./imgs/3dots.png")
bad_score = ("./imgs/bad_score.png")
good_score = ("./imgs/good_score.png")

import tkinter as tk
from tkinter import Toplevel, Label, Entry, Radiobutton, IntVar, Button, messagebox

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Langham Dome Training Simulator")
        self.root.geometry("400x300")
        self.high_scores = HighScores()  # Ensure this class is defined elsewhere
        self.total_score = 0  # Initialize total_score here

        # Main menu
        self.menu_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.menu_frame.pack(expand=True, fill='both')

        # Start Game
        self.start_button = tk.Button(self.menu_frame, text="Start Game", command=self.start_game, height=2, width=20, bg='#4CAF50', fg='white')
        self.start_button.pack(pady=10)

        # Highscores
        self.scores_button = tk.Button(self.menu_frame, text="Highscores", command=self.show_scores, height=2, width=20, bg='#008CBA', fg='white')
        self.scores_button.pack(pady=10)

        # Quit
        self.quit_button = tk.Button(self.menu_frame, text="Quit", command=self.root.quit, height=2, width=20, bg='#f44336', fg='white')
        self.quit_button.pack(pady=10)

    def start_game(self):
        setup_window = Toplevel(self.root)
        setup_window.title("Game Setup")
        setup_window.geometry("400x300")

        Label(setup_window, text="Enter your name:").pack(pady=(20, 0))
        name_entry = Entry(setup_window)
        name_entry.pack(pady=(0, 20))

        Label(setup_window, text="Select Difficulty:").pack()
        difficulty_var = IntVar(value=0)
        difficulties = ["Easy", "Medium", "Hard", "Expert"]
        for i, difficulty in enumerate(difficulties):
            Radiobutton(setup_window, text=difficulty, variable=difficulty_var, value=i).pack()

        Button(setup_window, text="Confirm and Proceed", command=lambda: self.open_simulation_window(name_entry.get(), difficulty_var.get(), setup_window)).pack(pady=20)

    def open_simulation_window(self, name, difficulty, setup_window):
        if name:
            setup_window.destroy()
            simulation_window = Toplevel(self.root)
            simulation_window.title("Simulation Control")
            simulation_window.geometry("400x300")

            start_button = Button(simulation_window, text="Start", bg='green', fg='white')
            start_button.pack(pady=10)

            stop_button = Button(simulation_window, text="Stop", bg='red', fg='white')
            stop_button.pack(pady=10)

            total_score_label = Label(simulation_window, text="Total Score: 0")
            total_score_label.pack(pady=20)

            def handle_shot():
                imgPath = good_score 
                score = calcScore(imgPath, difficulty)
                if score < 20:
                    self.total_score -= score
                elif score > 40:
                    self.total_score += score
                total_score_label.config(text=f"Total Score: {self.total_score}")

            shoot_button = Button(simulation_window, text="Shoot", command=handle_shot)
            shoot_button.pack(pady=10)

    def show_scores(self):
        scores_window = Toplevel(self.root)
        scores_window.title("Highscores")
        scores_window.geometry("400x300")
        scores_list = self.high_scores.get_scores()

        for difficulty in ["Easy", "Medium", "Hard", "Expert"]:
            Label(scores_window, text=f"{difficulty} Difficulty:", font=('Helvetica', 14, 'bold')).pack(pady=(10,0))
            for i, (name, score, diff) in enumerate(filter(lambda x: x[2] == difficulty, scores_list), start=1):
                Label(scores_window, text=f"{i}. {name}: {score}", bg='#f0f0f0').pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()