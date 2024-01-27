import csv

# opens file csv and reads the alphabet
with open("nato_phonetic_alphabet.csv") as nato:
  data = csv.reader(nato)
  dic = {key: value for (key, value) in data}

# takes a word from user
name = input("Enter a word: ").upper()


# searches through the alphabet by users word
done = [dic[l] for l in name]

print(done)