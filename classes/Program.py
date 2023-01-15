from classes.Sport import Sport
from datetime import datetime, timedelta


class Program:
    def __init__(self, athlete):
        # Data is not True because the goal is OOP.
        if athlete.age < 20:
            if athlete.weight <= 55:
                self.mountain_climber = Sport("Mountain Climber", 10)
                self.squats = Sport("Squats", 10)
                self.butt_bridge = Sport("Butt Bridge", 10)
                self.plank = Sport("Plank", 60)
            if 55 < athlete.weight < 70:
                self.mountain_climber = Sport("Mountain Climber", 12)
                self.squats = Sport("Squats", 12)
                self.butt_bridge = Sport("Butt Bridge", 12)
                self.plank = Sport("Plank", 90)
            if 70 <= athlete.weight:
                self.mountain_climber = Sport("Mountain Climber", 15)
                self.squats = Sport("Squats", 15)
                self.butt_bridge = Sport("Butt Bridge", 15)
                self.plank = Sport("Plank", 120)
        elif 20 <= athlete.age <= 45:
            if athlete.weight <= 55:
                self.mountain_climber = Sport("Mountain Climber", 14)
                self.squats = Sport("Squats", 14)
                self.butt_bridge = Sport("Butt Bridge", 14)
                self.plank = Sport("Plank", 105)
            if 55 < athlete.weight < 70:
                self.mountain_climber = Sport("Mountain Climber", 16)
                self.squats = Sport("Squats", 16)
                self.butt_bridge = Sport("Butt Bridge", 16)
                self.plank = Sport("Plank", 130)
            if 70 <= athlete.weight:
                self.mountain_climber = Sport("Mountain Climber", 20)
                self.squats = Sport("Squats", 20)
                self.butt_bridge = Sport("Butt Bridge", 20)
                self.plank = Sport("Plank", 150)
        elif 45 < athlete.age:
            if athlete.weight <= 55:
                self.mountain_climber = Sport("Mountain Climber", 12)
                self.squats = Sport("Squats", 12)
                self.butt_bridge = Sport("Butt Bridge", 12)
                self.plank = Sport("Plank", 90)
            if 55 < athlete.weight < 70:
                self.mountain_climber = Sport("Mountain Climber", 14)
                self.squats = Sport("Squats", 14)
                self.butt_bridge = Sport("Butt Bridge", 14)
                self.plank = Sport("Plank", 105)
            if 70 <= athlete.weight:
                self.mountain_climber = Sport("Mountain Climber", 16)
                self.squats = Sport("Squats", 16)
                self.butt_bridge = Sport("Butt Bridge", 16)
                self.plank = Sport("Plank", 130)
        self.start = datetime.now()
        self.day_list = []
        time = self.start
        for i in range(10):
            self.day_list.append(time.strftime("%y/%m/%d"))
            time += timedelta(days=3)

    def __str__(self):
        temp = ""
        for i in self.day_list:
            temp += f"""
            -{i}
                Mountain Climber: {self.mountain_climber.number} per round
                Squats: {self.squats.number} per round
                Butt Bridge: {self.butt_bridge.number} per round
                Plank: {self.plank.time}s
            """
        return (f"""
        ------------------------------
        {temp}
        ------------------------------
        """)
