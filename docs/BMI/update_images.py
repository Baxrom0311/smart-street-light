#!/usr/bin/env python3
"""Replace placeholder images with real screenshots in DOCX"""

from docx import Document
from docx.shared import Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

IMG = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/images/'

# Load existing doc
doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/bmi_draft.docx')

# Map old placeholder names to new real images
replacements = {
    'arxitektura.png': 'diagram_architecture.png',
    'ulash_sxemasi.png': 'screenshot_dashboard_desktop.png',  # will use diagram
    'sensor_timing.png': 'diagram_sequence.png',
    'debounce_algorithm.png': 'diagram_flowchart.png',
    'hysteresis.png': 'diagram_flowchart.png',
    'wifi_algorithm.png': 'diagram_state.png',
    'dashboard_desktop.png': 'screenshot_dashboard_desktop.png',
    'dashboard_mobile.png': 'screenshot_dashboard_mobile.png',
    'energy_graph.png': 'screenshot_stats.png',
    'state_diagram.png': 'diagram_state.png',
}

# Find and replace inline shapes (images)
from docx.opc.constants import RELATIONSHIP_TYPE as RT
import docx.opc.part

count = 0
for rel in doc.part.rels.values():
    if "image" in rel.reltype:
        old_name = rel.target_ref.split('/')[-1]
        for old, new in replacements.items():
            if old in old_name:
                new_path = IMG + new
                if os.path.exists(new_path):
                    with open(new_path, 'rb') as f:
                        rel.target_part._blob = f.read()
                    count += 1
                    print(f"Replaced: {old} -> {new}")
                break

print(f"\nTotal replaced: {count}")
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_Smart_Street_Light.docx')
print("Saved: BMI_Smart_Street_Light.docx")
