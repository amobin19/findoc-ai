import streamlit as st
import pymupdf

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

    # Open the uploaded PDF
    pdf_document = pymupdf.open(
        stream=uploaded_file.getvalue(),
        filetype="pdf"
    )

    # Extract text from every page
    extracted_text = ""

    for page in pdf_document:
        extracted_text += page.get_text()

    # Display extraction results
    st.subheader("Document Analysis")

    st.write("Total pages:", len(pdf_document))
    st.write("Characters extracted:", len(extracted_text))

    # Preveiw extracted text
    with st.expander("View extracted PDF text"):
        st.text(extracted_text[:5000])

    pdf_document.close()