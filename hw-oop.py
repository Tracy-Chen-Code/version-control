import numpy as np
from scipy.stats import norm


class SignalDetection:
    def __init__(self,hits, misses, falseAlarms, correctRejections):
        self.hits=hits
        self.misses=misses
        self.falseAlarms=falseAlarms
        self.correctRejection=correctRejections

    def hit_rate(self):
        total_signals = self.hits + self.misses 
        return self.hits/total_signals

        

    def false_alarm_rate(self):
        total_noises = self.falseAlarms + self.correctRejection
        return self.falseAlarms/total_noises
        

    def d_prime(self):
        return norm.ppf(self.hit_rate()) - norm.ppf(self.false_alarm_rate())



    def criterion(self):
        return -0.5 * (norm.ppf(self.hit_rate()) + norm.ppf(self.false_alarm_rate()))