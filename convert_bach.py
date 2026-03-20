import opendataloader_pdf

import time

start = time.time()

opendataloader_pdf.convert(

    input_path=["samples/"],       # 폴더 경로 → 안의 모든 PDF를 변환

    output_dir="output/",

    format="markdown,json"

)

elapsed = time.time() - start

print(f"변환 완료! 소요 시간: {elapsed:.2f}초")
