from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize,sent_tokenize

f = open("speechnotes.txt","r")
f1 = open("imagenotes.txt","r")
s = f.read()
s1 = f1.read()
textimage = s1
textspeech = s

def summarizer(text,file):
    port = PorterStemmer()
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)
   # print(text)
    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[port.stem(word)] += 1
        else:
            freqTable[port.stem(word)] = 1

    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        words_in_sentence = word_tokenize(sentence.lower())
    
        for w in words_in_sentence:
            w = w.lower()
            w = port.stem(w)
    
        for w in freqTable:
            if w in words_in_sentence:
                if sentence in sentenceValue:
                     sentenceValue[sentence] += freqTable[w]
                else:
                    sentenceValue[sentence] = freqTable[w]

    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
    average = int(sumValues/ (len(sentenceValue)+1))
    threshold = 1.2 * average

    summary = ''
    for sentence in sentences:
            if sentence in sentenceValue and sentenceValue[sentence] > threshold:
                summary +=  " " + sentence
    fsave = open(file+".txt","w+")
    fsave.write(summary)
    fsave.close()
    #print(summary)

def summ():
    summarizer(textimage,"imgnotessumm")
    summarizer(textspeech,"speechotessumm")
