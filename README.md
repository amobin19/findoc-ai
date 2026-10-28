FinDoc AI

FinDoc AI is a personal project I’m building to explore how AI can simplify financial document analysis.

Financial reports contain a lot of useful information, but finding and comparing specific details can be time-consuming. My goal is to build an application that makes it easier to extract financial data, understand key metrics, and eventually ask questions about a company’s financial performance.

I’m developing the project in stages, starting with PDF processing and gradually introducing AI-powered analysis.

Features

The current version supports:

* Uploading financial documents in PDF format
* Extracting text from uploaded PDFs
* Displaying document details, including filename, file size, and page count
* Previewing extracted text through a Streamlit interface

Tech Stack

* Python – Application logic
* Streamlit – Web interface
* PyMuPDF – PDF processing and text extraction

Getting Started

1. Clone the repository

git clone https://github.com/amobin19/findoc-ai.git
cd findoc-ai

2. Create and activate a virtual environment

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

python -m pip install -r requirements.txt

4. Run the application

python -m streamlit run app.py

Streamlit will provide a local URL where you can access the application.

Roadmap

I’m planning to add the following capabilities as the project develops:

* PDF uploading and text extraction
* Document metadata and text preview
* AI-generated document summaries
* Natural language Q&A for uploaded documents
* Extraction of key financial metrics
* Financial comparisons across reporting periods
* Interactive charts and visualizations

Current Status

The initial version is complete and supports PDF uploading and text extraction.

Next, I’m focusing on integrating an LLM so users can begin interacting with financial documents through natural language.

Author

Ayman Mobin