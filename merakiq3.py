# file=open("file.question.txt","x")
# print(file)
# file.close()

file=open("file.question.txt","w")
# banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
# i=0
# while i < len(banks_list):
#     print(banks_list[i])
#     i+=1
file.write("Kotak\nHDFC\nRBL\nSBI\nBank of Baroda")
print(file)
file.close()