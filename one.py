# Import necessary libraries
from newspaper import Article
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer  # Using Latent Semantic Analysis Summarizer
import nltk
# import nltk
# nltk.download('punkt')
import nltk
nltk.download('punkt_tab')
import nltk
nltk.data.path.append('/home/codespace/nltk_data')  # Add the correct path where punkt is stored

# Download necessary nltk packages
nltk.download('punkt')

# Function to fetch article text
def fetch_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

# Function to summarize the article using sumy LSA summarizer
def summarize_article(text, sentence_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()  # You can also try LexRank, Luhn, etc.
    summary = summarizer(parser.document, sentence_count)
    
    return ' '.join([str(sentence) for sentence in summary])

# Main function
if __name__ == "__main__":
    # Provide the URL of the news article you want to summarize
    url = 'https://www.nature.com/articles/d41586-024-02898-1'
    
    # Fetch the article text
    article_text = fetch_article(url)
    
    # Summarize the article
    summary = summarize_article(article_text, sentence_count=3)  # Get a summary of 3 sentences
    
    # Print the summary
    print("Summary of the article:")
    print(summary)
