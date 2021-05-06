file_name = 'xcel.xlsx'
import pandas as pd
import re
import ntpath
import pickle

class Tdic(dict):
    def __setKV__(self, k, v):

        if k in self:
            del self[k]
        if v in self:
            del self[v]
        Tdic.__setKV__(self, k, v)
        Tdic.__setKV__(self, v, k)

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def dicCreator(d):
    f = open("dictfile", "wb")
    pickle.dump(d, f)
    f.close()

    with open("dictfile", "rb") as mafile:
        manewD = pickle.load(mafile)
    print(manewD)


def extractor():
    xl_workbook = pd.ExcelFile(file_name)  # Load the excel workbook
    df = xl_workbook.parse("Sheet")  # Parse the sheet into a dataframe
    aList = df['Path'].tolist()  # Cast the desired column into a python list
    aList = [item for item in aList if str(item) != 'nan']  # cleaning items with nan value
    d = Tdic()
    # print (len(aList))
    for x, i in enumerate(aList):
        #	print(i,x)
        #	if (i==nan):continue
        aList[x] = re.sub(r'.*C:', 'C:', i)
        #	print (cleaner('aList[x]','C:'))
        if re.search("C:", aList[x]):
            d[aList[x]] = path_leaf(aList[x])
    #	print(d[aList[x]])
    #	print(d[path_leaf(aList[x])])

    dicCreator(d)


def main():
    extractor()


if __name__ == '__main__':
    main()