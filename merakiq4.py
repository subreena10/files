# my_data_file=open("question3.txt","w")
# my_data_file.write("rishab-meerut\nnilima-cohin\nimitiyaz=delhi\nrati-shimla/nayishah-delhi\nraghu-shimla\nnaseer-kanpur/nkarthikeyan-delhi\nsalma-jaipur\npankaj-delhi\nbrijesh-delhi/ngovind-delhi\npuneet-shimla/nsiddhi-delhi\nsuman-jaipur\nrajeev-shimla\nmohindar-delhi\nrajendar-jaipur\npriyanka-shimla\nsashi-jaipur\nsarika-delhi\ndeepti-shimla\nharshad-delhi\ntrishna-raipur\npradeep-jaipur\nsekhar-delhi\nnand-delhi\nanoop-delhi\nbalwinder-tokyo")
# print(my_data_file)

my_data_file=open("question3.txt","r")
for data in my_data_file:
    if "delhi" in data:
        n_file=open("delhi.txt","a")
        n_file.write(data)
    elif "shimla" in data:
        s_file=open("shimla.txt","a")
        s_file.write(data)
    else:
        o_file=open("others_fie","a")
        o_file.write(data)
my_data_file.close()
