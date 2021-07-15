class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        hh = self.hours if 9 < self.hours else f"0{self.hours}"
        mm = self.minutes if 9 < self.minutes else f"0{self.minutes}"
        ss = self.seconds if 9 < self.seconds else f"0{self.seconds}"
        return f"{hh}:{mm}:{ss}"

    def next_second(self):
        self.seconds += 1
        if Time.max_seconds < self.seconds:
            self.seconds %= Time.max_seconds + 1
            self.minutes += 1
        if Time.max_minutes <  self.minutes:
            self.minutes %= Time.max_minutes + 1
            self.hours += 1
        if Time.max_hours < self.hours:
            self.hours %= Time.max_hours + 1

        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
