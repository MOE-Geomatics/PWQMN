# 1. The starting point is a Access Database and a shape file. 
# Firstly, extract the 11 table from Access to tab separated txt file.
# 2. Run the following script.
# Python PWQMN.py > 1.txt

class PWQMNStation:
    def __init__(self, STATION):
        self.STATION = STATION
        self.PPUT = {}
        self.NNOTUR = {}
        self.CLIDUR = {}
        self.RSP = {}
    def addPPUT(self, date, value):
        if self.PPUT.has_key(date):
            self.PPUT[date] = self.PPUT[date] + "," + value
        else:
            self.PPUT[date] = value
    def addNNOTUR(self, date, value):
        if self.NNOTUR.has_key(date):
            self.NNOTUR[date] = self.NNOTUR[date] + "," + value
        else:
            self.NNOTUR[date] = value
    def addCLIDUR(self, date, value):
        if self.CLIDUR.has_key(date):
            self.CLIDUR[date] = self.CLIDUR[date] + "," + value
        else:
            self.CLIDUR[date] = value
    def addRSP(self, date, value):
        if self.RSP.has_key(date):
            self.RSP[date] = self.RSP[date] + "," + value
        else:
            self.RSP[date] = value
    def __str__(self):
        available = len(self.CLIDUR) + len(self.NNOTUR) + len(self.PPUT) + len(self.RSP)
        #str1 = "INSERT INTO PWQMN_DATA VALUES ("
        str1 = ""
#        str1 = str1 + "\"" + self.STATION + "\"" + "," + str(len(self.CLIDUR)) + "," + str(len(self.NNOTUR)) + "," + str(len(self.PPUT)) + "," + str(len(self.RSP))  + "," + str(available)
        str1 = str1 + self.STATION + "," + str(len(self.CLIDUR)) + "," + str(len(self.NNOTUR)) + "," + str(len(self.PPUT)) + "," + str(len(self.RSP))  + "," + str(available)
        str2 = "";
        for key in sorted(self.CLIDUR.iterkeys()):
            value = self.CLIDUR[key]
            if not ("," in value):
                arr = [value]
            else:
                arr = value.split(",")
            for value in arr:
                if len(value) > 0 and value[-1] == "0":
                    value = value[:-1]
                if len(value) > 0 and value[-1] == "0":
                    value = value[:-1]
                if len(value) > 0 and value[-1] == ".":
                    value = value[:-1]
                str2 = str2 + key + ":" + value + ";"
 
        str1 = str1 + "," + str(len(str2)) + "," + str2[:-1]
 
        str2 = "";
        for key in sorted(self.NNOTUR.iterkeys()):
            value = self.NNOTUR[key]
            if not ("," in value):
                arr = [value]
            else:
                arr = value.split(",")
            for value in arr:
                if len(value) > 0 and value[-1] == "0":
                    value = value[:-1]
                if len(value) > 0 and value[-1] == "0":
                    value = value[:-1]
                if len(value) > 0 and value[-1] == ".":
                    value = value[:-1]
                str2 = str2 + key + ":" + value + ";"
 
        #str1 = str1 + "\t" + str(len(str2)) + "\t" + str2[:-1]
        str1 = str1 + "," + str(len(str2)) + "," + str2[:-1]
        str2 = "";
        for key in sorted(self.PPUT.iterkeys()):
            value = self.PPUT[key]
            if not ("," in value):
                arr = [value]
            else:
                arr = value.split(",")
            for value in arr:
                if len(value) > 0 and value[-1] == "0":
                    value = value[:-1]
                if len(value) > 0 and value[-1] == "0":
                    value = value[:-1]
                if len(value) > 0 and value[-1] == ".":
                    value = value[:-1]
                str2 = str2 + key + ":" + value + ";"
 
        #tr1 = str1 + "\t" + str(len(str2)) + "\t" + str2[:-1]
        str1 = str1 + "," + str(len(str2)) + "," + str2[:-1]
        str2 = "";
        for key in sorted(self.RSP.iterkeys()):
            value = self.RSP[key]
            if not ("," in value):
                arr = [value]
            else:
                arr = value.split(",")
            for value in arr:
                if len(value) > 0 and value[-1] == "0":
                    value = value[:-1]
                if len(value) > 0 and value[-1] == "0":
                    value = value[:-1]
                if len(value) > 0 and value[-1] == ".":
                    value = value[:-1]
                str2 = str2 + key + ":" + value + ";"
 
        #str1 = str1 + "\t" + str(len(str2)) + "\t" + str2[:-1]
        str1 = str1 + "," + str(len(str2)) + "," + str2[:-1]
        return str1 #+ ");"
