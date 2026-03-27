import re
from typing import List, Tuple, Optional

def parse_verse(verse_str: str) -> Tuple[int, Optional[str]]:
    """
    Parse a verse string such as "10", "10a" into a tuple: (10, None) or (10, "a")
    """
    m = re.match(r"(\d+)([a-z]?)", verse_str)
    if not m:
        raise ValueError("Invalid verse: " + verse_str)
    num = int(m.group(1))
    letter = m.group(2) if m.group(2) != "" else None
    return (num, letter)

def verse_to_float(verse: Tuple[int, Optional[str]]) -> float:
    """
    Convert a verse (num, letter) into a float value so that 13 -> 13.0, 13a -> 13.1, 13b -> 13.2, etc.
    """
    num, letter = verse
    offset = 0.0
    if letter:
        offset = (ord(letter) - ord('a') + 1) / 10.0
    return num + offset

def merge_numbers(numbers: List[int]) -> List[Tuple[int, int]]:
    """
    Given a list of integers, merge consecutive ones.
    For example: [5,6,10,13] => [(5,6), (10,10), (13,13)]
    """
    numbers = sorted(numbers)
    merged = []
    start = numbers[0]
    prev = numbers[0]
    for n in numbers[1:]:
        if n == prev + 1:
            prev = n
        else:
            merged.append((start, prev))
            start = n
            prev = n
    merged.append((start, prev))
    return merged

def merge_verse_ranges(ranges: List[Tuple[Tuple[int, Optional[str]], Tuple[int, Optional[str]], str, str]]) -> str:
    """
    Given a list of verse ranges for one chapter (each as:
      (start_tuple, end_tuple, start_orig, end_orig)
    merge contiguous or overlapping ranges.
    
    For instance, for:
      [ ( (10, 'a'), (12, None), "10a", "12" ),
        ( (11, None), (20, None), "11", "20" ) ]
    the merged result will be "10a-20" (unless both citations use verse 13 with different parts – then the lower letter is dropped).
    
    When two ranges share the same starting integer (e.g. "13a" and "13b-20"),
    we output "13-20" (dropping the letter on the lower bound).
    Otherwise the first citation’s lower bound is kept.
    """
    # Sort by starting verse (using our numeric float value)
    ranges = sorted(ranges, key=lambda r: verse_to_float(r[0]))
    merged = []
    current = ranges[0]
    # Also record all original start strings in the merged group
    current_start_orig_list = [current[2]]
    for r in ranges[1:]:
        current_end_val = verse_to_float(current[1])
        r_start_val = verse_to_float(r[0])
        # We'll consider ranges contiguous if the new start is nearly what would follow the current end.
        # (This simple check works for our examples.)
        if r_start_val <= current_end_val + 0.11:
            # They overlap or are contiguous.
            if verse_to_float(r[1]) > current_end_val:
                # Extend the current range end.
                current = (current[0], r[1], current[2], r[3])
            current_start_orig_list.append(r[2])
        else:
            merged.append((current, current_start_orig_list))
            current = r
            current_start_orig_list = [r[2]]
    merged.append((current, current_start_orig_list))
    
    # Format each merged range.
    result_parts = []
    for (rng, start_orig_list) in merged:
        start_tuple, end_tuple, start_orig, end_orig = rng
        # If all original lower-bound strings (from the merged group) come from the same integer,
        # then we drop the letter (if any) and use just the number.
        nums = [parse_verse(s)[0] for s in start_orig_list]
        if all(n == nums[0] for n in nums):
            start_str = str(nums[0])
        else:
            start_str = start_orig
        # If the range is a single verse, output just one number.
        if verse_to_float(start_tuple) == verse_to_float(rng[1]):
            result_parts.append(start_str)
        else:
            result_parts.append(f"{start_str}-{end_orig}")

    i = 0
    while i < len(result_parts) - 1:
        a = result_parts[i].split('-')[-1]
        b = result_parts[i+1].split('-')[0]
        if int(a)+1 == int(b):
            new = result_parts[i].split('-')[0] + '-' + result_parts[i+1].split('-')[-1]
            result_parts.pop(i+1)
            result_parts.pop(i)
            result_parts.insert(i, new)
        else:
            i += 1
    
    return ".".join(result_parts)

def parse_citation(citation: str) -> dict:
    """
    Parse a citation string into its parts.
    
    The citation may be in one of these forms:
      - "Gv 1"  → book and chapter (chapter-only)
      - "Gd"    → book only
      - "1 Sam 3-5" → book and chapter range
      - "Mt 5, 10"  → book, chapter and verse
      - "1 Tm 10, 15-20" → book, chapter and verse range
      - "Mt 3, 58a"  → book, chapter and verse with part letter
      - "Mt 10, 8a-10" → book, chapter and verse range with part letter
    """
    pattern = r"^(?P<book>(?:\d\s*)?[A-Za-z]+(?:\s*[A-Za-z]+)?)\s*(?P<chapter>\d+(?:-\d+)?)?\s*(?:,\s*(?P<verses>\d+[a-z]?(?:-\d+[a-z]?)?))?\s*$"
    m = re.match(pattern, citation)
    if not m:
        raise ValueError("Invalid citation: " + citation)
    book = m.group("book").strip()
    chapter_str = m.group("chapter")
    verses_str = m.group("verses")
    if chapter_str is None:
        # Book-only citation (e.g. "Gd")
        return {"book": book, "type": "book"}
    else:
        if verses_str is None:
            # Chapter-only citation (or a chapter range like "3-5")
            if "-" in chapter_str:
                parts = chapter_str.split("-")
                start = int(parts[0])
                end = int(parts[1])
            else:
                start = int(chapter_str)
                end = start
            return {"book": book, "type": "chapter", "chapter_range": (start, end)}
        else:
            # Citation with verses. (Assume chapter is a single number.)
            chapter = int(chapter_str)
            if "-" in verses_str:
                parts = verses_str.split("-")
                verse_start = parse_verse(parts[0])
                verse_end = parse_verse(parts[1])
            else:
                verse_start = parse_verse(verses_str)
                verse_end = verse_start
            return {"book": book, "type": "verse", "chapter": chapter, "verses": (verse_start, verse_end)}

