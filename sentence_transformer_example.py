from sentence_transformers import SentenceTransformer
sentences = ["Bu örnek bir cümle", "Her cümle vektöre çevriliyor"]

model = SentenceTransformer('emrecan/bert-base-turkish-cased-mean-nli-stsb-tr')
embeddings = model.encode(sentences)
print(embeddings)

#ref: https://huggingface.co/emrecan/bert-base-turkish-cased-mean-nli-stsb-tr
