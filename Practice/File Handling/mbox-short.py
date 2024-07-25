"""
Write a program that prompts for a file name, then opens that file and reads through the file, looking for
lines of the form: X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those
values and produce an output as shown below. Do not use the sum() function or a variable named sum in your
solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.
"""

fh = open('mbox-short.txt')
count = 0
sum = 0
lis = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        lis.append(line.strip().split(":")[1])  # taking the numbers after ":"
        print(line.strip())
        # word = line.strip().split(":")
        # words = word[1].lstrip()
        # # print(type(words))
        # print(words)
        # for w in words:
        #     lis.append(w)
        count += 1  # counting total lines
# print(count)
# print(lis)
for item in lis:
    item = float(item)
    sum = sum + item
# print(sum)
print("\nAverage spam confidence:", sum/count)
fh.close()
print("Done\n")


"""
Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From '
like the following line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address
of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""

fh = open('mbox-short.txt')
count = 0

for line in fh:
    if not line.startswith("From:"):
        continue
    else:
        print(line.strip().split(":")[1].lstrip())
        count += 1
fh.close()
print("There were", count, "lines in the file with From as the first word")


# Alternate Approach:
fh = open('mbox-short.txt')
count = 0
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    # print(wds[2])
    count += 1
fh.close()
print("\nThere were", count, "lines in the file with From as the first word\n")


"""
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail
messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the
mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
loop to find the most prolific committer.
"""

handle = open("mbox-short.txt")
counts = dict()
for line in handle:
    if not line.startswith("From:"):
        continue
    else:
        words = line.strip().split(":")[1].lstrip()
        # print(words)
        if words not in counts:
            counts[words] = counts.get(words, 0) + 1
        else:
            counts[words] += 1
print(counts)

big_count = None
big_word = None
for word, count in counts.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count

print(big_word, big_count)
handle.close()
print()


"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
04 3/ 06 1/ 07 1/ 09 2/ 10 3/11 6/ 14 1/ 15 2/ 16 4/ 17 2/ 18 1/ 19 1
"""

handle = open("mbox-short.txt")
counts = dict()
for line in handle:
    if line.startswith("From:"):
        continue
    elif not line.startswith("From"):
        continue
    else:
        # print(line.rstrip())
        words = line.strip().split(" ")[6].rstrip()
        word = words.split(":")[0]
        # print(word)
        if word not in counts:
            counts[word] = counts.get(word, 0) + 1
        else:
            counts[word] += 1
print(counts)
for key, value in sorted(counts.items()):
    print(key, value)
handle.close()
