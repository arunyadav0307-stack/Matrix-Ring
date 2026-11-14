#!/usr/bin/env python3
"""Correct planning-only locator endpoints found by delivery preflight.
Read/write only newly authored, unsealed files; never frozen source copies.
"""
from pathlib import Path
B=Path(__file__).resolve().parents[1]
paths=[B/'MASTER_CORRECTION_REGISTER.md',B/'evidence/correction_actions.json',B/'evidence/master_correction_register.csv',B/'evidence/source_reading_observations.md',B/'scripts/capture_plan_sources.py']
changes=0
for p in paths:
 text=p.read_text();new=text
 for before,after in [('319-380','319-379'),('347-375','347-374'),('sections/appendix_tables.tex:96-126','sections/appendix_tables.tex:96-120'),('sections/05_hulls.tex:355–380','sections/05_hulls.tex:355–379'),("'sections/05_hulls.tex',355,380,","'sections/05_hulls.tex',355,379,")]:new=new.replace(before,after)
 if new!=text:p.write_text(new);changes+=1
assert changes==5,('One-time plan locator refinement expected five authored files',changes)
print('Corrected five action target endpoints and the matching supplemental locator; no manuscript or copied audit/source evidence changed.')
