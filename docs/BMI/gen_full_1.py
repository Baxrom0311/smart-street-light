#!/usr/bin/env python3
"""Full BMI - expanded to 70+ pages"""

from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document()
IMG = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/images/'

style = doc.styles['Normal']
style.font.name = 'Times New Roman'; style.font.size = Pt(14)
style.paragraph_format.line_spacing = 1.5
for s in doc.sections:
    s.top_margin = Cm(2); s.bottom_margin = Cm(2)
    s.left_margin = Cm(3); s.right_margin = Cm(1.5)

def hc(t, sz=16):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(t); r.bold = True; r.font.size = Pt(sz); r.font.name = 'Times New Roman'
def h2(t):
    doc.add_paragraph()
    p = doc.add_paragraph(); r = p.add_run(t); r.bold = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'
def h3(t):
    p = doc.add_paragraph(); r = p.add_run(t); r.bold = True; r.italic = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'
def t(text):
    p = doc.add_paragraph(text); p.paragraph_format.first_line_indent = Cm(1.25)
    for r in p.runs: r.font.name = 'Times New Roman'; r.font.size = Pt(14)
def img(name, caption="", w=Cm(14)):
    path = IMG + name
    if os.path.exists(path):
        doc.add_picture(path, width=w)
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    if caption:
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(caption); r.font.size = Pt(12); r.italic = True; r.font.name = 'Times New Roman'
def tbl(headers, rows, caption=""):
    if caption:
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(caption); r.font.size = Pt(12); r.italic = True; r.font.name = 'Times New Roman'
    tb = doc.add_table(rows=1+len(rows), cols=len(headers)); tb.style = 'Table Grid'
    for i, hd in enumerate(headers):
        c = tb.rows[0].cells[i]; c.text = hd
        for p in c.paragraphs:
            for r in p.runs: r.bold = True
    for ri, row in enumerate(rows):
        for ci, v in enumerate(row): tb.rows[ri+1].cells[ci].text = str(v)
    doc.add_paragraph()
def code(text):
    p = doc.add_paragraph()
    r = p.add_run(text); r.font.name = 'Courier New'; r.font.size = Pt(11)
    p.paragraph_format.left_indent = Cm(1)

# ==================== TITUL ====================
for _ in range(3): doc.add_paragraph()
hc("O'ZBEKISTON RESPUBLIKASI\nOLIY TA'LIM, FAN VA INNOVATSIYALAR VAZIRLIGI")
hc("MUHAMMAD AL-XORAZMIY NOMIDAGI\nTOSHKENT AXBOROT TEXNOLOGIYALARI UNIVERSITETI")
doc.add_paragraph()
hc('"KOMPYUTER INJINIRINGI" FAKULTETI\n"DASTURIY INJINIRING" KAFEDRASI')
for _ in range(2): doc.add_paragraph()
hc("BITIRUV MALAKAVIY ISHI", 18)
doc.add_paragraph()
hc('Mavzu:\n"SMART STREET TIZIMIDA ULTRATOVUSH SENSORI ORQALI\nENERGIYA TEJAMKORLIGINI TA\'MINLOVCHI\nYORITISH TIZIMINI ISHLAB CHIQISH"', 14)
for _ in range(3): doc.add_paragraph()
t("Bajardi: _______________________")
t("Ilmiy rahbar: _______________________")
for _ in range(4): doc.add_paragraph()
hc("Toshkent — 2026")
doc.add_page_break()

# ==================== MUNDARIJA ====================
hc("MUNDARIJA")
doc.add_paragraph()
items = [
    ("KIRISH", "4"), ("", ""),
    ("I BOB. SMART STREET TIZIMIDA YORITISH TIZIMLARI TIZIMLI TAHLILI VA MASALANING QO'YILISHI", ""),
    ("1.1. Smart Street tizimlarida energiya tejamkor yoritish tizimlari va ularning ahamiyati", "9"),
    ("1.2. Ultratovush sensorlarning ishlash prinsipi va texnik xususiyatlari", "20"),
    ("1.3. Masalaning qo'yilishi", "32"),
    ("", ""),
    ("II BOB. AMALIY QISM", ""),
    ("2.1. Tizimni loyihalash: texnik vositalar va komponentlarni tanlash", "36"),
    ("2.2. Masofani aniqlash algoritmi: ultrasonic sensor yordamida obyektni aniqlash", "46"),
    ("2.3. Yoritish tizimini boshqarish dasturi va tizimning ishlash jarayoni va natijalar tahlili", "55"),
    ("", ""),
    ("XULOSA", "66"),
    ("FOYDALANILGAN ADABIYOTLAR RO'YXATI", "69"),
    ("ILOVALAR", "71"),
]
for title, page in items:
    if not title: continue
    p = doc.add_paragraph()
    dots = '.' * max(3, 65 - len(title)) if page else ''
    r = p.add_run(f"{title} {dots} {page}")
    r.font.name = 'Times New Roman'; r.font.size = Pt(14)
    if not page: r.bold = True
doc.add_page_break()

print("Titul + Mundarija done")
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_full.docx')
