
import streamlit as st
import pandas as pd
import re

# Title and description
st.title("EqualitorAI HR: Fairness Scanner for Job Posts & Resumes")
st.markdown("""
Upload a job description or resume file. Our AI scans for biased terms, detects indirect discrimination,
and gives a fairness score + improvement suggestions.
""")

# File uploader
uploaded_file = st.file_uploader("📥 Upload Job Description or Resume (TXT format)", type=["txt"])

# Sample list of biased terms
biased_terms = {
    "native english speaker": "Consider removing language requirements unless absolutely essential.",
    "young and energetic": "May imply age bias. Use 'motivated' or 'dynamic' instead.",
    "recent graduate": "Can exclude experienced candidates unnecessarily.",
    "digital native": "Avoid terms tied to generation or age.",
    "must be able to lift 50 lbs": "Unless job requires it, may be exclusionary."
}

# Function to scan text for biased terms
def scan_text(text):
    found = {}
    for term in biased_terms:
        if re.search(term, text, re.IGNORECASE):
            found[term] = biased_terms[term]
    return found

# Main logic
if uploaded_file:
    file_text = uploaded_file.read().decode("utf-8", errors='ignore')
    st.subheader("📄 File Content Preview:")
    st.text(file_text[:500])  # show first 500 characters

    st.subheader("🤖 Detected Biased Terms:")
    findings = scan_text(file_text)
    if findings:
        for term, advice in findings.items():
            st.markdown(f"- **'{term}'** → {advice}")
        fairness_score = 100 - len(findings) * 10
        st.subheader("📊 Fairness Score:")
        st.success(f"{fairness_score}/100")
    else:
        st.success("✅ No biased terms detected. Excellent!")
        st.subheader("📊 Fairness Score:")
        st.success("100/100")

    st.subheader("📄 Recommendations:")
    st.markdown("- Use inclusive, role-focused language.\n- Avoid unnecessary physical or age-related requirements.\n- Focus on skills, not demographics.")

    st.markdown("---")
    st.caption("EqualitorAI HR MVP Demo — Built for transparency, not ideology.")
