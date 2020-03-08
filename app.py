from flask import Flask, render_template, request

app = Flask(__name__)

def encrypt(text, key, mode):
    encryptedText = ""
    shift = int(key)
    if mode == 'd': #set mode to d if we want to decrypt
        shift = -shift
    x = range(len(text))
    for i in x:
        char = text[i]
        if (char.isupper()):
            encryptedChar = chr((ord(char)+ shift - 65) % 26 + 65)
            encryptedText += encryptedChar
            #ord returns unicode val of char, 65 is the lowest unicode for a letter and it is uppercase A.
            #we then add (key - 65) to offset the the val of our char by our key val shift
            #we use modulo 26 to divide our result by the letters in alphabet
            #we add 65 to put it back in unicode letter range
        else: #for lowercase
            encryptedChar = chr((ord(char)+ shift - 97) % 26 + 97)
            encryptedText += encryptedChar
            #97 is lowest lowercase which is 'a'
    return encryptedText

@app.route('/', methods =['POST', 'GET'])
def index():
    return render_template('index.html')
@app.route('/encrypt', methods=['POST'])
def encryptPage():
    if request.method == 'POST':
        text = request.form['Input']
        key = request.form['ShiftKey']
        newText = encrypt(text, key, 'e')
        return render_template('index.html', result = ("Encrypted Message using " + key + " as key: " + newText))
@app.route('/decrypt', methods=['POST'])
def decryptPage():
    if request.method == 'POST':
        text = request.form['Input']
        key = request.form['ShiftKey']
        newText = encrypt(text,key, 'd')
        return render_template('index.html', result = ("Decrypted Message using " + key+ " as key: " + newText))
if __name__ == '__main__':
    app.run()
