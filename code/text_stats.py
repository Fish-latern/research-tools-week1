"""Count words in a UTF-8 text file and print the most frequent first."""

import argparse
from collections import Counter
from pathlib import Path
import re


def main():
    parser = argparse.ArgumentParser(description="统计 UTF-8 文本文件中的单词出现次数")
    parser.add_argument("file", type=Path, help="要统计的文本文件路径")
    args = parser.parse_args()

    try:
        text = args.file.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        parser.exit(1, f"读取文件失败：{exc}\n")

    # Match Unicode letters, excluding numbers and underscores.
    words = re.findall(r"[^\W\d_]+", text.casefold())
    counts = Counter(words)
    for word, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
        print(f"{word}\t{count}")


if __name__ == "__main__":
    main()
