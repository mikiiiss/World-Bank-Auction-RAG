import PyPDF2
import re

# Step 1: Extract text from the PDF using PyPDF2
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()  # Extract text from each page
    return text

# Step 2: Clean the extracted text
def clean_text(text):
    # Remove page numbers (e.g., "Page 1 of 10")
    text = re.sub(r"Page \d+ of \d+", "", text)
    
    # Remove headers/footers (e.g., "World Bank Report 2023")
    text = re.sub(r"World Bank Report \d{4}", "", text)
    
    # Remove extra spaces and newlines
    text = " ".join(text.split())
    
    return text

# Step 3: Normalize the text (optional)
def normalize_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"[^\w\s.,]", "", text)  # Remove special characters except periods and commas
    return text

# Step 4: Remove irrelevant content (e.g., short lines, boilerplate)
def remove_irrelevant_content(text):
    lines = text.split("\n")
    cleaned_lines = [line for line in lines if len(line.split()) > 5]  # Keep lines with more than 5 words
    cleaned_text = "\n".join(cleaned_lines)
    return cleaned_text

# Main function to preprocess the PDF
def preprocess_pdf(pdf_path):
    # Step 1: Extract text
    text = extract_text_from_pdf(pdf_path)
    
    # Step 2: Clean text
    text = clean_text(text)
    
    # Step 3: Normalize text (optional)
    text = normalize_text(text)
    
    # Step 4: Remove irrelevant content
    text = remove_irrelevant_content(text)
    
    return text

# Example usage
pdf_path = "../data/world Bank .pdf"  # Replace with the path to your PDF
cleaned_text = preprocess_pdf(pdf_path)

# Save the cleaned text to a file (optional)
with open("cleaned_text.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)

print("Text extraction and preprocessing complete!")
