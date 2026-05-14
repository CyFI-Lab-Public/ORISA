import os
import re
from collections import Counter
from difflib import SequenceMatcher

def load_prompt_text(prompt_file):
    """Load the original prompt and response from a text file."""
    with open(prompt_file, 'r', encoding='utf-8') as f:
        return f.read().strip()

def preprocess_text(text):
    """Preprocess text by removing special characters and converting to lowercase."""
    return re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()

def get_phrase_frequencies(text, n=3):
    """Extract word n-grams from text to capture phrases."""
    words = text.split()
    phrases = [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    return Counter(phrases)

def process_large_dump_file(dump_file, prompt_phrases):
    """Efficiently process a large memory dump file and find matching phrases."""
    found_phrases = Counter()
    total_phrases = sum(prompt_phrases.values())

    with open(dump_file, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = preprocess_text(line)
            for phrase in prompt_phrases:
                if phrase in line:
                    found_phrases[phrase] += 1

    # Cap found counts to avoid inflation
    recovered_count = sum(min(found_phrases[p], prompt_phrases[p]) for p in found_phrases)
    recovery_percentage = (recovered_count / total_phrases) * 100

    return recovery_percentage, found_phrases

# Example usage
prompt_file = "foreground_dumps/prompts.txt"  # Original prompt file
dump_file = "cleaned_prompt_dumps/foreground_dump1hr_only.txt"  # Large memory dump file

# Load and preprocess prompt text
prompt_text = load_prompt_text(prompt_file)
prompt_text = preprocess_text(prompt_text)
prompt_phrases = get_phrase_frequencies(prompt_text)

# Process memory dump
recovery_percentage, found_phrases = process_large_dump_file(dump_file, prompt_phrases)

print(f"Recovered Percentage: {recovery_percentage:.2f}%")
print("Top Recovered Phrases:", found_phrases.most_common(20))

