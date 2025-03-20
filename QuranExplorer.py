import xml.etree.ElementTree as ET
from typing import Dict, List
import re

class QuranExplorer:
    def __init__(self, arabic_file: str, english_file: str, translit_file: str):
        self.arabic_data = self._load_xml(arabic_file)
        self.english_data = self._load_xml(english_file)
        self.translit_data = self._load_xml(translit_file)
        self.max_chapters = max(len(self.arabic_data), len(self.english_data), len(self.translit_data))

    def _load_xml(self, filename: str) -> Dict[str, Dict]:
        """Load and parse XML file into a dictionary."""
        tree = ET.parse(filename)
        root = tree.getroot()
        quran_dict = {}
        
        for chapter in root.findall('Chapter'):
            chapter_id = chapter.get('ChapterID')
            chapter_name = chapter.get('ChapterName')
            verses = []
            
            for verse in chapter.findall('Verse'):
                verse_id = verse.get('VerseID')
                verse_text = verse.text.strip()
                verses.append({
                    'id': verse_id,
                    'text': verse_text
                })
            
            quran_dict[chapter_id] = {
                'name': chapter_name,
                'verses': verses
            }
            
        return quran_dict

    def _clean_transliteration(self, text: str) -> str:
        """Remove HTML-like tags from transliteration text."""
        # Remove tags like <u>, </u>, <b>, </b>, etc.
        cleaned = re.sub(r'<[^>]+>', '', text)
        return cleaned

    def display_verse(self, chapter_id: str, verse_id: str):
        """Display a specific verse in Arabic, Transliteration, and English."""
        arabic_chapter = self.arabic_data.get(chapter_id)
        english_chapter = self.english_data.get(chapter_id)
        translit_chapter = self.translit_data.get(chapter_id)
        
        if not (arabic_chapter and english_chapter and translit_chapter):
            print(f"Chapter {chapter_id} not found")
            return

        try:
            arabic_verse = next(v for v in arabic_chapter['verses'] if v['id'] == verse_id)
            english_verse = next(v for v in english_chapter['verses'] if v['id'] == verse_id)
            translit_verse = next(v for v in translit_chapter['verses'] if v['id'] == verse_id)
            
            print(f"\nSurah {chapter_id}: {arabic_chapter['name']} ({english_chapter['name']})")
            print(f"Verse {verse_id}:")
            print(f"Arabic: {arabic_verse['text']}")
            print(f"Transliteration: {self._clean_transliteration(translit_verse['text'])}")
            print(f"English: {english_verse['text']}")
            print("-" * 70)
        except StopIteration:
            print(f"Verse {verse_id} not found in Chapter {chapter_id}")

    def display_chapter(self, chapter_id: str):
        """Display all verses in a chapter with Arabic, Transliteration, and English."""
        arabic_chapter = self.arabic_data.get(chapter_id)
        english_chapter = self.english_data.get(chapter_id)
        translit_chapter = self.translit_data.get(chapter_id)
        
        if not (arabic_chapter and english_chapter and translit_chapter):
            print(f"Chapter {chapter_id} not found")
            return

        print(f"\nSurah {chapter_id}: {arabic_chapter['name']} ({english_chapter['name']})")
        print("=" * 70)
        
        for a_verse, t_verse, e_verse in zip(arabic_chapter['verses'], 
                                          translit_chapter['verses'],
                                          english_chapter['verses']):
            print(f"Verse {a_verse['id']}:")
            print(f"Arabic: {a_verse['text']}")
            print(f"Transliteration: {self._clean_transliteration(t_verse['text'])}")
            print(f"English: {e_verse['text']}")
            print("-" * 70)
            input("Press Enter to continue...")

    def search_text(self, search_term: str, language: str = "english"):
        """Search for text in the Quran (Arabic or English)."""
        results = []
        data_source = self.english_data if language.lower() == "english" else self.arabic_data
        
        for chapter_id, chapter in data_source.items():
            for verse in chapter['verses']:
                if search_term in verse['text']:
                    results.append((chapter_id, verse['id']))
        
        if not results:
            print(f"No results found for '{search_term}' in {language}")
            return
        
        print(f"\nFound {len(results)} results for '{search_term}' in {language}:")
        for chapter_id, verse_id in results:
            self.display_verse(chapter_id, verse_id)
            input("Press Enter for next result...")

    def main_menu(self):
        """Display interactive menu."""
        while True:
            print("\n=== Quran Explorer ===")
            print("1. View specific verse")
            print("2. View entire chapter")
            print("3. Search text in Arabic")
            print("4. Search text in English")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                chapter = input(f"Enter chapter number (1-{self.max_chapters}): ")
                if chapter in self.arabic_data:
                    max_verses = len(self.arabic_data[chapter]['verses'])
                    verse = input(f"Enter verse number (1-{max_verses}): ")
                    self.display_verse(chapter, verse)
                else:
                    print("Invalid chapter number")
            
            elif choice == "2":
                chapter = input(f"Enter chapter number (1-{self.max_chapters}): ")
                self.display_chapter(chapter)
            
            elif choice == "3":
                search_term = input("Enter search term (Arabic): ")
                self.search_text(search_term, "arabic")
            
            elif choice == "4":
                search_term = input("Enter search term (English): ")
                self.search_text(search_term, "english")
            
            elif choice == "5":
                print("Thank you for using Quran Explorer")
                break
            
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Replace these with your actual file paths
    arabic_file = "quran_arabic.xml"
    english_file = "quran_english.xml"
    translit_file = "quran_transliteration.xml"
    
    try:
        explorer = QuranExplorer(arabic_file, english_file, translit_file)
        explorer.main_menu()
    except FileNotFoundError as e:
        print(f"Error: Could not find file - {e}")
    except ET.ParseError as e:
        print(f"Error: Invalid XML format - {e}")
