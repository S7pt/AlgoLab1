class Perforator:
    def __init__(self, color, revolutions_per_minute, stroke_frequency, producer_name):
        self.color = color
        self.revolutions_per_minute = int(revolutions_per_minute)
        self.stroke_frequency = int(stroke_frequency)
        self.producer_name = producer_name

    def __repr__(self):
        return f"color: {self.color}, RPM: {self.revolutions_per_minute}," \
               f" stroke frequency: {self.stroke_frequency}, producer name: {self.producer_name} \n"
