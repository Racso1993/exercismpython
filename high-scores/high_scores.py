class HighScores:
    def __init__(self, scores):
        self._scores = scores
        
    def scores(self):
        return self._scores
    
    def highest(self):
        return max(self._scores)
    def top(self):
        a=sorted(self._scores)
        a.reverse()
        return a[0:3]
    def latest(self):
        return self._scores[-1]
    def report(self):
        if self._scores[-1] == max(self._scores):
            return "Your latest score was {}. That's your personal best!".format(self._scores[-1])
        else:
            return "Your latest score was {}. That's {} short of your personal best!".format(self._scores[-1],max(self._scores)-int(self._scores[-1]))
