from calculations import calcScore
from highscores import HighScores
import tkinter as tk
from tkinter import Toplevel, Label, Entry, Radiobutton, IntVar, Button

## Linux only PI module, does not work on my main desktop so this stays commented out whilst working from it
# from picamera2 import Picamera2, Preview 

# def takePic(i):
#     picam2 = Picamera2() 
#     camera_config = picam2.create_preview_configuration() 
#     picam2.configure(camera_config) 
#     picam2.start_preview(Preview.QTGL) 
#     picam2.start()

#     path = ("captures/"+i+".jpg") 

#     picam2.capture_file(path) 
#     picam2.close()

#     return(path)

# class GameApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Langham Dome Training Simulator")
#         self.root.geometry("400x300")
#         self.high_scores = HighScores()
#         self.total_score = 0
#         self.i = 0

#         self.menu_frame = tk.Frame(self.root, bg='#252A5B')
#         self.menu_frame.pack(expand=True, fill='both')

#         self.start_button = tk.Button(self.menu_frame, text="Start Game", command=self.start_game, height=2, width=20, bg='#FFC700', fg='black', font=('Helvetica', 10, 'bold'), bd=3, relief="solid")
#         self.start_button.pack(pady=10)

#         self.scores_button = tk.Button(self.menu_frame, text="Highscores", command=self.show_scores, height=2, width=20, bg='#FFC700', fg='black', font=('Helvetica', 10, 'bold'), bd=3, relief="solid")
#         self.scores_button.pack(pady=10)

#         self.quit_button = tk.Button(self.menu_frame, text="Quit", command=self.root.quit, height=2, width=20, bg='#FFC700', fg='black', font=('Helvetica', 10, 'bold'), bd=3, relief="solid")
#         self.quit_button.pack(pady=10)

#     def start_game(self):
#         setup_window = Toplevel(self.root)
#         setup_window.title("Game Setup")
#         setup_window.geometry("400x300")
#         setup_window.configure(bg='#252A5B')

#         Label(setup_window, text="Enter your name:", bg='#252A5B', fg='#FFC700').pack(pady=(20, 0))
#         name_entry = Entry(setup_window)
#         name_entry.pack(pady=(0, 20))

#         Label(setup_window, text="Select Difficulty:", bg='#252A5B', fg='#FFC700').pack()
#         difficulty_var = IntVar(value=0)
#         difficulties = ["Easy", "Medium", "Hard", "Expert"]

#         for index, difficulty in enumerate(difficulties):
#             Radiobutton(setup_window, text=difficulty, variable=difficulty_var, value=index, bg='#252A5B', fg='#FFC700', selectcolor='#252A5B').pack()

#         Button(setup_window, text="Confirm and Proceed", 
#                command=lambda: self.open_simulation_window(name_entry.get(), difficulties[difficulty_var.get()], setup_window), bg='#FFC700', fg='black', font=('Helvetica', 10, 'bold'), bd=3, relief="solid").pack(pady=20)

#     def open_simulation_window(self, name, difficulty, setup_window):
#         setup_window.destroy()
#         simulation_window = Toplevel(self.root)
#         simulation_window.title("Simulation Control")
#         simulation_window.geometry("400x300")
#         simulation_window.configure(bg='#252A5B')

#         state_label = Label(simulation_window, text="State: Waiting", bg='#252A5B', fg='#FFC700')
#         state_label.pack(pady=10)

#         start_button = Button(simulation_window, text="Start", bg='green', fg='white',
#                               command=lambda: self.start_simulation(start_button, stop_button, shoot_button, state_label))
#         start_button.pack(pady=10)

#         stop_button = Button(simulation_window, text="Stop", bg='red', fg='white', state='disabled',
#                              command=lambda: self.stop_simulation(simulation_window, state_label, name, difficulty))
#         stop_button.pack(pady=10)

#         shoot_button = Button(simulation_window, text="Shoot", state='disabled',
#                               command=lambda: self.handle_shot(difficulty, total_score_label))
#         shoot_button.pack(pady=10)

#         total_score_label = Label(simulation_window, text="Total Score: 0", bg='#252A5B', fg='#FFC700')
#         total_score_label.pack(pady=20)

#     def start_simulation(self, start_button, stop_button, shoot_button, state_label):
#         start_button.config(state='disabled')
#         stop_button.config(state='normal')
#         shoot_button.config(state='normal')
#         state_label.config(text="State: Simulation")

#     def stop_simulation(self, simulation_window, state_label, name, difficulty):
#         state_label.config(text="State: Finishing")
#         self.high_scores.save_score(name, self.total_score, difficulty)
#         self.show_final_score(simulation_window, name)

#     def handle_shot(self, difficulty, total_score_label):
#         self.i = self.i+1
#         #imgPath = takePic(self.i)

#         difficulties = ["Easy", "Medium", "Hard", "Expert"]
#         difficulty_index = difficulties.index(difficulty)  # convert string to an index

#         score = calcScore(imgPath, difficulty_index)
#         if score < 20:
#             self.total_score -= score
#         elif score > 40:
#             self.total_score += score
#         total_score_label.config(text=f"Total Score: {self.total_score}")

#     def show_final_score(self, simulation_window, name):
#         final_score_window = Toplevel(self.root)
#         final_score_window.title("Final Score")
#         final_score_window.geometry("300x200")
#         final_score_window.configure(bg='#252A5B')

#         Label(final_score_window, text=f"{name}, your final score: {self.total_score}", bg='#252A5B', fg='#FFC700').pack(pady=20)
#         Button(final_score_window, text="Next...", command=lambda: self.close_simulation(simulation_window, final_score_window), bg='#FFC700', fg='black', font=('Helvetica', 10, 'bold'), bd=3, relief="solid").pack(pady=20)

#     def close_simulation(self, simulation_window, final_score_window):
#         final_score_window.destroy()
#         simulation_window.destroy()

#     def show_scores(self):
#         scores_window = Toplevel(self.root)
#         scores_window.title("Highscores")
#         scores_window.geometry("400x300")
#         scores_window.configure(bg='#252A5B')

#         scores_list = self.high_scores.get_scores()

#         for index, difficulty in enumerate(["Easy", "Medium", "Hard", "Expert"]):
#             Label(scores_window, text=f"{difficulty} Difficulty:", font=('Helvetica', 14, 'bold'), bg='#252A5B', fg='#FFC700').pack(pady=(10, 0))
#             filtered_scores = [score for score in scores_list if score[2] == difficulty]
#             for i, (name, score, diff) in enumerate(filtered_scores, start=1):
#                 Label(scores_window, text=f"{i}. {name}: {score}", bg='#252A5B', fg='#FFC700').pack()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = GameApp(root)
#     root.mainloop()

testImg1 = "imgs/3dots.png"
testImg2 = "imgs/3dots2.png"
testImg3 = "imgs/bad_score.png"
testImg4 = "imgs/good_score.png"
testImg5 = "imgs/reticule.png"
testImg6 = "imgs/reticuleAndDot.png"