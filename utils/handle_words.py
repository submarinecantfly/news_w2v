import jieba
from logs.config import cfg

def stop_words():
    #获取stopwords，返回列表
    stop_words_file = open(cfg.stop_words_path, 'r')
    stopwords_list = []
    for line in stop_words_file.readlines():
        stopwords_list.append(line[:-1])
        #print(type(stopwords_list[-1]))
    return stopwords_list

def jieba_fenci(raw, stopwords_list):
    #返回结巴切分过的单词列表
    
    word_list =list(jieba.cut(raw, cut_all=False))
    #print(type(word_list))
    for word in word_list:
        if word in stopwords_list:
            
            word_list.remove(word)
    
    #word_list.remove('\n')
    #word_list = ' '.join(word_list)
    #print(type(word_list))
    return word_list

def clear_list(l,vocab):
    #删除不在词典内的单词，返回列表
    
    #print(l)
    l1 = []
    for word in l:
        if word in vocab:
            l1.append(word)
        else:
            l.remove(word)
            #print(word)
    return l1

