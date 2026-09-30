"""loc —— 统计一个目录下所有 .py 文件的行数。

用法:  python3 loc.py <目录>
"""
import sys
from pathlib import Path


def py_files(root: str):
    """产出 ROOT 下(含子目录)所有 .py 文件,按路径排序。"""
    return sorted(Path(root).rglob("*.py"))


def count_lines(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines())


def main(argv):
    root = argv[1] if len(argv) > 1 else "."
    total = 0
    for path in py_files(root):
        n = count_lines(path)
        total += n
        print(f"{path} {n}")
    print(f"TOTAL {total}")


if __name__ == "__main__":
    main(sys.argv)
