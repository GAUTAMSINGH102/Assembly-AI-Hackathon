from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename

import pandas as pd
import numpy as np
import os

# Importing Function
from answer import generate_answer
from question import generate_question
from questionclassification import question_classification
from side_answer import side_answer_func
from image import generate_image_func

#Importing funciton
from whisper_model_STP import speechToText
from bart_summary import summaryfromtranscribe
from keywords_extraction import keywordsUsingRake
from youtubeRecommender import youtubeRecommender
from bookRecommender import bookRecommender
from textFrompdf import textFromPdf
from textToSpeech import textToSpeech


transcribeText = ''

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/files'

@app.route('/')
def index():
    return render_template("index.html")
    
def stt(audio_file):

        transcribeText=speechToText(audio_file)

        return transcribeText


def tfp(pdf_file):

    pdfText = textFromPdf(pdf_file)

    return pdfText

def summaryfunction(transcribeText):

    summary = summaryfromtranscribe(transcribeText)

    return summary

def keywordsExtraction(transcribeText):

    keywordString = keywordsUsingRake(transcribeText)

    return keywordString

def youtubeRecommenderDict(keywordString):

    youtubeCards = youtubeRecommender(keywordString)

    return youtubeCards

def bookRecommenderDict(keywordString):

    bookCards = bookRecommender(keywordString)

    return bookCards

@app.route('/questions')
def questions():
    return render_template("base.html")

@app.route('/sideAnswer')
def sideAnswer():
    phrase = request.json['phrase']
    context = request.json['context']
    outputSideAns = side_answer_func(phrase, context)
    return jsonify(outputSideAns)

@app.route("/qa")
def qa():
    arr = []
    para = request.args.get('para')  # get para from the URL

    allquestionarr = generate_question(para)
    questionarr = allquestionarr[:6]
    print(questionarr)
    answerarr = generate_answer(questionarr)
    print(answerarr)
    queClass = question_classification(questionarr)
    print(queClass)
    generateImage = generate_image_func(questionarr)
    print(generateImage)

    for question, answer, classification, image_gen in zip(questionarr, answerarr, queClass, generateImage):
        arr.append([question, answer, classification, image_gen])    

    return render_template('qa.html', arr=arr)









    
@app.route('/getTranscribe', methods=['GET', 'POST'])
def getTranscribe():
    if request.method == 'POST':
        
        file = request.files['file']
        print(file)
        fileName = secure_filename(file.filename)
        print(fileName)
        
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))

        splitFileName = fileName.split(".")
        fileExtension = splitFileName[1]

        if(fileExtension == 'mp3'):
            audio_file = f'./static/files/{fileName}'
            print(audio_file)
            transcribe = stt(audio_file)

        elif(fileExtension == 'pdf'):
            pdf_file = f'./static/files/{fileName}'
            print(pdf_file)
            transcribe = tfp(pdf_file)

        if(len(transcribe) > 0):
            print(transcribe)
            return jsonify(transcribe)

@app.route('/transcribe', methods=['GET', 'POST'])
def transcribe():
    transcribe = ''
    if request.method == 'POST':
        
        file = request.files['file']
        fileName = secure_filename(file.filename)
        print(fileName)
        
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))

        print("that's it")
        # audio_file = f'./static/files/{fileName}'
        # print(audio_file)

        # transcribe = stt(audio_file)
        # print('complete')

        # if(len(transcribe) > 0):
        #     print(transcribe)
    return 'post request successfully'



@app.route('/uploadfile', methods=['GET', 'POST'])
def user():
    return render_template("uploadfile.html")


@app.route('/summary', methods=['GET', 'POST'])
def summary():
    if request.method == 'POST':
        transcribeTextJson = request.json
        transcribeText = transcribeTextJson['data']
        print(f"INSIDE SUMMARY : {transcribeText}")
        summaryText = summaryfunction(transcribeText)

        if(len(summaryText)>0):
            print(summaryText)
            return jsonify(summaryText)

@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    if request.method == 'POST':
        transcribeTextJson = request.json
        transcribeText = transcribeTextJson['data']
        print(f"INSIDE KEYWORDS : {transcribeText}")
        keywordString = keywordsExtraction(transcribeText)

        if(len(keywordString)>0):
            print(keywordString)
            return jsonify(keywordString)


@app.route('/recommender', methods=['GET', 'POST'])
def recommenderfunc():
    if request.method == 'POST':
        keywordStringJson = request.json
        keywordString = keywordStringJson['data']
        print(f"INSIDE RECOMMENDER : {keywordString}")

        youtube_cards = youtubeRecommenderDict(keywordString)

        if(len(youtube_cards)>0):
            print(youtube_cards)
            return jsonify(youtube_cards)


@app.route('/bookRecommender', methods=['GET', 'POST'])
def bookrecommenderfunc():
    if request.method == 'POST':
        keywordStringJson = request.json
        keywordString = keywordStringJson['data']
        print(f"INSIDE BOOK RECOMMENDER : {keywordString}")

        book_cards = bookRecommenderDict(keywordString)

        if(len(book_cards)>0):
            print(book_cards)
            return jsonify(book_cards)


@app.route('/tts', methods=['GET', 'POST'])
def ttsSummary():
    if request.method == 'POST':
        summaryJson = request.json
        summaryText = summaryJson['data']
        print(f"INSIDE tts : {summaryText}")

        textToSpeech(summaryText)

        return jsonify("Text To Speech")


@app.route('/plagiarism')
def plagiarsim():
    return render_template("plagiarism.html")
    



if __name__ == '__main__':
    app.run(debug=True)