import ssl
import re
from pymongo import MongoClient

class ReadData():
    def __init__(self, year):
        """
        A class that takes the year as a string variable and returns a list of eiter the volume or incident information
        depending on which method is called. Constructor calls the database
        """
        self.year = year
        self.cluster = MongoClient("mongodb+srv://admin:admin@cluster0.s0bw3.mongodb.net/calgary_traffic_db?retryWrites=true&w=majority", ssl=True,
                        ssl_cert_reqs=ssl.CERT_NONE)
        self.db = self.cluster["calgary_traffic_db"]

    def read_volume(self):
        """Returns a list of all traffic volume data for that particular year"""
        collection = self.db['volume']
        volume_data = []
        for dataset in collection.find({'year': self.year}):
            if self.year == '2016':
                lat = dataset['the_geom'][30:37]
                lon = dataset['the_geom'][18:28]
            elif self.year == '2017':
                lat = dataset['the_geom'][34:46]
                lon = dataset['the_geom'][18:32]
            elif self.year == '2018':
                lat = dataset['the_geom'][38:55]
                lon = dataset['the_geom'][18:37]
            volume_data.append([dataset['year'],dataset['secname'],lat,lon,dataset['shape_leng'],dataset['volume']])
        return volume_data

    def read_incidents(self):
        """Returns a list of all incidents data for that particular year"""
        collection = self.db['incidents']
        incident_data = []
        for dataset in collection.find({'start_dt':{"$regex":self.year}}):
            incident_data.append([dataset['incident info'], dataset['description'], dataset['start_dt'],
                                    dataset['modified_dt'], dataset['quadrant'],dataset['longitude'],dataset['latitude']])
        return incident_data


def main():
    """Testing the methods"""
    r = ReadData('2018')
    print(r.read_volume()[0])

if __name__ == '__main__':
    main()
    
