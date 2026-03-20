import json

#with open("output/lorem.json", "r", encoding="utf-8") as f:
with open("output/Beginning+STM32.json", "r", encoding="utf-8") as f:

    doc = json.load(f)


def chunk_by_element(doc):

    """방법 1: 요소별 청킹 — 각 문단/제목을 하나의 청크로"""

    chunks = []

    for element in doc["kids"]:

        if "content" in element and element["content"].strip():

            chunks.append({

                "text": element["content"],

                "type": element["type"],

                "page": element.get("page number", 0),

            })

    return chunks


def chunk_by_section(doc):

    """방법 2: 섹션별 청킹 — 제목 아래의 내용을 하나로 묶기"""

    chunks = []

    current_heading = "문서 시작"

    current_texts = []

    for element in doc["kids"]:

        if element["type"] == "heading":

            if current_texts:

                chunks.append({

                    "heading": current_heading,

                    "text": "\n".join(current_texts),

                })

            current_heading = element.get("content", "제목 없음")

            current_texts = []

        elif "content" in element and element["content"].strip():

            current_texts.append(element["content"])

    if current_texts:

        chunks.append({

            "heading": current_heading,

            "text": "\n".join(current_texts),

        })

    return chunks


# 방법 1: 요소별

element_chunks = chunk_by_element(doc)

print(f"=== 요소별 청킹: {len(element_chunks)}개 청크 ===")

for i, chunk in enumerate(element_chunks[:3]):

    preview = chunk["text"][:60] + "..." if len(chunk["text"]) > 60 else chunk["text"]

    print(f"  [{i}] ({chunk['type']}) {preview}")

print()

# 방법 2: 섹션별

section_chunks = chunk_by_section(doc)

print(f"=== 섹션별 청킹: {len(section_chunks)}개 청크 ===")

for i, chunk in enumerate(section_chunks[:3]):

    print(f"  [{i}] 제목: {chunk['heading']}")

    print(f"       내용: {chunk['text'][:60]}...")

    print()
