class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.a_times = a_times

    def top3(self):
        return self.a_times[0:3]
