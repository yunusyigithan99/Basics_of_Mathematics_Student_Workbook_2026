#!/usr/bin/env python3
import http.server
import socketserver
import os
import json
import re

PORT = 3333
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def regenerate_data():
    base_sol = os.path.join(DIRECTORY, '..', 'solutions')
    sections = {
        '1_Algebra': {'name': 'Algebra (Cebir)', 'topics': []},
        '2_Geometry': {'name': 'Geometry (Geometri)', 'topics': []},
        '3_Calculus': {'name': 'Calculus (Analiz)', 'topics': []}
    }

    for root, dirs, files in os.walk(base_sol):
        md_files = [f for f in files if f.endswith('.md')]
        if not md_files:
            continue
        rel = os.path.relpath(root, base_sol)
        parts = rel.split(os.sep)
        if len(parts) < 2:
            continue
        sec_key, topic_key = parts[0], parts[1]
        if sec_key not in sections:
            continue
        
        topic_data = {
            'id': topic_key,
            'title': topic_key.replace('_', ' ').title(),
            'solved_count': 0,
            'total_count': 0,
            'problems': []
        }
        
        for f in sorted(md_files):
            p_num_match = re.search(r'problem_(\d+)', f)
            p_num = int(p_num_match.group(1)) if p_num_match else 0
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fp:
                content = fp.read().strip()
            is_solved = len(content) > 200 and 'Original Problem' in content
            
            first_line = content.split('\n')[0] if content else ''
            title = first_line.replace('# ', '').strip() if first_line.startswith('# ') else f'Problem {p_num:02d}'
            
            topic_data['total_count'] += 1
            if is_solved:
                topic_data['solved_count'] += 1
                
            topic_data['problems'].append({
                'num': p_num,
                'file': f,
                'path': os.path.relpath(path, os.path.join(DIRECTORY, '..')),
                'title': title,
                'solved': is_solved,
                'chars': len(content)
            })
            
        sections[sec_key]['topics'].append(topic_data)

    for s in sections.values():
        s['topics'].sort(key=lambda x: x['id'])

    with open(os.path.join(DIRECTORY, 'data.json'), 'w', encoding='utf-8') as fp:
        json.dump(sections, fp, ensure_ascii=False, indent=2)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path.startswith('/data.json'):
            regenerate_data()
        return super().do_GET()

if __name__ == '__main__':
    regenerate_data()
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving dashboard at http://localhost:{PORT}")
        httpd.serve_forever()
