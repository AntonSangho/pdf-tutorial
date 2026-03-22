import glob
import opendataloader_pdf

opendataloader_pdf.convert(
    input_path=glob.glob("samples/*.pdf"),
    output_dir="output/",
    format="markdown,json"
)
print("변환 완료! output/폴더를 확인하세요")
