from js import document
import random

pirate_dict = {
    "hello": ["ahoy", "avast"],
    "hi": ["yo-ho-ho", "ahoy"],
    "my": ["me"],
    "friend": ["matey", "bucko"],
    "sir": ["cap'n", "ye ol' captain"],
    "madam": ["proud beauty", "fair maiden"],
    "stranger": ["scurvy dog", "landlubber"],
    "officer": ["foul blaggart"],
    "where": ["whar"],
    "is": ["be"],
    "the": ["th'"],
    "you": ["ye"],
    "your": ["yer"],
    "you're": ["ye be"],
    "we're": ["we be"],
    "are": ["be"],
    "wow": ["blimey", "yo ho ho"],
}


def translate_to_pirate(text):
    words = text.lower().split()
    translated = []
    for word in words:
        if word in pirate_dict:
            translated.append(random.choice(pirate_dict[word]))
        else:
            translated.append(word)
    return " ".join(translated).capitalize()


def translate_english(event):
    input_text = document.getElementById("english").value
    translated = translate_to_pirate(input_text)
    document.getElementById("output").innerText = translated


# Make the translate_english function available to the HTML
globals()['translate_english'] = translate_english
