import streamlit as st
from utils import read_txt, read_pdf, read_docx
from contract_processor import extract_clauses, extract_entities, classify_contract, simple_summary
from risk_engine import detect_risks, contract_risk_score

st.set_page_config(page_title="GenAI Legal Assistant", layout="wide")

st.title("⚖️ GenAI Legal Contract Assistant")

uploaded_file = st.file_uploader(
    "Upload Contract (PDF, DOCX, TXT)",
    type=["pdf", "docx", "txt"]
)

text = ""

if uploaded_file:
    if uploaded_file.name.endswith(".txt"):
        text = read_txt(uploaded_file)
    elif uploaded_file.name.endswith(".pdf"):
        text = read_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        text = read_docx(uploaded_file)

if text:
    st.subheader("📄 Contract Type")
    st.write(classify_contract(text))

    st.subheader("📑 Extracted Clauses")
    clauses = extract_clauses(text)
    for c in clauses:
        st.write("•", c)

    st.subheader("🏷 Extracted Entities")
    st.write(extract_entities(text))

    st.subheader("⚠ Risk Detection")
    risks = detect_risks(text)
    st.write(risks if risks else "No risks found")

    st.subheader("📊 Overall Risk Level")
    st.write(contract_risk_score(risks))

    st.subheader("📃 Simplified Summary")
    st.write(simple_summary(text))
