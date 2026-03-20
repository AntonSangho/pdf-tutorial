import opendataloader_pdf 

opendataloader_pdf.convert(
    #input_path=["samples/lorem.pdf"],
    input_path=["samples/The_Art_of_Electronics_3rd.pdf"],
    #input_path=["samples/Beginning+STM32.pdf"],
    output_dir="output/",
    format="markdown,json"
)
print("변환 완료! output/폴더를 확인하세요")