from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.table import Table  # 테이블 활용 시 추가

# 기본 출력
print("--- [bold cyan]Rich 기본 출력 예제[/bold cyan] ---")

# 각각의 스타일을 적용한 텍스트 생성
text_italic = Text("꽉", style="italic")
text_bold = Text("꽉꽉", style="bold")
text_underline = Text("꽉꽉꽉", style="underline")
text_combo = Text("꽉꽉꽉꽉",
                  style="bold italic underline")

# 핑크색 텍스트 (hex 코드 #ff69b4 사용)
text_pink = Text("꽉꽉꽉꽉꽉", style="bold #ff69b4")

# 오리 ASCII 아트 (밝은 노란색 스타일 적용)
duck_art = (
    "   _\n"
    "<(o )___\n"
    " ( ._> /\n"
    "  `---'  "
)
text_duck = Text(duck_art, style="bold bright_yellow")

# Text.assemble을 사용하여 여러 스타일의 텍스트를 하나의 블록으로 조합
combined_text = Text.assemble(
    ("Duck say\n", "bold underline"),
    "\n\n",
    (text_italic.plain, "italic"),
    "\n",
    (text_bold.plain, "bold"),
    "\n",
    (text_underline.plain, "underline"),
    "\n",
    (text_combo.plain, "bold italic underline"),
    "\n",
    (text_pink.plain, "bold #ff69b4"),
    "\n\n",
    (text_duck.plain, "bold bright_yellow")
)

# Panel을 생성하여 강조 효과 적용 (타이틀, 서브타이틀, 테두리 스타일 설정)
panel = Panel(
    combined_text,
    title="오리는",
    subtitle="꽈악꽈악",
    border_style="green"
)

# Panel 출력
print(panel)