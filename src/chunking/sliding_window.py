from transformers import AutoTokenizer
import os

def sliding_window_chunking(text, window_size=256, step_size=128):
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")  # Use any tokenizer
    
    # Split the text into smaller parts (e.g., paragraphs)
    paragraphs = text.split("\n\n")  # Split by double newlines (assuming paragraphs are separated this way)
    
    chunks = []
    for paragraph in paragraphs:
        # Tokenize each paragraph separately
        tokens = tokenizer.tokenize(paragraph)
        for i in range(0, len(tokens), step_size):
            chunk = tokens[i:i + window_size]
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
    chunks = sliding_window_chunking(cleaned_text, window_size=256, step_size=128)
    
    # Save chunks to the correct folder
    output_dir = "../../data/chunks/sliding_window"
    save_chunks(chunks, output_dir, "sliding_window")
    
    print(f"Chunks saved to {output_dir}")