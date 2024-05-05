import os

class HighScores:
    def __init__(self, filename='highscores.txt'):
        self.filename = filename
        print("HighScores initialized.")  # Debug print
        self.scores = self.load_scores()

    def load_scores(self):
        print("Loading scores...")  # Debug print
        if not os.path.exists(self.filename):
            print("File not found, creating new file.")
            open(self.filename, 'w').close()
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            return [tuple(line.strip().split(',')) for line in lines]

    def save_score(self, name, score, difficulty):
        self.scores.append((name, str(score), difficulty))
        # Sort scores assuming they are floats now
        self.scores.sort(key=lambda x: float(x[1]), reverse=True)
        with open(self.filename, 'w') as file:
            for entry in self.scores:
                file.write(','.join(entry) + '\n')

    def get_scores(self):
        print("Fetching scores...")  # Debug print
        return self.scores
