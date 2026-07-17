class TimeMap:

    def __init__(self):
        self.timestamp_dict = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timestamp_dict.keys():
            self.timestamp_dict[key][timestamp] = value 
        else:
            self.timestamp_dict[key] = { timestamp: value }
                

    def get(self, key: str, timestamp: int) -> str:
        timestamp_value = self.timestamp_dict.get(key, {})
        # print(timestamp_value)
        while timestamp >= 0:
            if timestamp in timestamp_value.keys():
                return timestamp_value[timestamp]
            timestamp -= 1
        return ""


