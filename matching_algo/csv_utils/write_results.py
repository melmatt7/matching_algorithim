def write_results(res_data, file_name):
    f = open('../matching_algo/files/results'+file_name+".csv", 'w')
    
    for key in res_data.keys():
        f.write("%s," % key)
        for data in res_data[key]:
            f.write("%s," % data)

        f.write("\n")

    f.close()
