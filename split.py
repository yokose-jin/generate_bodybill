import MeCab

mecab = MeCab.Tagger("-Owakati")
input_sentences = open("./data.txt", 'r', encoding='utf-8')
output_sentences = open("./out.txt", 'w', encoding='utf-8')

for line in input_sentences.read().split('\n'):
    splitted_sentence = ' '.join(mecab.parse(line).split())
    output_sentences.write(splitted_sentence)
    output_sentences.write("\n")

input_sentences.close()
output_sentences.close()

