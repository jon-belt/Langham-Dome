import os

class HighScores:
    def __init__(self, filename='highscores.txt'):
        self.filename = filename
        self.scores = self.load_scores()

    def load_scores(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            return [tuple(map(str.strip, line.split(','))) for line in lines]

    def save_score(self, name, score):
        self.scores.append((name, str(score)))
        self.scores.sort(key=lambda x: int(x[1]), reverse=True)  # Sort scores in descending order
        with open(self.filename, 'w') as file:
            for name, score in self.scores:
                file.write(f'{name},{score}\n')

    def get_scores(self):
        return self.scores
