#!/usr/bin/env python3
"""
Basics of Mathematics Student Workbook 2026 - Interactive Presentation & Evaluation Server
Lightweight local HTTP server for workbook review, evaluation, and presentation.
"""

import http.server
import socketserver
import os
import json
import re

PORT = 3333
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(DIRECTORY)
SOLUTIONS_DIR = os.path.join(BASE_DIR, 'solutions')
EXERCISES_DIR = os.path.join(BASE_DIR, 'exercises')

def regenerate_data():
    """Generates a complete dataset including exercises, solutions, and parsed sections."""
    exercises_cache = {}
    if os.path.isdir(EXERCISES_DIR):
        for root, dirs, files in os.walk(EXERCISES_DIR):
            for f in sorted(files):
                if f.endswith('_en.md'):
                    parts = os.path.relpath(root, EXERCISES_DIR).split(os.sep)
                    sec = parts[0]
                    top_key = f.replace('_en.md', '')
                    key = f'{sec}/{top_key}'
                    with open(os.path.join(root, f), 'r', encoding='utf-8') as fp:
                        txt = fp.read()
                    matches = re.findall(
                        r'###\s+(?:Problem|Exercise)\s+(\d+)\.?(.*?)(?=(?:###\s+(?:Problem|Exercise)\s+\d+|\Z))',
                        txt, re.DOTALL
                    )
                    exercises_cache[key] = {int(m[0]): m[1].strip() for m in matches}

    sections_def = {
        '1_Algebra': {'name': '1_Algebra', 'display_name': 'Algebra', 'topics': []},
        '2_Geometry': {'name': '2_Geometry', 'display_name': 'Geometry', 'topics': []},
        '3_Calculus': {'name': '3_Calculus', 'display_name': 'Calculus', 'topics': []}
    }

    all_problems = []
    for sec_key, sec_val in sections_def.items():
        sec_path = os.path.join(SOLUTIONS_DIR, sec_key)
        if not os.path.isdir(sec_path):
            continue
        for topic_dir in sorted(os.listdir(sec_path)):
            top_path = os.path.join(sec_path, topic_dir)
            if not os.path.isdir(top_path):
                continue
            topic_title = topic_dir.replace('_', ' ').title()
            topic_data = {
                'id': topic_dir,
                'title': topic_title,
                'category_id': sec_key,
                'category_name': sec_val['name'],
                'problems': []
            }
            for i in range(1, 16):
                fn = f'problem_{i:02d}_solution.md'
                sol_path = os.path.join(top_path, fn)
                if not os.path.exists(sol_path):
                    continue
                with open(sol_path, 'r', encoding='utf-8') as fp:
                    sol_txt = fp.read()

                first_line = sol_txt.split('\n')[0].strip()
                title = first_line.replace('# ', '').strip() if first_line.startswith('# ') else f'Problem {i:02d}'

                ex_key = f'{sec_key}/{topic_dir}'
                q_txt = exercises_cache.get(ex_key, {}).get(i, '')
                if not q_txt:
                    sec1_match = re.search(r'##\s+1\.\s*Original Problem\s*\n(.*?)(?=(?:##|\Z))', sol_txt, re.DOTALL)
                    q_txt = sec1_match.group(1).strip() if sec1_match else ''

                parsed_secs = []
                for sm in re.finditer(r'##\s+(\d+)\.\s*(.*?)\n(.*?)(?=(?:##\s+\d+\.|\Z))', sol_txt, re.DOTALL):
                    parsed_secs.append({
                        'num': int(sm.group(1)),
                        'title': sm.group(2).strip(),
                        'content': sm.group(3).strip()
                    })

                is_solved = len(sol_txt) > 200 and 'Original Problem' in sol_txt
                p_obj = {
                    'id': f'{sec_key}_{topic_dir}_{i:02d}',
                    'category_id': sec_key,
                    'category_name': sec_val['name'],
                    'topic_id': topic_dir,
                    'topic_title': topic_title,
                    'num': i,
                    'title': title,
                    'path': os.path.relpath(sol_path, BASE_DIR),
                    'question_md': q_txt,
                    'solution_md': sol_txt,
                    'sections': parsed_secs,
                    'chars': len(sol_txt),
                    'solved': is_solved
                }
                topic_data['problems'].append(p_obj)
                all_problems.append(p_obj)
            sections_def[sec_key]['topics'].append(topic_data)

    out_file = os.path.join(DIRECTORY, 'data.json')
    with open(out_file, 'w', encoding='utf-8') as fp:
        json.dump({
            'sections': sections_def,
            'total_problems': len(all_problems),
            'solved_problems': sum(1 for p in all_problems if p['solved'])
        }, fp, ensure_ascii=False)


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path.startswith('/data.json'):
            # Only regenerate if explicitly refreshed or modified
            if 'refresh=1' in self.path:
                regenerate_data()
        return super().do_GET()


if __name__ == '__main__':
    regenerate_data()
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving workbook evaluation portal at http://localhost:{PORT}")
        httpd.serve_forever()
