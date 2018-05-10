from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from utils.get_words import get_words
from logs.config import cfg
def train_model():
    words_path = cfg.words_path
    train_df_path = cfg.train_df_path
    model_output_path = cfg.model_output_path
    print('preparing words')
    get_words(words_path,train_df_path)#准备语料
    print('train model using {}'.format(train_df_path))
    model_output_path = cfg.model_output_path
    model = Word2Vec(LineSentence(words_path),
    size=cfg.train_size, window=cfg.train_window, 
    min_count=cfg.train_min_count, workers=cfg.train_workers)#训练

    model.save(model_output_path)

    print('training done,saving model as {}'.format(model_output_path))
