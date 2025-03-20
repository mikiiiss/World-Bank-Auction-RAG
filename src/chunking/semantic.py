from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import numpy as np
import os

def semantic_chunking(text, num_chunks=10):
    model = SentenceTransformer("all-MiniLM-L6-v2")  # Pre-trained embedding model
    sentences = text.split(". ")  # Split into sentences
    embeddings = model.encode(sentences)
    
    # Cluster sentences into chunks
    kmeans = KMeans(n_clusters=num_chunks)
    kmeans.fit(embeddings)
    labels = kmeans.labels_
    
    # Group sentences into chunks
    chunks = []
    for i in range(num_chunks):
        chunk = ". ".join([sentences[j] for j in range(len(sentences)) if labels[j] == i])
        chunks.append(chunk)
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
    chunks = semantic_chunking(cleaned_text, num_chunks=20)
    
    # Save chunks to the correct folder
    output_dir = "../../data/chunks/semantic"
    save_chunks(chunks, output_dir, "semantic")
    
    print(f"Chunks saved to {output_dir}")