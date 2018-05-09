import pandas as pd
from logs.config import cfg
def write_result():
    result_path = cfg.top20_path
    train_data_path = cfg.train_df_path
    print('loading result from {}'.format(result_path))
    result = pd.read_csv(result_path,encoding='gbk')
    print('loading train data from {}'.format(train_data_path))
    train_data = pd.read_csv(train_data_path)
    for i in range(50):
        print('=========================================')
        print(result['title'][i])
        print('_________________________________________')
        to = result['top20'][i]
        l = to.split(',')
        with open('output/{}.txt'.format(i+1),'w',encoding='utf-8') as f:
                for j in range(0,20):
                    if j==0:
                        print('st')
                        f.write(train_data['title'][int(l[j][1:])])
                        f.write('\n')
                        print(train_data['title'][int(l[j][1:])],'\n')
                    elif j==19:
                        
                        f.write(train_data['title'][int(l[j][:-1])])
                        f.write('\n')
                        print(train_data['title'][int(l[j][:-1])],'\n')
                        print('en')
                    else:   
                        f.write(train_data['title'][int(l[j])])
                        f.write('\n')
                        print(train_data['title'][int(l[j])],'\n')