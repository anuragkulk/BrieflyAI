import streamlit as st
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import time

# Load env
load_dotenv()

# Page config
st.set_page_config(page_title="BrieflyAI", page_icon="⚡", layout="wide")

# 🔥 Ultra-modern UI (glassmorphism + neon glow)
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #020617);
}
.main {
    background: transparent;
    color: white;
}
.title {
    text-align: center;
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(90deg, #22c55e, #3b82f6, #a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 30px;
}
.input-box input {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    color: white;
}
.stButton>button {
    width: 100%;
    border-radius: 12px;
    background: linear-gradient(90deg, #22c55e, #3b82f6);
    color: white;
    font-weight: bold;
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 20px rgba(59,130,246,0.5);
}
.result-card {
    padding: 25px;
    border-radius: 16px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>⚡ BrieflyAI</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Instant AI-powered news summaries with real-time search 🚀</div>", unsafe_allow_html=True)

# Input
query = st.text_input("🔍 What do you want to know?", placeholder="e.g. AI trends, cricket news, geopolitics...")

# Tools
search_tool = TavilySearchResults(max_result = 5)
llm = ChatMistralAI(model="mistral-small-2506")

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant

Summarize the following news into clear bullet points:

{news}
""")

chain = prompt | llm | StrOutputParser()

# Button
if st.button("⚡ Generate Insights"):
    if query.strip() == "":
        st.warning("Enter something first bro 👀")
    else:
        with st.spinner("🧠 Thinking like an AI genius..."):
            news_result = search_tool.run(query)
            time.sleep(1)
            result = chain.invoke({"news": news_result})

        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown("### 📰 AI Summary")
        st.write(result)
        st.markdown("</div>", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## ⚙️ System Info")
st.sidebar.write("Model: mistral-small-2506")
st.sidebar.write("Search: Tavily API")
st.sidebar.write("Framework: LangChain")

st.sidebar.markdown("## 💡 Try Queries")
st.sidebar.write("- Latest AI breakthroughs")
st.sidebar.write("- India cricket updates")
st.sidebar.write("- Startup news 2026")
st.sidebar.write("- SpaceX missions")