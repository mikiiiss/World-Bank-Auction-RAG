from transformers import AutoTokenizer
import os

def fixed_size_chunking(text, chunk_size=256, overlap=50):
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")  # Use any tokenizer
    tokens = tokenizer.tokenize(text)
    chunks = []
    for i in range(0, len(tokens), chunk_size - overlap):
        chunk = tokens[i:i + chunk_size]
        chunks.append(tokenizer.convert_tokens_to_string(chunk))
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
    chunks = fixed_size_chunking(cleaned_text, chunk_size=256, overlap=50)
    
    # Save chunks to the correct folder
    output_dir = "../../data/chunks/fixed_size"
    save_chunks(chunks, output_dir, "fixed_size")
    
    print(f"Chunks saved to {output_dir}")