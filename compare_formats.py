import opendataloader_pdf

formats = ["markdown", "json", "text", "html"]

for fmt in formats:

    opendataloader_pdf.convert(

        input_path=["samples/lorem.pdf"],

        output_dir=f"output/{fmt}/",

        format=fmt

    )

    print(f"{fmt} 변환 완료 → output/{fmt}/")
