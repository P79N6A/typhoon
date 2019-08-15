#encoding: utf-8
import numpy as np
import jieba
from pyfasttext import FastText

class Participle(object):

    def __init__(self, fasttext_bin):
        '''
        :param fasttext_bin:分词模型路径
        '''
        self.fasttext_bin = fasttext_bin
        self.model = FastText(fasttext_bin)

    def get_vector(self, text, get_type=2):
        '''
        根据分词内容获取分词向量
        :param text: 分词内容
        :param get_type: 分词模式
        :return:分词向量，np：(n, 300)
        '''
        word_np = []
        if self.model is None:
            model = FastText(self.fasttext_bin)
        else:
            model = self.model
        if get_type == 1:
            seg_list = jieba.cut(text, cut_all=True) #全模式
        elif get_type == 2:
            seg_list = jieba.cut(text, cut_all=False) #精确模式
        else:
            seg_list = jieba.cut_for_search(text) #搜索引擎模式

        for li in list(seg_list):
            word_np.append(np.array(model[li]))
        if len(word_np) == 0:
            word_np = np.zeros((1, 300))
        else:
            word_np = np.array(word_np)
        return word_np

if __name__ == "__main__":
    text = '有些人，社交能力很差。只能和那些志同道合，彼此欣赏的人做朋友。而那些性格不随和，不喜欢自己，但是Q能给自己带来提升的人，他们没有能力搞定。'
    fasttext_bin = "../data/cc.zh.300.bin"

    participle = Participle(fasttext_bin)
    word_np = participle.get_vector(text)

    print(word_np.shape)
    print("suss!!!")