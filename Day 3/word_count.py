def words(A):
    wordlist = A.split()
    word_freq = {}
    for word in wordlist:
        wordlist.append(word)
        word_freq ={i:wordlist.count(i) for i in wordlist}
        return word_freq
