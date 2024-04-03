import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    docs = [line.lower().split() for line in text.split('\n')]

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    calculated = {}

    def countTF(word, line):
      counter = 0

      if len(line) == 0:
         return  0.0
      
      for w in line:
         if (w == word):
          counter = counter + 1
      # counter = line.count(word)

      return counter/len(line)
    
    def countDF(word, lines):
      counter = 0

      if len(lines) == 0:
         return 0.0
      
      for line in lines:
          if word in line:
             counter = counter + 1
      # counter = sum(1 for line in lines if word in line)
             
      return counter/len(lines)
       

    for index, line in enumerate(docs):
        calculated[index] = dict()
        unique_words = set(line)
        
        for unique_word in unique_words:
          count_term = countTF(unique_word, line)
          count_document = countDF(unique_word, docs)
          calculated[index][unique_word] = {"tf": count_term, "df": count_document}

    # for i in calculated:
    #    print(calculated[i])

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector
    counted = []
    
    for index, line in enumerate(docs):
      line_tf_idf = []
      
      for word in line:
        word_tf = calculated[index][word]["tf"]
        word_idf = np.log10(np.divide(1,calculated[index][word]["df"]))
        word_tf_idf = word_tf * word_idf
        line_tf_idf.append(word_tf_idf)

      counted.append(line_tf_idf)

    # print(counted)
       
    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.
    def distance(row1, row2):
      sum = 0
      
      for i in range(min(len(row1), len(row2))):
          sum += abs(row1[i] - row2[i])
      
      if sum > 0:
          return sum
      return np.inf
    
    def all_pairs(data):
      dist = [[distance(sent1, sent2) for sent1 in data] for sent2 in data]
      return dist

    def find_nearest_pair(data):
        N = len(data)
        dist = np.empty((N, N), dtype=float)
        dist = np.array(all_pairs(data))
        # print(dist)
        print(np.unravel_index(np.argmin(dist), dist.shape))

    find_nearest_pair(counted)
main(text)
