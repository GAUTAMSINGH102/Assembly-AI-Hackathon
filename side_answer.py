import pandas as pd
import numpy as np
import streamlit as st
import cohere
import textwrap

API_KEY = ''
co = cohere.Client(API_KEY)

def side_answer_func(phrase, context):
    # Call the Cohere Generate endpoint
    response = co.generate(
        model='large',
        prompt=f'Given a phrase and context, this program will generate explanation of the phrase in the given context. \n\nPhrase: Augmented reality\nContext: Artificial Intelligence\nExplanation: Augmented reality (AR) is an interactive experience that combines the real world and computer-generated content.The content can span multiple sensory modalities, including visual, auditory, haptic, somatosensory and olfactory.\n--\nPhrase: {phrase}\nContext: {context}\nExplanation:',
        max_tokens=200,
        temperature=0.5,
        k=0,
        p=1,
        frequency_penalty=0.2,
        presence_penalty=0.2,
        stop_sequences=["--"],
        return_likelihoods='NONE')

    answers = response.generations[0].text[0:-2]
    # answers = answers.replace("\n\n--", "").replace("\n--", "").strip()


    return answers


# ar = side_answer_func('CNN', 'Deep Learning')
# print(ar)