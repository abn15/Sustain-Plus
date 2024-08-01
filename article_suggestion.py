import os
import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
from openai.error import RateLimitError

nltk.download('punkt')
nltk.download('stopwords')

def fetch_and_clean(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            clean_content = remove_tags(response.content)
            return clean_content
        else:
            st.error(f"Failed to fetch content from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"An error occurred while fetching content from {url}: {str(e)}")
        return None

def remove_tags(html):
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(['style', 'script']):
        data.decompose()
    return ' ' .join(soup.stripped_strings)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    cleaned_text = ' '.join(tokens)
    return cleaned_text, tokens

def plot_keyword_frequencies(keyword_freq):
    words, frequencies = zip(*keyword_freq.items())
    plt.figure(figsize=(12, 8))
    plt.bar(words, frequencies, color='blue')
    plt.xlabel('Keywords')
    plt.ylabel('Frequency')
    plt.title('Keyword Frequency Distribution')
    plt.xticks(rotation=90)
    plt.tight_layout()
    st.pyplot(plt)

def show_article_suggestions_page():
    st.header("Article Suggestions")

    urls = [
        'https://explitia.com/esg-strategy-in-a-manufacturing-company/',
        'https://incit.org/en/thought-leadership/optimising-capital-allocation-for-esg-key-strategies-for-manufacturers/',
        'https://www.forbes.com/sites/lisacaldwell/2023/03/29/suppliers-are-the-secret-sauce-to-manufacturers-esg-success/',
        'https://sustainabilitymag.com/top10/top-10'
    ]

    aggregated_data = ""
    for url in urls:
        cleaned_content = fetch_and_clean(url)
        if cleaned_content:
            aggregated_data += cleaned_content + " "

    cleaned_text_data, tokens = clean_text(aggregated_data)

    keywords = [
        'sustainabl', 'invest', 'esg', 'environment', 'social', 'governanc',
        'respons', 'green', 'ethical', 'impact', 'stakehold', 'transpar',
        'account', 'risk', 'opportun', 'renew', 'carbon',
        'report', 'climat', 'divers', 'wind', 'solar'
    ]

    filtered_tokens = [word for word in tokens if word in keywords]
    keyword_freq = Counter(filtered_tokens)

    plot_keyword_frequencies(keyword_freq)

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("API key for OpenAI not found in environment variables")
    else:
        openai_llm = OpenAI(api_key=api_key)

        prompt_template = PromptTemplate(
            template=(
                "Given the following details about the business in producer management: {text}, "
                "provide suggestions to improve its sustainability. The business has the following sustainability scores: e=20, s=20, g=25."
            ),
            input_variables=["text"]
        )

        llm_chain = LLMChain(
        llm=openai_llm,
        prompt=prompt_template
    )

    # Define the text data (parameters for sustainability)
    text_data = "The business operates in producer management with a focus on efficiency, social responsibility, and governance."

    # Function to get sustainability suggestions with retry logic
    def get_sustainability_suggestions(llm_chain, text_data):
        try:
            suggestions = llm_chain.run(text=text_data)
            return suggestions
        except RateLimitError as e:
            st.error(f"Rate limit reached: {str(e)}. Retrying in 20 seconds...")
            time.sleep(20)
            return get_sustainability_suggestions(llm_chain, text_data)

    # Get sustainability suggestions
    suggestions = get_sustainability_suggestions(llm_chain, text_data)

    # Display the result
    st.write(f"Sustainability Suggestions: {suggestions}\n")

