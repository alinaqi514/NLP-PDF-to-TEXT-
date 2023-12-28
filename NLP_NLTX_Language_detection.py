import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from langdetect import detect
import nltk
nltk.download('punkt')
import nltk
nltk.download('stopwords')


# Open the PDF file in read-binary mode
pdf_file = open('LabTask7.pdf', 'rb')

# Create a PDF file reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF
num_pages = len(pdf_reader.pages)

# Create an empty string to store the text
text = ''

# Loop through each page and extract the text
for page_num in range(num_pages):
    page = pdf_reader.pages[page_num]
    text += page.extract_text()

# Tokenize the sentences
sentences = sent_tokenize(text)

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_sentences = [sentence for sentence in sentences if sentence.lower() not in stop_words]

# Calculate the frequency distribution of words
words = nltk.word_tokenize(text)
fdist = FreqDist(words)

# Calculate the score for each sentence
scores = {}
for sentence in filtered_sentences:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in fdist:
            if len(sentence.split(' ')) < 30:
                if sentence not in scores:
                    scores[sentence] = fdist[word]
                else:
                    scores[sentence] += fdist[word]

# Get the top 5 sentences with the highest scores
summary_sentences = sorted(scores, key=scores.get, reverse=True)[:5]

# Combine the summary sentences into a summary
summary = ' '.join(summary_sentences)

# Print the summary
print(summary)
print("<------------------------------------------------->")

# Detect the language of the text
language = detect(text)

# Print the detected language
print('The language of the text is:', language)
