# Markdown 사용법 완벽 가이드

## 1. 제목 (Headers)

```markdown
# H1 제목
## H2 제목
### H3 제목
#### H4 제목
##### H5 제목
###### H6 제목
```

## 2. 텍스트 스타일링

### 기본 텍스트 포매팅
```markdown
**굵은 글씨**
*기울임 글씨*
~~취소선~~
`인라인 코드`
```

**굵은 글씨**  
*기울임 글씨*  
~~취소선~~  
`인라인 코드`

## 3. 목록 (Lists)

### 순서 없는 목록
```markdown
- 항목 1
- 항목 2
  - 하위 항목 2.1
  - 하위 항목 2.2
- 항목 3
```

### 순서 있는 목록
```markdown
1. 첫 번째 항목
2. 두 번째 항목
3. 세 번째 항목
```

## 4. 링크와 이미지

### 링크
```markdown
[텍스트](URL)
[GitHub](https://github.com)
```

### 이미지
```markdown
![대체 텍스트](이미지 URL)
![GitHub Logo](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)
```

## 5. 코드 블록

### 인라인 코드
```markdown
`console.log('Hello World')`
```

### 코드 블록
````markdown
```javascript
function greet(name) {
    console.log(`Hello, ${name}!`);
}
```
````

```javascript
function greet(name) {
    console.log(`Hello, ${name}!`);
}
```

## 6. 표 (Tables)

```markdown
| 헤더1 | 헤더2 | 헤더3 |
|-------|-------|-------|
| 셀1   | 셀2   | 셀3   |
| 셀4   | 셀5   | 셀6   |
```

| 헤더1 | 헤더2 | 헤더3 |
|-------|-------|-------|
| 셀1   | 셀2   | 셀3   |
| 셀4   | 셀5   | 셀6   |

## 7. 인용문

```markdown
> 이것은 인용문입니다.
> 여러 줄에 걸쳐 작성할 수 있습니다.
>> 중첩된 인용문도 가능합니다.
```

> 이것은 인용문입니다.
> 여러 줄에 걸쳐 작성할 수 있습니다.
>> 중첩된 인용문도 가능합니다.

## 8. 수평선

```markdown
---
또는
***
또는
___
```

---

## 9. 체크박스

```markdown
- [x] 완료된 항목
- [ ] 미완료 항목
- [ ] 또 다른 미완료 항목
```

- [x] 완료된 항목
- [ ] 미완료 항목
- [ ] 또 다른 미완료 항목

## 10. GitHub 특화 기능

### 이모지
```markdown
:smile: :heart: :thumbsup:
```
😊 ❤️ 👍

### 사용자 멘션
```markdown
@username
```

### 이슈 참조
```markdown
#123 (이슈 번호)
```

## 실용적인 팁

1. **미리보기 사용**: 대부분의 에디터에서 Markdown 미리보기 기능을 제공합니다.
2. **일관성 유지**: 동일한 스타일을 문서 전체에서 일관되게 사용하세요.
3. **공백 활용**: 적절한 공백과 줄바꿈으로 가독성을 높이세요.
4. **목적에 맞는 구조**: 문서의 목적에 맞게 제목과 구조를 설계하세요.

---

**작성자**: [강상욱]  
**작성일**: 2025년 9월 23일  
**GitHub**: [Your GitHub Profile]
