important_keywords = [
    "value", "summary", "trick",       # English
    "fayda", "samjhata", "tarika",     # Hinglish
    "फायदा", "सारांश", "तरीका"          # Hindi (Devnagari)
]

viral_hooks_found = []

with open("transcript.txt", "r", encoding="utf-8") as file:
    for line in file:
        # Check every keyword against the current text line
        for keyword in important_keywords:
            if keyword in line:
                parts = line.split(" - ")
                clean_text = parts[1].strip()
                viral_hooks_found.append(clean_text)

# Outside the loops, export the matches to a new file
with open("export_hooks.txt", "w",encoding="utf-8") as export_file:
    for hook in viral_hooks_found:
        export_file.write(hook + "\n")

print("\n System Success: 'export_hooks.txt' updated from raw file data!")
input("\nPress Enter to close this window...")

