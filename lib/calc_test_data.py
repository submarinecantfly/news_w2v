import numpy as np
import pandas as pd
import heapq
from gensim.models import Word2Vec
from logs.config import cfg
from utils import handle_words as hw
def calc_test_data():
    model_path = cfg.model_output_path
    print('loading model from {}'.format(model_path))
    model = Word2Vec.load(model_path)
    vocab = list(model.wv.vocab.keys())
    test_data_path = cfg.test_df_path
    print('loading test data from {}'.format(test_data_path))        
    test = pd.read_csv(test_data_path,encoding='gbk')
    test['top20'] = np.zeros(test.shape[0])
    train_data_path = cfg.train_df_path
    print('loading train data from {}'.format(train_data_path))
    train = pd.read_csv(train_data_path)
    stopwords_list = hw.stop_words()
    test_words = []

    for i in range(test.shape[0]):
        raw = test['title'][i]
        l1 = hw.jieba_fenci(raw,stopwords_list)
        l1 = hw.clear_list(l1,vocab)
        test_words.append(l1)

    anss = np.zeros((50,485686))
    print(anss.shape)
    for i in range(train.shape[0]):    
        raw = train['title'][i]    
        l1 = hw.jieba_fenci(raw,stopwords_list)    
        l1 = hw.clear_list(l1,vocab)
        #print('test',l1)
        for j in range(test.shape[0]):
            l2 = test_words[j]
            try:
                anss[j,i] = model.n_similarity(l1,l2)
            except:anss[j,i] = 0
        if i%1000==0:
            print('{} words done'.format(i))
            
    print('all done')
    top20_path = cfg.top20_path
    print('saving result as {}'.format(top20_path))
    # for i in range(50):
    #     ans = anss[i,:]
    #     top = heapq.nlargest(20,range(len(ans)),ans.__getitem__)
    #     test['top20'][i] = str(top)
    for i in range(50):
        ans = anss[i,:]
        top = heapq.nlargest(20,range(len(ans)),ans.__getitem__)
        an['top20'][i] = top
        
        test.to_csv(cfg.top20_path,mode='a')