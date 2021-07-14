set -e
set -x

python ./dump_model.py
tar cf word2vec_google_news_200k.tar.xz -I 'xz -0' word2vec_google_news_200k.bin*
