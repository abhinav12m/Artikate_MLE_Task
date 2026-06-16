from pathlib import Path

import fitz
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents(folder="data"):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    chunks = []

    for pdf_file in Path(folder).glob("*.pdf"):

        doc = fitz.open(pdf_file)

        for page_num in range(len(doc)):

            page = doc[page_num]
            text = page.get_text()

            page_chunks = splitter.split_text(text)

            for chunk in page_chunks:

                chunks.append(
                    {
                        "text": chunk,
                        "document": pdf_file.name,
                        "page": page_num + 1,
                    }
                )

    return chunks