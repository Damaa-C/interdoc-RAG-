import os
from dotenv import load_dotenv
from groq import Groq
#from openai import OpenAI

load_dotenv()

client = Groq(api_key=os.getenv("groq_api_key"))

def build_prompt(question: str, chunks:list[str],metadatas: list[dict]):
    blocks =[]
    for i, (chunk, meta) in enumerate(zip(chunks, metadatas),start=1):
        blocks.append(f"[Source {i}: {meta['source']},chunk {meta['chunk_index']}]\n{chunk}")
    context = "\n\n".join(blocks)
    return (
        "You are a helpful assistant.Use the context below to answer the question"
        "in a friendly, clear way. If the context does not contain the answer"
        "say so politely or say you don't have enough information- do not guess"
        "Reference relevant sources using [Source N]"
        f"Context: \n{context}\n\nQuestion: {question}\n\nAnswer:"
    )


def generate_answer(question: str, search_results: dict):
    chunks = search_results["documents"][0]
    metadatas = search_results["metadatas"][0]
    # if vectorstore is empty(nothing uploaded yet),chunks will be an empty list
    # we want it to return a helpful message instead of crashing or blank prompt
    if not chunks:
        return {"answer":"No documents have been uploaded yet","sources":[]}
    
    prompt = build_prompt(question, chunks, metadatas)
    response = client.chat.completion.create(
        model = "Llama-3.3-70b-versatile",
        max_tokens = 500,
        messages = [{"role": "system", "content": prompt}]

    )
    answer_text = response.choices[0].message.content
    sources = [{"source": meta["source"], "chunk_index": meta["chunk_index"]} for meta in metadatas]
    return {"answer": answer_text, "sources": sources}
