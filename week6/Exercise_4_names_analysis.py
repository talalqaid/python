# Exercise 4: Count names and occurrences of a user-supplied name.

def main():
    names_file = open('names.txt', 'r')
    names = []
    for line in names_file:
        if line.strip() != '':
            names.append(line.strip())
    names_file.close()

    search = input('Enter the name to search for: ').strip()
    occurrences = 0
    for name in names:
        if name.lower() == search.lower():
            occurrences += 1

    print('Total number of names:', len(names))
    print(search, 'occurs', occurrences, 'time(s).')
main()
