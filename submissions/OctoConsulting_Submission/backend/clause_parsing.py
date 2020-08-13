# The purpose of this file is to parse EULA documents into individual clauses
# The accepted filetypes are .docx or .pdf
# The files are parsed into a string using the OCR packages >>>> and pdfplumber for .docx and .pdf respectively
# Then the package nltk is used to separate the string into individual clauses

import nltk
import pdfplumber
import docx


def extract_all_clauses(document):
    # Checks document type, uses OCR to parse text from document, and returns a list of clauses
    # Input: Word document (.docx) or pdf document (.pdf)
    # Output: A list of clauses that have been parsed from the document

    if document.endswith('.docx'):
        text_body = _doc_to_text_body(document)
    elif document.endswith('.pdf'):
        text_body = _pdf_to_text_body(document)
    else:
        return("Error: The supplied document is not the correct filetype. Please upload a docx or pdf document to proceed.")
    return(parse_sentences(text_body))


def parse_sentences(body):
    # Input: Body of text as a single string
    # Output: List of tokenized sentences
    tokenizer = nltk.data.load('/nltk_data/corpora/punkt/english.pickle')
    return tokenizer.tokenize(body)


def _doc_to_text_body(doc_path):
    # Converts contents of word doc to string
    print("Word Doc OCR Starting")
    doc = docx.Document(doc_path)
    text_body_arr = []
    for para in doc.paragraphs:
        text_body_arr.append(para.text)
    print("Word Doc OCR Finished")
    return ' '.join(text_body_arr)


def _pdf_to_text_body(pdf_path):
    # Converts contents of PDF to string
    # Input: Path to pdf doc
    # Output: A single string that is all of the extracted text from the pdf doc
    print("PDF OCR Starting")
    text_body_arr = []
    with pdfplumber.open(pdf_path) as pdf:
        for each_page in pdf.pages:
            page_text = each_page.extract_text()
            text_body_arr.append(page_text)
    print("PDF OCR Finished")
    return ' '.join(text_body_arr)
    # for clause in parsed:
    #     print(clause)


if __name__ == '__main__':
    # test_text = "There isn't time, so brief is life. And but an instant, so to speak, for that."
    # test_2 = "4. PAYMENTS. 4.1 – Licensing/Service Fees. License fees are due at the time of signing the agreement. 4.2 – Support and Maintenance Payment. Support and Maintenance is included as part of licensing fee during subscription validity period. 4.3 – Overdue Payments. Overdue payments of License Fee required by this Agreement shall accrue interest at the lesser of one and one-half percent (1.5%) per month or the maximum allowable interest under applicable law, from the due date until paid, and Customer shall pay COMPANY's costs of collection, including COMPANY's reasonable attorneys' fees and court costs. COMPANY will suspend any services, support or consulting services otherwise required to be provided to Customer under this Agreement after 2 months of non-payment until all delinquent payments, including interest and costs of collection, have been paid by Customer. 4.4 - Returned Checks and Declined Credit Cards may incur a fee. "
    # clauses = parse_clauses(test_2)
    # print(clauses)

    test_pdf_path = "C:/Users/meredith.lee/Documents/GitHub/GSA-AI/submissions/OctoConsulting_Submission/backend/testdata/test1.pdf"
    test_docx_path = "C:/Users/meredith.lee/Documents/GitHub/GSA-AI/submissions/OctoConsulting_Submission/backend/testdata/test1.docx"
    # pdf_to_text_body(test_pdf_path)

    # parsed_doc = extract_all_clauses(test_pdf_path)
    # print(len(parsed_doc))
    # for text in parsed_doc:
    #     print(text)

    parsed_docx = extract_all_clauses(test_docx_path)
    # print(parsed_docx)
    # print(len(parsed_docx))