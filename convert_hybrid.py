"""
Hybrid 모드: PDF → Markdown 변환 + 이미지 설명 생성 (GPU 사용)

사용법:
  1. 터미널 1에서 hybrid 서버 시작:
     opendataloader-pdf-hybrid --port 5002 --enrich-picture-description

  2. 터미널 2에서 이 스크립트 실행:
     python convert_hybrid.py
"""

import opendataloader_pdf
import time

# === 설정 ===
#INPUT_PDF = "samples/The_Art_of_Electronics_3rd.pdf"
INPUT_PDF = "samples/Beginning+STM32.pdf"
OUTPUT_DIR = "output_hybrid/"
HYBRID_URL = "http://localhost:5002"

print(f"입력: {INPUT_PDF}")
print(f"출력: {OUTPUT_DIR}")
print(f"서버: {HYBRID_URL}")
print()

start = time.time()

opendataloader_pdf.convert(
    input_path=[INPUT_PDF],
    output_dir=OUTPUT_DIR,
    format="markdown,json",
    hybrid="docling-fast",
    hybrid_url=HYBRID_URL,
    hybrid_timeout="120000",
)

elapsed = time.time() - start
print(f"\n변환 완료! 소요 시간: {elapsed:.1f}초")
print(f"결과 파일: {OUTPUT_DIR}")
