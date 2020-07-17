import csv
import ssl
from pymongo import MongoClient


# processes the data in a traffic volume csv and ingests the data into a database
def process_volume_file(file_name):
    with open(file_name) as file:
        # creates a reader object to allow for iteration of each row
        reader = csv.reader(file)

        # prepares header names for database ingestion
        header_list = process_volume_header(next(reader))
        header_order = ["year", "secname", "the_geom", "shape_leng", "volume"]

        # stores the document objects represented as a dictionary into a list
        db_write_list = []

        # iterate through each row in the csv file
        for row in reader:
            # creates a tuple pairing between header and current csv row
            tup_list = list(zip(header_list, row))
            # converts the tuple list into a dictionary
            row_dict = dict(tup_list)

            # organizes the data into the proper header order
            document = {}
            for header in header_order:
                document[header] = row_dict[header]

            # adds row data as dictionary object into db_write_list
            db_write_list.append(document)

        # connect and ingest data into database
        ingest_data_into_db(db_write_list, "volume")


# formats the header names in a volume csv file
def process_volume_header(headers):
    # list containing standardized header names in the original csv header order
    header_list = []

    # iterate through each header and standardize header name
    for header in headers:
        # removes any whitespace before and after string input and converts to lowercase
        header = header.strip().lower()

        # checks for a match in header name and appends the standardized name
        if header == "year" or header == "year_vol":
            header_list.append("year")
        elif header == "secname" or header == "segment_name":
            header_list.append("secname")
        elif header == "the_geom" or header == "multilinestring":
            header_list.append("the_geom")
        elif header == "shape_leng" or header == "length_m":
            header_list.append("shape_leng")
        elif header == "volume":
            header_list.append("volume")

    # returns a list of the standardized header names
    return header_list


# processes the data in a traffic incidents csv and ingests the data into a database
def process_incidents_file(file_name):
    with open(file_name) as file:
        # creates a reader object to allow for iteration of each row
        reader = csv.reader(file)

        # prepares header names for database ingestion
        header_list = process_incidents_header(next(reader))
        header_order = ["incident info", "description", "start_dt", "modified_dt", "quadrant", "longitude", "latitude", "location", "count"]

        # stores the document objects represented as a dictionary into a list
        db_write_list = []

        # iterate through each row in the csv file
        for row in reader:
            # creates a tuple pairing between header and current csv row
            tup_list = list(zip(header_list, row))
            # converts the tuple list into a dictionary
            row_dict = dict(tup_list)

            # organizes the data into the proper header order
            document = {}
            for header in header_order:
                document[header] = row_dict[header]

            # adds row data as dictionary object into db_write_list
            db_write_list.append(document)

        # connect and ingest data into database
        ingest_data_into_db(db_write_list, "incidents")


# formats the header names in an incidents csv file
def process_incidents_header(headers):
    # list containing standardized header names in the original csv header order
    header_list = []

    # iterate through each header and standardize header name
    for header in headers:
        # removes any whitespace before and after string input and converts to lowercase
        header = header.strip().lower()

        # appends header to list
        header_list.append(header)

    # returns a list of the standardized header names
    return header_list


# connects to a MongoDB database and ingests data
def ingest_data_into_db(documents, collection_name):
    # connects to the MongoDB machine cluster
    cluster = MongoClient(
        "mongodb+srv://admin:admin@cluster0.s0bw3.mongodb.net/calgary_traffic_db?retryWrites=true&w=majority", ssl=True,
        ssl_cert_reqs=ssl.CERT_NONE)

    # specifying the database and collection to connect to
    db = cluster["calgary_traffic_db"]
    collection = db[collection_name]

    # writes documents to database
    collection.insert_many(documents)


def main():
    """
    ONLY RUN THIS ONCE AS IT WILL CREATE MULTIPLE ENTRIES INTO THE DATABASE
    """
    # process_volume_file("TrafficFlow2016_OpenData.csv")
    # process_volume_file("2017_Traffic_Volume_Flow.csv")
    # process_volume_file("Traffic_Volumes_for_2018.csv")
    #
    # process_incidents_file("Traffic_Incidents_Archive_2016.csv")
    # process_incidents_file("Traffic_Incidents_Archive_2017.csv")


if __name__ == "__main__":
    main()