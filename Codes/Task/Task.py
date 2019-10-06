import random
from psychopy import visual, event, core
from Codes.Task.Objects.Dot import Dot
from Codes.Task.Utils.Directions import Dir


black = [-1, -1, -1]
white = [1, 1, 1]


class Task:
    def __init__(self, n_trials=100 ,scr_size=(800, 800), n_dots=200, max_step_size=10):
        self.n_trials = n_trials
        self.n_dots = n_dots
        self.max_step_size = max_step_size
        self.win = visual.Window(size=scr_size, units="pix", fullscr=False)

    def run_task(self):
        for _ in range(self.n_trials):
            self.dots = [Dot([random.uniform(-400, 400), random.uniform(-400, 400)])
                         for _ in range(self.n_dots)]
            self.fixation()
            self.random_dot_motion()
            self.select_direction()
            self.get_confidence()

    def fixation(self):
        visual.TextStim(win=self.win, text="+", color=[0, 1, 0], pos=[500, 0]).draw()
        self.win.flip()
        Task.delay(0.5)

    def random_dot_motion(self):
        clock = core.Clock()
        while clock.getTime() < 2.0:
            visual.ElementArrayStim(
                win=self.win,
                nElements=self.n_dots,
                elementTex=None,
                elementMask="circle",
                xys=[dot.xy for dot in self.dots],
                sizes=10
            ).draw()
            self.win.flip()
            self.move_dots()

    def move_dots(self):
        for dot in self.dots:
            if dot.move_direction == Dir.Right:
                dot.xy[0] += random.random() * self.max_step_size
            else:
                dot.xy[0] -= random.random() * self.max_step_size

    def select_direction(self):
        visual.TextStim(
            self.win,
            text="select the direction, which most of the dots are moving forward.",
            pos=(200,200)
        ).draw()
        visual.ImageStim(
            self.win,
            image='/Users/sadegh/Desktop/multi-critic/images/arrow_key.jpg',
            size=100, ori=90.0, pos=[200, -100]
        ).draw()
        visual.ImageStim(
            self.win,
            image='/Users/sadegh/Desktop/multi-critic/images/arrow_key.jpg',
            size=100, ori=270.0, pos=[-200, -100]
        ).draw()
        self.win.flip()
        return event.waitKeys(keyList=["left", "right"])

    def get_confidence(self):
        visual.TextStim(self.win, text='1', pos=[250, -100], color=black).draw()
        visual.TextStim(self.win, text='2', pos=[350, -100], color=black).draw()
        visual.TextStim(self.win, text='3', pos=[450, -100], color=black).draw()
        visual.TextStim(self.win, text='4', pos=[550, -100], color=black).draw()
        visual.TextStim(self.win, text='5', pos=[650, -100], color=black).draw()
        visual.TextStim(self.win, text='6', pos=[750, -100], color=black).draw()
        self.win.flip()
        return event.waitKeys(keyList=["1", "2", "3", "4", "5", "6"])

    @staticmethod
    def delay(ms):
        clock = core.Clock()
        while clock.getTime() < ms:
            pass


