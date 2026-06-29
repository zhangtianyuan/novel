"""小说写入工具：将新章节追加到正文.md末尾"""
import sys
from pathlib import Path

NOVEL_DIR = Path(r"C:\Users\Admin\.openclaw\workspace\novel")
BODY_FILE = NOVEL_DIR / "正文.md"

def append_chapter(chapter_title: str, content: str) -> None:
    """在正文.md末尾追加新章节"""
    text = BODY_FILE.read_text(encoding="utf-8")
    separator = "\n\n---\n\n" if text.strip() else ""
    text += f"{separator}{content.strip()}\n"
    BODY_FILE.write_text(text, encoding="utf-8")
    print(f"[OK] 已追加: {chapter_title}")

def read_tail(num_chars: int = 5000) -> str:
    """读取正文.md末尾内容，用于查看最新剧情"""
    text = BODY_FILE.read_text(encoding="utf-8")
    return text[-num_chars:]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python novel_save.py append '第X章 标题' < content.txt")
        print("      python novel_save.py tail [字符数]")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "append":
        title = sys.argv[2] if len(sys.argv) > 2 else "新章"
        content = sys.stdin.read()
        append_chapter(title, content)
    elif cmd == "tail":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
        print(read_tail(n))
    else:
        print(f"未知命令: {cmd}")
