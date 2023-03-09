from SheetExtractor import extract_sheet

file_names = ["marimba", "piano", "string", "woodwind", "synth"]

for file_name in file_names:
    extract_sheet(file_name, 2, 4, 8)
