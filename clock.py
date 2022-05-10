from datetime import datetime
import pytz

class worldClock:
    def __init__(self, city, timeZone):
        self.city = city;
        self.timeZone = pytz.timezone(timeZone);
        self.time = datetime.now(self.timeZone);

    def getTime(self):
        return self.time.strftime("%H:%M:%S");

NY = worldClock('New York','America/New_York');
SP = worldClock('São Paulo','America/Sao_Paulo');
London = worldClock('London','Europe/London');
Paris = worldClock('Paris','Europe/Paris');
Perth = worldClock('Perth','Australia/Perth');

array = [NY, SP, London, Paris, Perth];

for val in array:
    print("{}: {}".format(val.city, val.getTime()));