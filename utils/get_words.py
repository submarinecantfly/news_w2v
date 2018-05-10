from utils import handle_words as hw
import pandas as pd


stopwords_list = hw.stop_words()#加载stop_words
def get_words(words_path,df_path):
    #用df_path文件中的句子来构建语料库
    df = pd.read_csv(df_path)
    with open(words_path,'wb') as y:
        for i in range(df.shape[0]):
            w_l = hw.jieba_fenci(df['title'][i],stopwords_list)#进行分词
            #print(w_l)
            for n in range(len(w_l)):
                y.write(w_l[n].encode('utf-8'))#删除stopwords
            y.write('\n'.encode('utf-8'))
            if (i+1)%10000==0:
                #break
                print(i)
    print('words prepared')
    return words_path