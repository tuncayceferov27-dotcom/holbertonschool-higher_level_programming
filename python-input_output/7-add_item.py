#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then saves them to a file.
"""
import sys
import os

# Əvvəlki tapşırıqlardakı funksiyaları import edirik
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# 1. Əgər fayl varsa, içindəkiləri oxu, yoxdursa boş siyahı yarat
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# 2. Yeni arqumentləri siyahıya əlavə et (sys.argv[0] skriptin adıdır, onu keçirik)
items.extend(sys.argv[1:])

# 3. Siyahını yenidən fayla yaz
save_to_json_file(items, filename)
