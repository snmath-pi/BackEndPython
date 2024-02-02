countryFile = open('countries.txt', 'r')
# print(countryFile.readable())
# print(countryFile.readline())

for files in countryFile.readlines():
    print(files, end="")
countryFile.close()
