import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup
from textblob import TextBlob

st.set_page_config(
    page_title="News Aggregator Dashboard",
    page_icon="📰",
    layout="wide"
)


NEWS_SOURCES = {
    "Technology": "https://techcrunch.com/",
    "Business": "https://www.reuters.com/business/",
    "Sports": "https://www.espn.com/",
}



def scrape_techcrunch():
    articles = []

    try:
        response = requests.get(
            "https://techcrunch.com/",
            headers={"User-Agent": "Mozilla/5.0"}
        )

        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all("h3")

        for headline in headlines[:20]:
            title = headline.get_text(strip=True)

            if title:
                articles.append({
                    "Title": title,
                    "Category": "Technology"
                })

    except Exception as e:
        st.error(f"TechCrunch Error: {e}")

    return articles


def scrape_reuters_business():
    articles = []

    try:
        response = requests.get(
            "https://www.reuters.com/business/",
            headers={"User-Agent": "Mozilla/5.0"}
        )

        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all(["h2", "h3"])

        for headline in headlines[:20]:
            title = headline.get_text(strip=True)

            if len(title) > 10:
                articles.append({
                    "Title": title,
                    "Category": "Business"
                })

    except Exception as e:
        st.error(f"Reuters Error: {e}")

    return articles


def scrape_espn():
    articles = []

    try:
        response = requests.get(
            "https://www.espn.com/",
            headers={"User-Agent": "Mozilla/5.0"}
        )

        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all(["h1", "h2", "h3"])

        for headline in headlines[:20]:
            title = headline.get_text(strip=True)

            if len(title) > 8:
                articles.append({
                    "Title": title,
                    "Category": "Sports"
                })

    except Exception as e:
        st.error(f"ESPN Error: {e}")

    return articles



def get_sentiment(text):
    score = TextBlob(text).sentiment.polarity

    if score > 0:
        return "Positive"

    elif score < 0:
        return "Negative"

    return "Neutral"



@st.cache_data
def load_news():

    all_articles = []

    all_articles.extend(scrape_techcrunch())
    all_articles.extend(scrape_reuters_business())
    all_articles.extend(scrape_espn())

    df = pd.DataFrame(all_articles)

    if not df.empty:
        df["Sentiment"] = df["Title"].apply(get_sentiment)

    return df



st.title("📰 News Aggregator Dashboard")

st.markdown(
    """
    Search headlines, filter by category,
    and view sentiment analysis.
    """
)

df = load_news()

if df.empty:
    st.warning("No articles found.")
    st.stop()



st.sidebar.header("Filters")

selected_category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(df["Category"].unique())
)

search_query = st.sidebar.text_input(
    "Search Keyword"
)



filtered_df = df.copy()

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

if search_query:
    filtered_df = filtered_df[
        filtered_df["Title"].str.contains(
            search_query,
            case=False,
            na=False
        )
    ]



col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Articles", len(filtered_df))

with col2:
    st.metric(
        "Positive Headlines",
        len(filtered_df[
            filtered_df["Sentiment"] == "Positive"
        ])
    )

with col3:
    st.metric(
        "Negative Headlines",
        len(filtered_df[
            filtered_df["Sentiment"] == "Negative"
        ])
    )

st.divider()



for _, row in filtered_df.iterrows():

    with st.container():

        st.subheader(row["Title"])

        c1, c2 = st.columns(2)

        with c1:
            st.write(f"📂 Category: {row['Category']}")

        with c2:
            st.write(f"📊 Sentiment: {row['Sentiment']}")

        st.divider()