def merge_bible_citations(citations: List[str]) -> str:
    """
    Given a list of citation strings, merge them according to the conventions.
    
    Examples:
      - ["Gv 1", "Gv 2"]  → "Gv 1-2"
      - ["Dt 10", "Dt 11", "Dt 12", "Dt 13"] → "Dt 10-13"
      - ["Nm 5", "Nm 6", "Nm 10", "Nm 13"] → "Nm 5-6; 10; 13"
      - ["1 Sam 3, 10-15", "1 Sam 3, 16-18"] → "1 Sam 3, 10-18"
      - ["Mt 10, 13a", "Mt 10, 13b-20"] → "Mt 10, 13-20"
    """
    if len(citations) == 1:
        return citations[0]
    parsed_list = [parse_citation(c) for c in citations]
    # Group citations by book.
    groups = {}
    book_order = []  # preserve first-occurrence order
    for item in parsed_list:
        book = item["book"]
        if book not in groups:
            groups[book] = {"book_only": False, "chapters": set(), "verses": {}}
            book_order.append(book)
        if item["type"] == "book":
            groups[book]["book_only"] = True
        elif item["type"] == "chapter":
            start, end = item["chapter_range"]
            for ch in range(start, end+1):
                groups[book]["chapters"].add(ch)
        elif item["type"] == "verse":
            ch = item["chapter"]
            # Save the verse range along with “original” string versions.
            def verse_to_str(v):
                num, letter = v
                return f"{num}{letter}" if letter else f"{num}"
            vs = verse_to_str(item["verses"][0])
            ve = verse_to_str(item["verses"][1])
            if ch not in groups[book]["verses"]:
                groups[book]["verses"][ch] = []
            groups[book]["verses"][ch].append((item["verses"][0], item["verses"][1], vs, ve))
    
    # Build the merged output for each book.
    book_outputs = []
    for book in book_order:
        group = groups[book]
        parts = []
        # (A) Chapters without verses.
        if group["chapters"]:
            merged_chapters = merge_numbers(sorted(group["chapters"]))
            chapter_parts = []
            for start, end in merged_chapters:
                if start == end:
                    chapter_parts.append(str(start))
                else:
                    chapter_parts.append(f"{start}-{end}")
            parts.append("; ".join(chapter_parts))
        # (B) Verses (grouped by chapter).
        verse_parts = []
        for ch in sorted(group["verses"].keys()):
            merged_verses = merge_verse_ranges(group["verses"][ch])
            verse_parts.append(f"{ch}, {merged_verses}")
        if verse_parts:
            parts.append("; ".join(verse_parts))
        # Combine parts for the book.
        combined = "; ".join(parts) if parts else ""
        if group["book_only"]:
            # If a book-only citation was given (e.g. "Gd"), output it.
            if combined:
                book_out = f"{book}; {book} {combined}"
            else:
                book_out = book
        else:
            if combined:
                book_out = f"{book} {combined}"
            else:
                book_out = book
        book_outputs.append(book_out)
    
    return "; ".join(book_outputs)

# === Testing with the provided examples ===
if __name__ == '__main__':
    examples = [
        (["Gv 1", "Gv 2"], "Gv 1-2"),
        (["Dt 10", "Dt 11", "Dt 12", "Dt 13"], "Dt 10-13"),
        (["Nm 5", "Nm 6", "Nm 10", "Nm 13"], "Nm 5-6; 10; 13"),
        (["Es 1", "Es 2", "Es 3", "Lv 1"], "Es 1-3; Lv 1"),
        (["Gn 7", "Gn 8", "Gn 9", "Gn 20", "Gn 21"], "Gn 7-9; 20-21"),
        (["Ap 1", "Ap 3"], "Ap 1; 3"),
        (["Lc 22", "Mt 28"], "Lc 22; Mt 28"),
        (["Rm 1", "1 Cor 2"], "Rm 1; 1 Cor 2"),
        (["Gd", "Ap 1"], "Gd; Ap 1"),
        (["1 Sam 3, 10-15", "1 Sam 3, 16-18"], "1 Sam 3, 10-18"),
        (["Mt 5, 3-33", "Mt 5, 37-40"], "Mt 5, 3-33.37-40"),
        (["Lc 5, 4-10", "Lc 6, 10"], "Lc 5, 4-10; 6, 10"),
        (["Mt 5, 9-10", "Gv 5, 3-8"], "Mt 5, 9-10; Gv 5, 3-8"),
        (["Mt 10, 10a-12", "Mt 10, 11-20"], "Mt 10, 10a-20"),
        (["Mt 1, 3-18a", "Mt 1, 18b-24"], "Mt 1, 3-24"),
        (["Mt 10, 13a", "Mt 10, 13b-20"], "Mt 10, 13-20"),
    ]

    for citations, expected in examples:
        result = merge_bible_citations(citations)
        if result != expected:
            print(f"{citations} => {result}   expected: {expected}")
