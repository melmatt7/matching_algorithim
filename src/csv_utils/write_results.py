import csv

def write_results(res_data, file_name):
    f = open('files/results/'+file_name+".csv", 'w')
    
    for key in res_data.keys():
        f.write("%s, %s\n" % (key, res_data[key]))

    f.close()

