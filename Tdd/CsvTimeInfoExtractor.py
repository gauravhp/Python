import csv
import os

IP_FILENAME = os.path.join(os.path.dirname(__file__), '/Users/gaparmar/slc15dvo/combined.csv')
OP_FILENAME = os.path.join(os.path.dirname(__file__), '/Users/gaparmar/slc15dvo/final.csv')

class time_info:
    def __init__(self,taskname, minutes, seconds):
        self.task_name = taskname
        self.minutes = minutes
        self.seconds = seconds

class ExtractTargetTimingsFromsCsv:
    csv_data = []

    def intialize_csv_data(self):
        with open(IP_FILENAME) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                time_info_row = row[1].split(" ")
                if(time_info_row[1]=="secs."):
                    timeinfo = time_info(row[0],0,time_info_row[0])
                    self.csv_data.append(timeinfo)
                else:
                    timeinfo = time_info(row[0],time_info_row[0],time_info_row[2])
                    self.csv_data.append(timeinfo)
        return self.csv_data

    def get_time_info_as_string(self, timeinfo):
        return timeinfo.task_name + "," + str(timeinfo.minutes) + "," + str(timeinfo.seconds) + "\n"

    def remove_file_if_it_exists(self):
        if os.path.exists(OP_FILENAME):
            os.remove(OP_FILENAME)

    def write_csv_to_file(self):
        output_file= open(OP_FILENAME, "a")
        output_file

        with open(OP_FILENAME, 'w', newline='') as file:
            for timeinfo in self.csv_data:
                output_file.write(ExtractTargetTimingsFromsCsv.get_time_info_as_string(self,timeinfo))

        output_file.close()
        return

extractTargetTimingsFromsCsv = ExtractTargetTimingsFromsCsv()

if __name__ == '__main__':
    extractTargetTimingsFromsCsv.intialize_csv_data()
    extractTargetTimingsFromsCsv.write_csv_to_file()

