import gensim.downloader as api
from gensim.models import KeyedVectors


path = api.load('word2vec-google-news-300', return_path=True)
model = KeyedVectors.load_word2vec_format(path, binary=True, limit=200_000)
model.save('word2vec_google_news_200k.bin')
