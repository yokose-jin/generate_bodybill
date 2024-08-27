import markovify

input_sentences = open("./out.txt", "r", encoding="utf-8")
model = markovify.NewlineText(input_sentences.read())

out_sentence = model.make_sentence(tries=100)
print(out_sentence.replace(" ", ""))

input_sentences.close()