# python-101

Python 언어를 처음부터 배우는 예제 저장소. 0단계는 파이썬 소개(코드 없음), 1단계부터 35단계까지 코드 하나를 이어서 키웁니다.

## 브랜치 구조

단계마다 완료 시점의 코드가 브랜치와 태그로 남아 있습니다.

```bash
git branch -a                                    # step-01-setup, step-02-..., ...
git switch step-03-variables                     # 특정 단계 코드로 이동
git diff step-02-traceback step-03-variables     # 두 단계 사이 변경점
```

`main` 은 항상 최신 단계입니다.

## 실행

```bash
git clone https://github.com/newlecture-corp/python-101.git
cd python-101

curl -LsSf https://astral.sh/uv/install.sh | sh   # uv 설치 (처음 한 번)
uv sync                                           # Python 3.12 + 가상환경 준비

uv run python check_env.py                        # 환경 점검
```
