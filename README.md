# Quran Explorer

A Python script to explore the Quran with Arabic text, English transliteration, and English translation. Features include viewing specific verses, entire chapters, and searching text in both Arabic and English.

## Features
- Display verses with Arabic, transliteration, and English translation
- View entire chapters with verse-by-verse display
- Search functionality in both Arabic and English
- Interactive command-line menu interface

## Prerequisites
- Python 3.6 or higher

## Installation

1. Clone the repository:
```git clone https://github.com/yourusername/InteractiveQuran.git```
```cd InteractiveQuran```

2. Install required Python packages (none beyond standard library):
   - The script uses only built-in modules (```xml.etree.ElementTree```, ```typing```, ```re```)

Note: The required XML database files (```quran_arabic.xml```, ```quran_english.xml```, ```quran_transliteration.xml```) are included in this repository.

## Usage

Run the script from the command line:

```python quran_explorer.py```

The main menu provides these options:
1. View specific verse by entering chapter and verse numbers
2. View entire chapter by chapter number
3. Search text in Arabic
4. Search text in English
5. Exit the program

### Example Commands
- To view Surah 1, Verse 1: Select option 1, enter ```1``` for chapter, ```1``` for verse
- To view all of Surah 2: Select option 2, enter ```2``` for chapter
- To search for "Allah" in English: Select option 4, enter ```Allah```

## File Structure
```InteractiveQuran/```
```├── quran_explorer.py    # Main Python script```
```├── quran_arabic.xml     # Arabic text database```
```├── quran_english.xml    # English translation database```
```├── quran_transliteration.xml  # Transliteration database```
```└── README.md           # This file```

## Data Sources and Credits
The Quran database files (```quran_arabic.xml```, ```quran_english.xml```, ```quran_transliteration.xml```) included in this repository are sourced from https://github.com/ceefour/qurandatabase, created by ceefour. These files are used under the terms of their original license [specify the license if known, e.g., Creative Commons, MIT, etc.]. Full credit and thanks to ceefour for providing these valuable XML resources.

## Troubleshooting
- If you get a "FileNotFoundError": Ensure all XML files are present in the repository directory
- If you get a "ParseError": Verify the XML files are valid and not corrupted
- Chapter numbers must be between ```1``` and ```114```
- Verse numbers must be valid for the selected chapter

## Contributing
Feel free to submit pull requests or open issues for bugs and feature requests.

## License
Licensed under the MIT License.
