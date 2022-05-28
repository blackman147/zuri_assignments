# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
   with open(filename) as f:
    lines = f.read()
    f.close()

    return lines


def count_words():
    text = read_file_content("/Users/blackman147/PycharmProjects/flask_docker/zuri_projects /Reading-Text-Files/story.txt")
    # [assignment] Add your code here
    values = text.split()
    word_count = {}
    for value in values:
        if value in word_count:
            word_count[value] = word_count.get(value) + 1
        else:
            word_count[value] = 1

    return word_count


print(count_words())