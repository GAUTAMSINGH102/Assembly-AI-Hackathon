import pandas as pd
import numpy as np
import streamlit as st
import cohere
import textwrap

# Question: What is Machine Learning?
# Answer: Machine learning is a branch of artificial intelligence (AI) and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy.

# --
# Question: How Data should be cleaned before providing it to Algorithm?
# Answer: Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. When combining multiple data sources, there are many opportunities for data to be duplicated or mislabeled.

# --
# Question: Which Algorithm are there in Machine Learning?
# Answer: There are four types of machine learning algorithms: supervised, semi-supervised, unsupervised and reinforcement.
        

API_KEY = ''
co = cohere.Client(API_KEY)

def generate_answer(questionData):

    arr = []
    for i in range(0, len(questionData)):
        base_answer_prompt = f"""
        This program will answer questions based on the provided data.
        Question: How Data should be cleaned before providing it to Algorithm?
        Answer: Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. When combining multiple data sources, there are many opportunities for data to be duplicated or mislabeled.
        
        --
        Question: """

        # Call the Cohere Generate endpoint
        response = co.generate(
            model='large',
            prompt=base_answer_prompt + " " + questionData[i] + "\nAnswer:",
            max_tokens=250,
            temperature=0.7,
            k=0,
            p=0.7,
            frequency_penalty=0.1,
            presence_penalty=0,
            stop_sequences=["--"])

        answers = response.generations[0].text
        answers = answers.replace("\n\n--", "").replace("\n--", "").strip()

        arr.append(answers)

    return arr


# questionsData = ['What is transfer learning', ' Why is transfer learning useful in NLP', ' How does transfer learning work in NLP', ' How does transfer learning work in computer vision', ' What is the process for transfer learning', ' What are the main steps in the transfer learning process', ' What is ULMFiT', ' What are the key benefits of transfer learning', ' What are the advantages of transfer learning', ' What are the limitations of transfer learning', ' What are the limitations of transfer learning', '']
# ar = generate_answer(questionsData)
# print(ar)