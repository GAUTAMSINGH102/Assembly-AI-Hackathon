# SmartClass
Be Smart With Smart Class  

## Purpose
- The main purpose was to reduce the time that we spent on reading content and watching Video Lectures.
- We will achieve it by providing:
    - Summarization of Pdfs, Videos and Images
    - Recommending the Relevant Videos, Books and Blogs.
    - Generating Quesiton and Answer for Better Interaction (Stable Diffusion)
    - Generating PDF and PPT for Presentation
    - By Answering it queries  

## Text Summarization  
- Mainly we can get Summary of:
  - Video Lecture
  - Research Paper/ PDFs
  - Images

- **Video Lectures**  
  - At First we will convert it into audio format mp3 or wav.
  - From Audio, using **Whisper OpenAI Model** we would convert it into Text.

- **Research Paper / PDF**
  - To convert PDFs into Text we will use **PyPDF2**.

- **Images**
  - To Convert Images into Text we will use **OCR** Method.

- We would finally find Summary of the text that we have generated using BART Model.  


## Recommendation
- From the Text of Videos, PDFs, Images we will extract Keywords From it using **RAKE Model**.
- And on the Basis of Keywords we will provide the personalized Recommendation to the User.

## Question & Answer
- Using Cohere API we will generate Question & Answer
- For Better Interaction we have also added Images using Stable Diffusion.

## PDFs and PPT For Presentation
- After reading enough content finally we need PPT or PDF to present it.
- So using img2pdf and Pillow Library I have generated PPT and PDF from it.

## Screenshots
### **Upload Video Lectures, PDFs and Images**
![Upload Video Lecture, PDFs and Images](https://github.com/GAUTAMSINGH102/SmartClass/blob/main/WebsiteImages/upload.png)

### **Transcribe Text**
![Transcribe Text](https://github.com/GAUTAMSINGH102/SmartClass/blob/main/WebsiteImages/transcribe.png)

### **Summary**
![Summary](https://github.com/GAUTAMSINGH102/SmartClass/blob/main/WebsiteImages/summary.png)

### **Youtube Recommender**
![Youtube Recommender](https://github.com/GAUTAMSINGH102/SmartClass/blob/main/WebsiteImages/youtuberecommender.png)

### **Book Recommender**
![Book Recommender](https://github.com/GAUTAMSINGH102/SmartClass/blob/main/WebsiteImages/bookrecommender.png)

