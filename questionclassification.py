import cohere 
from cohere.classify import Example 
API_KEY = 'j9fltyvpID3YyH82yoUqSCjhcydpMh1vG3lLS83z'
co = cohere.Client(API_KEY)

inputs=["what is Data Mining", "How to find the face embedding using transfer learning"]

def question_classification(inputData):
  arr = []
  response = co.classify( 
    model='large', 
    inputs=inputData, 
    examples=
      [
        Example("What is Machine Learning", "Basic"), 
        Example("How Machine Learning differ from Artificial Intelligence", "Important"), 
        Example("How do big data and Machine Learning relate", "Very Important"), 
        Example("Real World Application for Machine Learning", "Very Important"), 
        Example("what is Data Science", "Basic"), 
        Example("what is Big Data", "Basic"), 
        Example("Current Application of Machine Learning", "Important"), 
        Example("How CNN works", "Very Important"), 
        Example("Working of Neural Network in Deep Learning", "Important"), 
        Example("How Object Detection work with YOLO", "Very Important")
      ]
  ) 

  for i in range(0, len(inputData)):
      # print('Classification: {}'.format(response.classifications[i].prediction)) 
      arr.append(response.classifications[i].prediction)

  return arr

# ar = question_classification(inputs)
# print(ar)
