# ===================== LEVEL: HARD =====================
# TASK 8: Anagram Groups and Set Operations
#
# PART A - Anagram groups
#   Anagrams are words made of the same letters (e.g. "listen" and "silent").
#   Given:
#       words = ["listen", "silent", "enlist", "google", "gogole",
#                "cat", "act", "tac", "dog"]
#   1. Group the anagrams together using a dictionary.
#      (hint: sorted letters of the word as a tuple/string can be the key)
#   2. Print only the groups that have 2 or more words.
#
#   Expected output (order may differ):
#       ['listen', 'silent', 'enlist']
#       ['google', 'gogole']
#       ['cat', 'act', 'tac']
#
# PART B - Set operations
#   Given:
#       python_students = {"Ali", "Leyla", "Orxan", "Aysel"}
#       java_students   = {"Leyla", "Nigar", "Aysel", "Tural"}
#   Print:
#     1. Students who study both courses (intersection)
#     2. Students who study at least one course (union)
#     3. Students who study only Python (difference)
#     4. Students who study exactly one course (symmetric difference)
#
# Bonus: Write a function is_anagram(a, b) and solve Part A without sorting,
#        using a dictionary of letter counts.
#
# Concepts: dict with tuple keys, grouping, sorted(), set operations

# Write your code below:
