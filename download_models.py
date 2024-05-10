from transformers import AutoModelForSequenceClassification, AutoTokenizer

modelName = "MoritzLaurer/deberta-v3-large-zeroshot-v2.0"
modelPath = "model"

model = AutoModelForSequenceClassification.from_pretrained(modelName)
model.save_pretrained(modelPath)

tokenizer = AutoTokenizer.from_pretrained(modelName)
tokenizer.save_pretrained(modelPath)
