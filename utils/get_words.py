from utils import handle_words as hw
import pandas as pd


stopwords_list = hw.stop_words()
def get_words(words_path,df_path):
    df = pd.read_csv(df_path)
    with open(words_path,'wb') as y:
        for i in range(df.shape[0]):
            w_l = hw.jieba_fenci(df['title'][i],stopwords_list)
            #print(w_l)
            for n in range(len(w_l)):
                y.write(w_l[n].encode('utf-8'))
            y.write('\n'.encode('utf-8'))
            if (i+1)%10000==0:
                #break
                print(i)
    print('words prepared')
    return words_path