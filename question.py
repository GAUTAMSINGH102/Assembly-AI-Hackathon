import pandas as pd
import numpy as np
import streamlit as st
import cohere
import textwrap

API_KEY = 'j9fltyvpID3YyH82yoUqSCjhcydpMh1vG3lLS83z'
co = cohere.Client(API_KEY)

# Paragraph: A declarative action model is a compact representation of the state transitions of dynamic systems that generalizes over world objects. The specification of declarative action models is often a complex hand-crafted task. In this paper we formulate declarative action models via state constraints, and present the learning of such models as a combinatorial search. The comprehensive framework presented here allows us to connect the learning of declarative action models to well-known problem solving tasks. In addition, our framework allows us to characterize the existing work in the literature according to four dimensions: (1) the target action models, in terms of the state transitions they define; (2) the available learning examples; (3) the functions used to guide the learning process, and to evaluate the quality of the learned action models; (4) the learning algorithm. Last, the paper lists relevant successful applications of the learning of declarative actions models and discusses some open challenges with the aim of encouraging future research work.
# Questions: What is a declarative action model? How does the framework mentioned help to characterize the existing work? What are some of the open challenges with respect to the successful applications of the learning of declarative actions models?

def generate_question(inp_query):
    base_question_prompt = textwrap.dedent("""
    Given a paragraph, this program will generate questions from the paragraph.
    Paragraph: Machine learning is a branch of artificial intelligence (AI) and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy. IBM has a rich history with machine learning. One of its own, Arthur Samuel, is credited for coining the term, machine learning with his research (PDF, 492 KB) (link resides outside IBM) around the game of checkers. Robert Nealey, the self-proclaimed checkers master, played the game on an IBM 7094 computer in 1962, and he lost to the computer. Compared to what can be done today, this feat almost seems trivial, but it considered a major milestone within the field of artificial intelligence. Over the next couple of decades, the technological developments around storage and processing power will enable some innovative products that we know and love today, such as Netflix recommendation engine or self-driving cars. Machine learning is an important component of the growing field of data science. Through the use of statistical methods, algorithms are trained to make classifications or predictions, uncovering key insights within data mining projects. These insights subsequently drive decision making within applications and businesses, ideally impacting key growth metrics. As big data continues to expand and grow, the market demand for data scientists will increase, requiring them to assist in the identification of the most relevant business questions and subsequently the data to answer them.
    Questions: What is Machine Learning? What is importance of Machine Learning? What is significance of Machine Learning to Data Science? What does the term Data Science Mean? How does big data play a role in the field of Machine Learning? How do Machine Learning algorithm assist in Data Mining Projects? What are the Statistical methos that are used in Machine Learning? How does Machine Learning assist in Decision Making within applications and businesses? What are some common Machine Learning algorithm and application? What are some examples of how Machine Learning is used today? 
    
    --
    Paragraph:""")

    # Call the Cohere Generate endpoint
    response = co.generate(
        model='large',
        prompt=base_question_prompt + " " + inp_query + "\nQuestions:",
        max_tokens=150,
        temperature=0.7,
        k=0,
        p=0.7,
        frequency_penalty=0.1,
        presence_penalty=0,
        stop_sequences=["--"])

    questions = response.generations[0].text
    questions = questions.replace("\n\n--", "").replace("\n--", "").strip()

    arr = questions.split('?')

    return arr


# para = 'Transfer learning is a huge deal in NLP. There are two main reasons why: (1) assembling a large text corpus to train on is often difficult (we usually only have a few examples); and (2) we dont have powerful enough GPUs (unless we are someone like OpenAI) to train these models anyway. Transfer learning involves taking a model with pretrained weights (someone else has done the heavy lifting for us) and fine-tuning it on new data. That is, we take the body of the old model, train the head on our task-specific data, and splice them back together. The body is responsible for the broad general knowledge representations, and the head of the model makes slight tweaks to predictions based on the actual task and domain-specific data. This means we can actually produce useful language models with minimal data and a regular CPU. Transfer learning is similar in computer vision, where the models are pretrained on a massive dataset to teach the models basic features of vision. We then fine-tune on the specific dataset, such as classifying types of weeds. We almost always get much better results with this fine-tuned model than if we had just trained a model from scratch on the weed data. One key transfer learning method in NLP is ULMFiT: universal language model fine-tuning for text classification. The idea is simple: pretrain a model to predict the next word given a sequence of words, which as you may have noted does not require labeled data. After this unsupervised pretraining, do the same training (predicting the next word) on your specific data. Finally, train the head of this new model on the classification task. This breakthrough gestated two transformers that combined self-attention with transfer learning: GPT and BERT. Both achieved state-of-the-art results on many NLP benchmark tasks.'
# ans = generate_question(para)
# print(ans)