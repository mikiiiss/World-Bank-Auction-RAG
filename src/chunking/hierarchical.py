import os

def hierarchical_chunking(text):
    # Split into sections (e.g., based on headings)
    sections = text.split("\n\n")  # Assuming sections are separated by double newlines
    
    # Split each section into paragraphs
    chunks = []
    for section in sections:
        paragraphs = section.split("\n")  # Assuming paragraphs are separated by newlines
        chunks.extend(paragraphs)
    return chunks

def save_chunks(chunks, output_dir, method_name):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Save each chunk to a file
    for i, chunk in enumerate(chunks):
        with open(f"{output_dir}/{method_name}_chunk_{i}.txt", "w", encoding="utf-8") as file:
            file.write(chunk)

# Example usage
if __name__ == "__main__":
    # Load your cleaned text here
    with open("../../data/processed/cleaned_text.txt", "r", encoding="utf-8") as file:
        cleaned_text = file.read()
    
    # Generate chunks
    chunks = hierarchical_chunking(cleaned_text)
    
    # Save chunks to the correct folder
    output_dir = "../../data/chunks/hierarchical"
    save_chunks(chunks, output_dir, "hierarchical")
    
    print(f"Chunks saved to {output_dir}")