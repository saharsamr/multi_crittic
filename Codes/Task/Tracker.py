from Codes.Task.Utils.Directions import Dir

class Ttrial_info:
    def __init__(self, correct_answer, user_answer, user_confidence):
        self.correct_answer = correct_answer
        self.user_answer = user_answer
        self.user_confidence = user_confidence

class Tracker:
    def __init__(self, n_trials):
        self.n_trials = n_trials
        self.trials_info = []

    def add_trial_info(self, correct_answer, user_answer, user_confidence):
        self.trials_info.append(Ttrial_info(correct_answer, user_answer, user_confidence))

    @staticmethod
    def majority_voting(dots):
        n_right, n_left = 0, 0
        for dot in dots:
            if dot.move_direction == Dir.Right:
                n_right += 1
            else:
                n_left += 1
        return Dir.Right if n_right > n_left else Dir.Left
