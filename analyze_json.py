import json

#with open("output/lorem.json", "r", encoding="utf-8") as f:
with open("output/Beginning+STM32.json", "r", encoding="utf-8") as f:
    doc = json.load(f)

# 문서 기본 정보

print("===문서 정보===")

print(f"파일명:{doc['file name']}")

print(f"페이지 수: {doc['number of pages']}")

print()

# 요소 분석 

kids = doc["kids"]

print(f"===추출된 요소 : 총 {len(kids)}개===")

print()

# 요소 타입별 개수 세기

type_count ={}

for elements in kids:
    t= elements["type"]
    type_count[t] = type_count.get(t,0) + 1
print("타입별 개수:")
for t, count in type_count.items():
    print(f" {t}:{count}개")
print()

# 첫 3개 요소 미리보기
print("=== 첫 3개 요소 미리보기 ===")
for i, element in enumerate(kids[:3]):
    print(f"\n[{i}] 타입: {element['type']}")
    print(f"    페이지: {element.get('page number', '?')}")
    if "content" in element:
        content = element["content"]
        preview = content[:80] + "..." if len(content) > 80 else content
        print(f"    내용: {preview}")
    if "bounding box" in element:
        bb = element["bounding box"]  # [x1, y1, x2, y2] 형식
        print(f"    영역: ({bb[0]:.1f}, {bb[1]:.1f}) → ({bb[2]:.1f}, {bb[3]:.1f})")


