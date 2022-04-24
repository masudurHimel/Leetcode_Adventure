class UndergroundSystem:

    def __init__(self):
        self.id = []
        self.duration_dict = {}
        self.flag_dict = {}
        self.res_dict = {}
        self.travel_count = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.duration_dict[id] = [(stationName, t)]
        self.flag_dict[id] = 1
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, end_station = self.duration_dict[id][0][0], stationName
        start_time, end_time = self.duration_dict[id][0][1], t
        self.duration_dict[id] = self.duration_dict[id].append((stationName, t))
        self.flag_dict[id] = 0
        travel_count = self.travel_count[f"{start_station}-{end_station}"] = self.travel_count.get(f"{start_station}-{end_station}", 0) + 1
        avg_time = (self.res_dict.get(f"{start_station}-{end_station}", 0.0) * (travel_count-1) + (end_time-start_time)) / travel_count
        self.res_dict[f"{start_station}-{end_station}"] = avg_time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.res_dict.get(f"{startStation}-{endStation}", 0.0)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)