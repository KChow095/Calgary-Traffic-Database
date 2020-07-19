import ssl
import re
from decimal import Decimal
from pymongo import MongoClient

class ReadData():
    def __init__(self, year):
        self.year = year
        self.cluster = MongoClient("mongodb+srv://admin:admin@cluster0.s0bw3.mongodb.net/calgary_traffic_db?retryWrites=true&w=majority", ssl=True,
                        ssl_cert_reqs=ssl.CERT_NONE)
        self.db = self.cluster["calgary_traffic_db"]

    def read_volume(self):
        collection = self.db['volume']
        volume_data = []
        for dataset in collection.find({'year': self.year}):
            lat = dataset['the_geom'][30:37]
            lon = dataset['the_geom'][18:28]
            volume_data.append([dataset['year'],dataset['secname'],lat,lon,dataset['shape_leng'],dataset['volume']])
        return volume_data

    def read_incidents(self):
        collection = self.db['incidents']
        incident_data = []
        for dataset in collection.find({'start_dt':{"$regex":self.year}}):
            incident_data.append([dataset['incident info'], dataset['description'], dataset['start_dt'],
                                    dataset['modified_dt'], dataset['quadrant'],dataset['longitude'],dataset['latitude']])
        return incident_data


def main():
    r = ReadData('2016')
    print(r.read_incidents())

if __name__ == '__main__':
    main()
    
