important_keywords = [
    "value", "summary", "trick",       # English
    "fayda", "samjhata", "tarika",     # Hinglish
    "फायदा", "सारांश", "तरीका"          # Hindi (Devnagari)
]

viral_hooks_found = []

# Using try-except ensures the script alerts you gracefully if transcript.txt doesn't exist
try:
    with open("transcript.txt", "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            
            # 1. Skip empty lines entirely
            if not clean_line:
                continue
                
            # 2. Check keywords against a lowercase version of the line
            lower_line = clean_line.lower()
            
            for keyword in important_keywords:
                if keyword in lower_line:
                    # 3. Prevent structural crashes if ' - ' is missing
                    if " - " in clean_line:
                        parts = clean_line.split(" - ", 1) # Split only at the first occurrence
                        hook_text = parts[1].strip()
                        viral_hooks_found.append(hook_text)
                        break  # 4. Prevents writing the same line twice if it has multiple keywords
                        
except FileNotFoundError:
    print("\n[ERROR]: 'transcript.txt' file not found! Please create it in this folder.")
    input("\nPress Enter to exit...")
    exit()

# Export clean matches to the text file
with open("export_hooks.txt", "w", encoding="utf-8") as export_file:
    for hook in viral_hooks_found:
        export_file.write(hook + "\n")

print("\n🔥 System Success: 'export_hooks.txt' updated cleanly from raw data!")
input("\nPress Enter to close this window...")