class PWQNMDataSet:
    def __init__(self):
        self.PWQMNStations = {}
    def addData(self, inputFile, yearInput):
        import fileinput
        i = 0
        for line in fileinput.input(inputFile):
            i = i + 1
            if i < 2:
                continue
            items = line.strip().split("\t")
            PARM = items[1][1:-1]
            if not (PARM in ["PPUT", "NNOTUR", "CLIDUR", "RSP"]):
                continue
            #print line.strip()
            #if True:
            #    continue
            STATION = items[0][1:-1]
            DATE = items[3] #14/1/2002
            strs = DATE.split("/")
            year = strs[2][2:-8]
            month = strs[1]
            if len(month) == 1:
                month = "0" + month
            day = strs[0]
            if len(day) == 1:
                day = "0" + day
            DATE = year + month + day
            VALUE = items[7]
            if (yearInput == 2011):
                VALUE = items[6]
            #print VALUE
            if self.PWQMNStations.has_key(STATION):
                #self.PWQMNStations[STATION] = self.PWQMNStations[STATION] + line
                station = self.PWQMNStations[STATION]
                if (PARM == "PPUT"):
                    station.addPPUT(DATE, VALUE)
                if (PARM == "NNOTUR"):
                    station.addNNOTUR(DATE, VALUE)
                if (PARM == "CLIDUR"):
                    station.addCLIDUR(DATE, VALUE)
                if (PARM == "RSP"):
                    station.addRSP(DATE, VALUE)
            else:
                station = PWQMNStation(STATION)
                if (PARM == "PPUT"):
                    station.addPPUT(DATE, VALUE)
                if (PARM == "NNOTUR"):
                    station.addNNOTUR(DATE, VALUE)
                if (PARM == "CLIDUR"):
                    station.addCLIDUR(DATE, VALUE)
                if (PARM == "RSP"):
                    station.addRSP(DATE, VALUE)
                self.PWQMNStations[STATION] = station
        #print len(self.PWQMNStations)
    def __str__(self):
        #result = "STATION\tCHLORIDE\tNITRATES\tPHOSPHORUS\tSUS_SOLIDS\tAVAILABLE\tCHLORIDE_LEN\tCHLORIDE_CONT\tNITRATES_LEN\tNITRATES_CONT\tPHOSPHORUS_LEN\tPHOSPHORUS_CONT\tSUSPENDED_SOLIDS_LEN\tSUSPENDED_SOLIDS_CONT\n"
        #result = "CREATE TABLE PWQMN_DATA ( STATION  varchar(255), CHLORIDE int, NITRATES int, PHOSPHORUS int, SUS_SOLIDS int, AVAILABLE int, CHLORIDE_LEN int, CHLORIDE_CONT  varchar2(4000), NITRATES_LEN int, NITRATES_CONT  varchar2(4000), PHOSPHORUS_LEN int, PHOSPHORUS_CONT  varchar2(4000), SUSPENDED_SOLIDS_LEN int, SUSPENDED_SOLIDS_CONT  varchar2(4000));\n"
        result = "STATION,CHLORIDE,NITRATES,PHOSPHORUS,SUS_SOLIDS,AVAILABLE,CHLORIDE_LEN,CHLORIDE_CONT,NITRATES_LEN,NITRATES_CONT,PHOSPHORUS_LEN,PHOSPHORUS_CONT,SUSPENDED_SOLIDS_LEN,SUSPENDED_SOLIDS_CONT\n"
        for key, value in self.PWQMNStations.items():
            result = result + str(value) + "\n"
        return result
 
if __name__ == "__main__":
    pwqmn = PWQNMDataSet()
    #for year in range(2002, 2012, 1):
    for year in range(2002, 2012, 1):
        pwqmn.addData('PWQMN_' + str(year) + '_rawdata.txt', year)
    print pwqmn
    #handle1 = open("1.txt",'w+')
    #handle1.write(str(stations))
    #handle1.close();
    #stations.getTable();