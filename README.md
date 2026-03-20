# pdf-tutorial

[opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf)를 활용한 PDF 데이터 추출 튜토리얼 프로젝트입니다.

PDF 문서에서 텍스트, 표, 이미지를 자동으로 추출하고, RAG(검색 증강 생성)에 활용할 수 있도록 청킹하는 과정을 다룹니다.

## 요구사항

- Python 3.x
- Java 11 ([Adoptium](https://adoptium.net/temurin/releases/?os=windows&arch=x64&package=jdk&version=11))
- GPU (하이브리드 모드 사용 시)

## 설치

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
# .\\venv\\Scripts\\activate   # Windows

pip install opendataloader-pdf
```

## 스크립트 설명

| 파일 | 설명 |
|------|------|
| `convert_basic.py` | PDF → Markdown/JSON 기본 변환 |
| `convert_bach.py` | `samples/` 폴더 내 PDF 일괄 변환 |
| `convert_hybrid.py` | GPU 하이브리드 모드 변환 (이미지 설명 생성 포함) |
| `analyze_json.py` | 추출된 JSON 구조 분석 (타입별 개수, 요소 미리보기) |
| `chunking.py` | RAG용 텍스트 청킹 (요소별 / 섹션별) |
| `compare_formats.py` | markdown, json, text, html 4가지 포맷 비교 변환 |

## 사용법

### 기본 변환

```bash
python convert_basic.py
```

`output/` 폴더에 Markdown과 JSON 파일이 생성됩니다.

### 일괄 변환

`samples/` 폴더에 PDF를 넣고 실행합니다.

```bash
python convert_bach.py
```

### 하이브리드 모드 (GPU)

터미널 1에서 서버를 시작합니다.

```bash
opendataloader-pdf-hybrid --port 5002 --enrich-picture-description
```

터미널 2에서 변환을 실행합니다.

```bash
python convert_hybrid.py
```

### JSON 분석 및 청킹

```bash
python analyze_json.py
python chunking.py
```

## 디렉토리 구조

```
pdf-tutorial/
├── samples/          # 입력 PDF 파일
├── output/           # 변환 결과 (gitignore)
├── convert_basic.py
├── convert_bach.py
├── convert_hybrid.py
├── analyze_json.py
├── chunking.py
└── compare_formats.py
```

## 참고

- [opendataloader-pdf GitHub](https://github.com/opendataloader-project/opendataloader-pdf)
- [opendataloader 공식 문서](https://opendataloader.org)
