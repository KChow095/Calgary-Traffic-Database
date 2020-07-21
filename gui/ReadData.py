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

    def read_volume(self, year):
        """Returns a list of all traffic volume data for that particular year"""
        collection = self.db['volume']
        volume_data = []
        for dataset in collection.find({'year': year}):
            if year == '2016':
                lat = dataset['the_geom'][30:37]
                lon = dataset['the_geom'][18:28]
            elif year == '2017':
                lat = dataset['the_geom'][34:46]
                lon = dataset['the_geom'][18:32]
            elif year == '2018':
                lat = dataset['the_geom'][38:55]
                lon = dataset['the_geom'][18:37]
            volume_data.append([dataset['year'],dataset['secname'],lat,lon,dataset['shape_leng'],int(dataset['volume'])])
        return volume_data

    def read_incidents(self, year):
        """Returns a list of all incidents data for that particular year"""
        collection = self.db['incidents']
        incident_data = []
        for dataset in collection.find({'start_dt':{"$regex":year}}):
            incident_data.append([dataset['incident info'], dataset['description'], dataset['start_dt'],
                                    dataset['modified_dt'], dataset['quadrant'],dataset['latitude'], dataset['longitude']])
        return incident_data
    
    def sort_volume(self, year):
        """Method to call to sort the lists based on the volume with the largest number first, returns a sorted list"""
        data = self.read_volume(year)
        data.sort(key = lambda x:x[5])
        data.reverse()
        return data
    
    def sort_incidents(self,year):
        """Method to call when to retrieve a list of locations where the most incidents happen"""
        data = self.read_incidents(year)
        incident_dict = {}
        incident_list = []
        for info, descp, start, modified, quad, lati, longi in data:
            incident_dict[info] = incident_dict.get(info, 0) + 1
        for key, value in incident_dict.items():
            key = key.strip('.')
            incident_list.append([value, key, key[-2:]])
        incident_list.sort()
        incident_list.reverse()
        return incident_list

    def yearly_data(self, type):
        """Returns a list of total counts for each year"""
        data_2016 = []
        data_2017 = []
        data_2018 = []
        year_2016 =0
        year_2017 =0
        year_2018 =0
        if type == 'Traffic Volume':
            data_2016 = self.read_volume('2016')
            data_2017 = self.read_volume('2017')
            data_2018 = self.read_volume('2018')
            for dataset in data_2016:
                year_2016 += dataset[5]
            for dataset in data_2017:
                year_2017 += dataset[5]
            for dataset in data_2018:
                year_2018 += dataset[5]
        else:
            data_2016 = self.sort_incidents('2016')
            data_2017 = self.sort_incidents('2017')
            data_2018 = self.sort_incidents('2018')
            for dataset in data_2016:
                year_2016 += dataset[0]
            for dataset in data_2017:
                year_2017 += dataset[0]
            for dataset in data_2018:
                year_2018 += dataset[0]
        x = [year_2016,year_2017,year_2018]
        return x

def main():
    """Testing the methods"""
    r = ReadData('2018')
    print(r.yearly_data("hello"))

if __name__ == '__main__':
    main()
    
