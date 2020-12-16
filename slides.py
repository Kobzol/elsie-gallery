from elsie import Slides

from part1 import features
from part2 import performance
from part3 import memory_safety
from part4 import fearless_concurrency
from utils import slide_header

COLOR1 = "black"
COLOR2 = "#f74f00"

slides = Slides()

slides.update_style("default", font="Raleway-v4020", size=36, color=COLOR1)  # Default font
slides.update_style("emph", color=COLOR2)     # Emphasis
slides.derive_style("code", "code2", size=40, align="left")


def intro(slides: Slides):
    slide = slides.new_slide()
    slide.new_style("title", size=60, bold=True)
    slide.new_style("name", size=30)
    slide.new_style("contact", size=15, color="gray")

    slide.sbox(height="30%").image("imgs/logo.svg")
    slide.box(height=80)
    slide.box().text("Rust: Fast & Safe", "title")
    slide.box(height=20)
    slide.box().text("Jakub Beránek, Mathieu Fehr, Saurabh Raje", "name")

    slide = slides.new_slide()
    slide.box(width=500).image("imgs/meme-rust-meeting.jpg")

    slide = slides.new_slide()
    content = slide_header(slide, "What is Rust?")
    content.box().text("""
System programming language for building
reliable and efficient software.""")

    content.box(height=20)
    content.box(width="fill", height=150, show="2+").image("imgs/history.svg")
    content.box(height=20)
    content.box(width="fill", height=350, show="3+").image("imgs/users.svg")


def outro(slides: Slides):
    slide = slides.new_slide()
    slide.box().text("Thanks, our curse has finally been lifted", style={"size": 50})
    slide.box(height=20)
    slide.box(show="next+").text("Now YOU have to go and spread the word about Rust",
                                 style={"size": 40})


intro(slides)
features(slides)
performance(slides)
memory_safety(slides)
fearless_concurrency(slides)
outro(slides)

slides.render("slides.pdf")
