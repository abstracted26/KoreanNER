# Importing JSON & Regex for creating a json & manipulating datastructures
import json
import re
# Importing NLTK and NumPy
from nltk import tokenize
import numpy as np
#Importing koalanlp function from koala_nlp.py
from koalaNLP import koreannlp
# Importing Flask for creating a python server
from flask import Flask, request
app = Flask(__name__)

# Korean NLP Server API
@app.route('/KoreanNER', methods=['POST'])
def extract():
    try:
        # Storing text from the request form in a variable
        text = request.form['text']
        # initializing bad_chars_list
        bad_chars = ['.',';', ':', '!', "*",'~',"'","입"]
        # Removing Bad Characters
        for i in bad_chars :
            text = text.replace(i, '')
            
        print(text)
        
        # Seperating Words from the text
        words = tokenize.word_tokenize(text)
        koreannlp_input = ""
        for word in words:
            koreannlp_input = koreannlp_input + word

        print(koreannlp_input)
        
        # Calling the KoalaNLP package from koala_nlp Python Script
        entities = koreannlp(koreannlp_input)
        print(entities)
        # Mapping the KoalaNLP output into a string array
        entities_array = map(str, entities)
        x = ""
        print(entities_array)
        for i in entities_array:
            x = x + i + " "

        # Creating the JSON that will be returned
        json_of_data = {
            "data": x
        }
        # Returning the Entities Array in a JSON
        return (json_of_data)
        
    except:
        return json.dumps({"data":"데이터가 충분하지 않거나 이미지의 데이터가 잘못됨"}), 400
    
if __name__ == '__main__':
    app.run(port=5010, debug=True)
