LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lang_freq = {}
text_freq = []
freq_table = []

def init_freq_table():
    with open('frequency-table.csv') as f:
        for line in f:
            freq_table.append(line.rstrip().split(","))

def letter_size(text):
    sum = 0
    for i in LETTERS:
        sum += text.count(i)
    return sum

def similarity_percent(lang):
    diff = 0

    for i in range(1,len(freq_table) - 1):
        diff += abs(text_freq[i] - lang_freq[lang][i])
    return "{}%".format(abs(round(100 - diff,2)))

def get_language(text):
    text_freq[:] = []

    for c in range(1,len(freq_table[0])):
        l = []
        for r in range(1,len(freq_table)):
            if freq_table[r][c][-1] == '%':
                l.append(float(freq_table[r][c][:-1]))
            else:
                l.append(float(freq_table[r][c]))
        lang_freq[freq_table[0][c]] = l

    #generate text's letter frequency
    TEXT_LENGTH = letter_size(text)
    for i in LETTERS:
        text_freq.append(text.count(i)/(TEXT_LENGTH * 1.0) * 100)

    #compare each lang's freq to the text's frequency
    min_dif = [10000000,10000000,10000000,10000000,10000000]
    min_dif_lang = ["","","","",""]
    for c in range(1,len(freq_table[0])):
        sum = 0
        for r in range(1,len(freq_table) - 1):
            sum += abs(text_freq[r] - lang_freq[freq_table[0][c]][r])
        for i in range(len(min_dif)):
            if sum < min_dif[i]:
                if i + 4 < len(min_dif):
                    min_dif[i + 4] = min_dif[i + 3]
                    min_dif_lang[i + 4] = min_dif_lang[i + 3]
                if i + 3 < len(min_dif):
                    min_dif[i + 3] = min_dif[i + 2]
                    min_dif_lang[i + 3] = min_dif_lang[i + 2]
                if i + 2 < len(min_dif):
                    min_dif[i + 2] = min_dif[i + 1]
                    min_dif_lang[i + 2] = min_dif_lang[i + 1]
                if i + 1 < len(min_dif):
                    min_dif[i + 1] = min_dif[i]
                    min_dif_lang[i + 1] = min_dif_lang[i]
                min_dif[i] = sum
                min_dif_lang[i] = freq_table[0][c]
                break

    result = ""
    for i in range(len(min_dif_lang)):
        result += "{}) {} - Similarity: {}\n".format(i + 1,min_dif_lang[i], similarity_percent(min_dif_lang[i]))

    return result
