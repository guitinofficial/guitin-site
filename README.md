# guitin.co.kr

정적 사이트(HTML/CSS/JS). 빌드 도구 없이 Vercel에 그대로 배포됩니다.

- 문구 수정: `_src/build.py`(약관은 `_src/*.part.html`)를 고친 뒤 `python3 _src/build.py` 실행
- 스타일: `assets/css/site.css` · 스크립트: `assets/js/site.js`
- 이메일 구독: 스티비 구독 페이지(`_src/build.py`의 `STIBEE`)로 연결. 주소록이 바뀌면 이 주소만 바꾸고 다시 빌드
- 캐시 갱신: CSS·JS를 바꾸면 `_src/build.py`의 `VERSION`을 올리고 다시 빌드
