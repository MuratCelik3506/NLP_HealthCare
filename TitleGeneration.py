from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
import os

def create_title(text):
    #nltk.download('punkt')

    tokenizer = AutoTokenizer.from_pretrained("fabiochiu/t5-small-medium-title-generation") # czearing/article-title-generator
    model = AutoModelForSeq2SeqLM.from_pretrained("fabiochiu/t5-small-medium-title-generation")# czearing/article-title-generator


    inputs = ["summarize: " + text]

    inputs = tokenizer(inputs, truncation=True, return_tensors="pt")
    output = model.generate(**inputs, num_beams=8, do_sample=True, min_length=10, max_length=64)
    decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    predicted_title = nltk.sent_tokenize(decoded_output.strip())[0]
    return predicted_title
# Conversational AI: The Future of Customer Service
