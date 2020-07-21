import ssl
import re
import folium
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
        for dataset in data:
            incident_dict[dataset[0]] = incident_dict.get(dataset[0], 0) + 1
        for key, value in incident_dict.items():
            incident_list.append([value, key])
        for incident in incident_list:
            for dataset in data:
                if (incident[1] == dataset[0]) and (len(incident)==2):
                    incident.append(dataset[4])
                    incident.append(dataset[5])
                    incident.append(dataset[6])
        incident_list.sort()
        incident_list.reverse()
        return incident_list

    def yearly_data(self, type):
        """Returns a list of maximum values for each year"""
        data_2016 = []
        data_2017 = []
        data_2018 = []
        year_2016 =0
        year_2017 =0
        year_2018 =0
        if type == 'Traffic Volume':
            data_2016 = self.sort_volume('2016')
            year_2016 = data_2016[0][5]
            data_2017 = self.sort_volume('2017')
            year_2017 = data_2017[0][5]
            data_2018 = self.sort_volume('2018')
            year_2018 = data_2018[0][5]
        else:
            data_2016 = self.sort_incidents('2016')
            year_2016 = data_2016[0][0]
            data_2017 = self.sort_incidents('2017')
            year_2017 = data_2017[0][0]
            data_2018 = self.sort_incidents('2018')
            year_2018 = data_2018[0][0]
        x = [year_2016,year_2017,year_2018]
        return x

    def draw_map(self, type, year):
        #Creating the map and plotting the points with the highest volume and most incidents
        map = folium.Map(location = [51.0447, -114.0719], zoom_start=12)
        max_cor = []
        if type == "Traffic Volume":
            data = self.sort_volume(year)
            max_vol = data[0][5]
            for year, sec, lat, lon, shap, vol in data:
                if vol == max_vol:
                    max_cor.append([float(lat), float(lon)])
            for lat, lon in max_cor:
                folium.Marker([lat,lon], popup='<strong>Maximum Traffic Volume</strong>').add_to(map)
        else:
            data = self.sort_incidents(year)
            max_acc = data[0][0]
            for dataset in data:
                if dataset[0] == max_acc:
                    max_cor.append([float(dataset[3]),float(dataset[4])])
            for lat, lon in max_cor:
                folium.Marker([lat,lon], popup='<strong>Maximum Traffic Incidents</strong>').add_to(map)
        #Generating the map
        map.save('CalgaryMap.html')

def main():
    """Testing the methods"""
    r = ReadData('2016')
    print(r.draw_map("else","2016"))

if __name__ == '__main__':
    main()