#A good example of extracting paragraph to feed retriever properly for RAG use cases. 

def chunk_text(text, max_chunk_length=300):
    chunks = []
    current_chunk = ""

    for paragraph in text.split("\n"):
        for sentence in paragraph.split("."):
            sentence = sentence.strip()
            if not sentence:
                continue
            if len(current_chunk) + len(sentence) + 1 <= max_chunk_length:
                if current_chunk:
                    current_chunk += ". "
                current_chunk += sentence
            else:
                chunks.append(current_chunk)
                current_chunk = sentence
        if current_chunk:
            chunks.append(current_chunk)
            current_chunk = ""
    
    return chunks

text = """
Chunking, a cognitive strategy rooted in psychology, is instrumental in processing and retaining complex information. It involves breaking down large amounts of data into smaller, more manageable chunks, thereby reducing cognitive load and facilitating comprehension. Take, for instance, the task of memorizing a phone number: instead of attempting to recall ten individual digits, the number is naturally chunked into three segments—area code, prefix, and line number—streamlining the memorization process. Similarly, in learning new languages, chunking aids in memorizing vocabulary by grouping related words together based on common themes or categories, making them easier to recall.

Furthermore, chunking plays a crucial role in enhancing problem-solving skills. By dissecting intricate problems into smaller, more digestible components, individuals can focus on addressing each chunk sequentially, leading to a more systematic and effective problem-solving approach. This strategy allows for the identification of patterns or similarities among different elements of the problem, enabling individuals to devise targeted solutions. Ultimately, whether applied to memory retention, language learning, or problem-solving endeavors, chunking proves to be an invaluable tool in navigating the complexities of information processing and cognitive tasks.
"""

chunks = chunk_text(text)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:")
    print(chunk)
    print()
