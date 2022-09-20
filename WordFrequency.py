from itertools import count


text = open('sometext.txt','r')
mydict = dict()

def main():

    for line in text:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")

        for word in words:
            if word in mydict:
                mydict[word] = mydict[word] + 1
            else:
                mydict[word] = 1

            for key in list(mydict.keys()):
                print(key, ":", mydict[key])
main()

