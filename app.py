import streamlit as st
import pymupdf
from document_processing import search_document,sentence_extract

# Configure the application
st.set_page_config(
    page_title="FinDoc AI",
    page_icon="📄",
    layout="wide"
)

# Application header
st.title("📄 FinDoc AI")
st.subheader("AI-Powered Financial Document Analyst")
st.write(
    "Upload financial documents and explore their contents."
)

# PDF upload functionality
uploaded_file = st.file_uploader(
    "Upload a financial PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success("PDF uploaded successfully!")
    st.write("Filename:", uploaded_file.name)
    st.write("File size:", uploaded_file.size, "bytes")

    keyword = st.text_input("Keyword: ")

    # Open the uploaded PDF
    pdf_document = pymupdf.open(
        stream=uploaded_file.getvalue(),
        filetype="pdf"
    )

    # Extract text from every page
    extracted_text = ""

    for page in pdf_document:
        extracted_text += page.get_text()

    if keyword:
        results = search_document(extracted_text, keyword)
        items_found = len(results)
        st.write(items_found, " matches found.")
        if items_found == 0:
            st.write("No matching results found.")
        for line in results:
            st.text(line)
    
    # Display extraction results
    st.subheader("Document Analysis")
    st.write("Total pages:", len(pdf_document))
    st.write("Characters extracted:", len(extracted_text))

    # Display the summary of the text
    summary = st.number_input("How many sentences would you like exctracted? ",min_value=0,value=0,step=1)
    st.write(sentence_extract(extracted_text,summary))

    # Preveiw extracted text
    with st.expander("View extracted PDF text"):
        st.text(extracted_text[:5000])

    pdf_document.close()