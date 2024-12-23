#!usr/bin/env/ python
# -*- coding:utf-8 -*-
"""
@Author :Xiaoxu Zhang
@Date   :2024/12/23
"""
import os
from fire import Fire
import json

msg_list = [
    "## title",
    "body",
    "| Index | Year | Title | Venue | CitedBy |",
    "|-------|------|-------|-------|---------|",
    "| [100](https://ieeexplore.ieee.org/abstract/document/10711878/) | 2024 | Neural network-based knowledge transfer for multitask optimization | IEEE Transactions on … | 4 |",
    "| [99](https://proceedings.neurips.cc/paper_files/paper/2023/hash/b2fe1ee8d936ac08dd26f2ff58986c8f-Abstract-Conference.html) | 2024 | Famo: Fast adaptive multitask optimization | Advances in Neural … | 18 |",
    "| [98](https://ieeexplore.ieee.org/abstract/document/10398471/) | 2024 | Multiobjective multitask optimization with multiple knowledge types and transfer adaptation | IEEE Transactions on Evolutionary Computation | 18 |",
    "| [97](https://www.sciencedirect.com/science/article/pii/S0020025524008351) | 2024 | MOREM: An Evolutionary Multitasking Optimization Algorithm for Multi-Objective Recommendations | Information Sciences | 0 |",
]

def convert_to_markdown_content(msg_lst):
    return "\\n".join(msg_lst).replace(' \u2026', '')

def escape_markdown_characters(content):
    return content.replace("'", "'\\''").replace("(", "\\(").replace(")", "\\)")

class TestCreate:
    def __init__(self):
        pass

    @staticmethod
    def run(mode='dev'):
        content = convert_to_markdown_content(msg_list)
        content = escape_markdown_characters(content)
        if mode == 'prod':
            env_file = os.getenv("GITHUB_ENV")
        else:
            env_file = "preview"
        with open(env_file, "a") as f:
            f.write(f"MSG=\"{content}\"")

if __name__ == '__main__':
    Fire(TestCreate).run()
