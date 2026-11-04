"""1단계 환경 점검 스크립트.

실행:  uv run python check_env.py

확인하는 것
  1. Python 버전이 3.12 인가
  2. 시스템 Python 이 아니라 이 프로젝트의 가상환경(.venv) 안에서 실행되고 있는가
  3. 프로젝트 파일(pyproject.toml, uv.lock)이 제자리에 있는가
"""

import sys
from pathlib import Path


def main() -> int:
    ok = True

    version = sys.version.split()[0]
    print(f"Python       : {version}")
    if sys.version_info[:2] != (3, 12):
        print("  -> 3.12 가 아닙니다. 'uv run python check_env.py' 로 실행했는지 확인하세요.")
        ok = False

    in_venv = ".venv" in Path(sys.prefix).parts
    print(f"가상환경      : {'프로젝트 .venv 안' if in_venv else '아님'}")
    if not in_venv:
        print("  -> 시스템 Python 으로 실행됐습니다. 'uv run' 을 앞에 붙이세요.")
        ok = False

    here = Path(__file__).parent
    for name in ("pyproject.toml", "uv.lock", ".python-version"):
        exists = (here / name).exists()
        print(f"{name:<14}: {'있음' if exists else '없음'}")
        if not exists:
            ok = False
    if not (here / "uv.lock").exists():
        print("  -> uv sync 를 한 번 실행하세요.")

    if not ok:
        return 1
    print("\n환경 준비 완료. 2단계로 넘어가세요.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
