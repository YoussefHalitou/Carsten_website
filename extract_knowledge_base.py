#!/usr/bin/env python3
"""
Knowledge Base Extraction Script für Hausarztpraxis Orchideenkamp
Extrahiert strukturierte Informationen aus HTML-Dateien für Chatbot & Voice Agent
"""

import json
import re
from pathlib import Path
from bs4 import BeautifulSoup
from typing import Dict, List, Optional

class HTMLKnowledgeExtractor:
    """Extrahiert und strukturiert Content aus HTML-Dateien"""
    
    def __init__(self, html_dir: Path):
        self.html_dir = Path(html_dir)
        self.knowledge_base = []
        
    def extract_metadata(self, soup: BeautifulSoup, file_path: Path) -> Dict:
        """Extrahiert Metadaten aus HTML"""
        title_tag = soup.find('title')
        title = title_tag.text.strip() if title_tag else file_path.stem
        
        # Meta Description
        meta_desc = soup.find('meta', {'name': 'description'})
        description = meta_desc.get('content', '') if meta_desc else ''
        
        return {
            'title': title,
            'description': description,
            'filename': file_path.name,
            'url_path': file_path.stem + '.html'
        }
    
    def clean_text(self, text: str) -> str:
        """Bereinigt Text für bessere Lesbarkeit"""
        # Multiple spaces und newlines reduzieren
        text = re.sub(r'\s+', ' ', text)
        # Führende/folgende Leerzeichen entfernen
        text = text.strip()
        return text
    
    def extract_sections(self, soup: BeautifulSoup) -> List[Dict]:
        """Extrahiert strukturierte Sections mit Headings"""
        sections = []
        
        # Finde alle Headings (h1-h4)
        for heading in soup.find_all(['h1', 'h2', 'h3', 'h4']):
            section = {
                'heading': self.clean_text(heading.get_text()),
                'level': heading.name,
                'content': []
            }
            
            # Sammle Content nach Heading bis zum nächsten Heading
            current = heading.find_next_sibling()
            while current and current.name not in ['h1', 'h2', 'h3', 'h4']:
                if current.name == 'p':
                    text = self.clean_text(current.get_text())
                    if text:
                        section['content'].append(text)
                elif current.name == 'ul' or current.name == 'ol':
                    # Liste extrahieren
                    items = [self.clean_text(li.get_text()) for li in current.find_all('li')]
                    if items:
                        section['content'].append({'list': items})
                elif current.name == 'div':
                    # Verschachtelte Divs durchsuchen
                    paragraphs = current.find_all('p', recursive=False)
                    for p in paragraphs:
                        text = self.clean_text(p.get_text())
                        if text:
                            section['content'].append(text)
                
                current = current.find_next_sibling()
            
            if section['content']:
                sections.append(section)
        
        return sections
    
    def extract_contact_info(self, soup: BeautifulSoup) -> Optional[Dict]:
        """Extrahiert Kontaktinformationen"""
        contact = {}
        
        # Telefon
        phone_patterns = [r'\(?\d{5}\)?\s*\d{5,6}', r'\d{4,5}\s*/\s*\d{4,7}']
        for pattern in phone_patterns:
            phone_match = re.search(pattern, soup.get_text())
            if phone_match:
                contact['phone'] = phone_match.group(0)
                break
        
        # Email
        email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', soup.get_text())
        if email_match:
            contact['email'] = email_match.group(0)
        
        # Adresse
        address_patterns = [
            r'Neuer Bahnweg\s+\d+',
            r'\d{5}\s+Westerstede'
        ]
        for pattern in address_patterns:
            addr_match = re.search(pattern, soup.get_text())
            if addr_match and 'address' not in contact:
                contact['address'] = addr_match.group(0)
        
        return contact if contact else None
    
    def extract_opening_hours(self, soup: BeautifulSoup) -> Optional[Dict]:
        """Extrahiert Öffnungszeiten/Sprechzeiten"""
        text = soup.get_text()
        hours = {}
        
        # Pattern für Sprechzeiten
        patterns = {
            'weekdays': r'Mo-Fr:\s*([\d:]+\s*-\s*[\d:]+\s*&?\s*[\d:]*\s*-?\s*[\d:]*)',
            'saturday': r'Sa:\s*([\d:]+\s*-\s*[\d:]+)',
            'telemedizin': r'Telemedizin\s+Di:\s*([\d:]+\s*-\s*[\d:]+)'
        }
        
        for key, pattern in patterns.items():
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                hours[key] = match.group(1).strip()
        
        return hours if hours else None
    
    def extract_services(self, soup: BeautifulSoup) -> List[str]:
        """Extrahiert angebotene Leistungen"""
        services = []
        
        # Suche nach Service-Karten
        service_cards = soup.find_all('div', class_='service-card')
        for card in service_cards:
            h3 = card.find('h3')
            if h3:
                services.append(self.clean_text(h3.get_text()))
        
        # Fallback: Links zu Leistungsseiten
        if not services:
            service_links = soup.find_all('a', href=True)
            service_keywords = ['versorgung', 'labor', 'impfung', 'diagnostik', 
                              'vorsorge', 'reise', 'attest', 'telemedizin', 
                              'ernaehrung', 'spezial']
            for link in service_links:
                href = link.get('href', '')
                if any(keyword in href.lower() for keyword in service_keywords):
                    text = self.clean_text(link.get_text())
                    if text and text not in services:
                        services.append(text)
        
        return services
    
    def extract_from_file(self, file_path: Path) -> Dict:
        """Extrahiert alle Informationen aus einer HTML-Datei"""
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Entferne Navigation, Footer, Scripts
        for element in soup(['nav', 'footer', 'script', 'style', 'header']):
            element.decompose()
        
        # Extrahiere Informationen
        metadata = self.extract_metadata(soup, file_path)
        sections = self.extract_sections(soup)
        contact = self.extract_contact_info(soup)
        hours = self.extract_opening_hours(soup)
        services = self.extract_services(soup)
        
        # Volltext für einfache Suche
        full_text = self.clean_text(soup.get_text())
        
        return {
            'metadata': metadata,
            'sections': sections,
            'contact': contact,
            'opening_hours': hours,
            'services': services,
            'full_text': full_text[:2000],  # Ersten 2000 Zeichen
            'content_length': len(full_text)
        }
    
    def process_all_files(self):
        """Verarbeitet alle HTML-Dateien"""
        html_files = sorted(self.html_dir.glob('*.html'))
        
        print(f"🔍 Gefundene HTML-Dateien: {len(html_files)}")
        
        for html_file in html_files:
            # Skip Backup-Dateien und spezielle Dateien
            if html_file.name.startswith('_'):
                continue
            
            try:
                print(f"  📄 Verarbeite: {html_file.name}")
                data = self.extract_from_file(html_file)
                self.knowledge_base.append(data)
            except Exception as e:
                print(f"  ❌ Fehler bei {html_file.name}: {str(e)}")
        
        print(f"\n✅ Erfolgreich verarbeitet: {len(self.knowledge_base)} Dateien")
    
    def save_json(self, output_file: Path):
        """Speichert Knowledge Base als JSON"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.knowledge_base, f, ensure_ascii=False, indent=2)
        print(f"💾 Gespeichert: {output_file}")
    
    def save_text_chunks(self, output_file: Path, chunk_size: int = 1000):
        """Speichert als Text-Chunks für Vector Database"""
        chunks = []
        
        for doc in self.knowledge_base:
            title = doc['metadata']['title']
            
            # Chunks aus Sections erstellen
            for section in doc['sections']:
                heading = section['heading']
                
                for content in section['content']:
                    if isinstance(content, dict) and 'list' in content:
                        # Listen als einzelne Chunks
                        text = f"{title} - {heading}\n\n" + "\n".join(content['list'])
                    else:
                        text = f"{title} - {heading}\n\n{content}"
                    
                    # Lange Texte aufteilen
                    if len(text) > chunk_size:
                        words = text.split()
                        current_chunk = []
                        current_length = 0
                        
                        for word in words:
                            current_length += len(word) + 1
                            if current_length > chunk_size:
                                chunks.append({
                                    'text': ' '.join(current_chunk),
                                    'source': doc['metadata']['filename'],
                                    'title': title,
                                    'section': heading
                                })
                                current_chunk = [word]
                                current_length = len(word)
                            else:
                                current_chunk.append(word)
                        
                        if current_chunk:
                            chunks.append({
                                'text': ' '.join(current_chunk),
                                'source': doc['metadata']['filename'],
                                'title': title,
                                'section': heading
                            })
                    else:
                        chunks.append({
                            'text': text,
                            'source': doc['metadata']['filename'],
                            'title': title,
                            'section': heading
                        })
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(chunks, f, ensure_ascii=False, indent=2)
        
        print(f"📦 {len(chunks)} Text-Chunks gespeichert: {output_file}")
    
    def create_summary(self) -> Dict:
        """Erstellt Zusammenfassung der Knowledge Base"""
        summary = {
            'total_documents': len(self.knowledge_base),
            'total_sections': sum(len(doc['sections']) for doc in self.knowledge_base),
            'total_content_length': sum(doc['content_length'] for doc in self.knowledge_base),
            'documents': []
        }
        
        for doc in self.knowledge_base:
            summary['documents'].append({
                'title': doc['metadata']['title'],
                'filename': doc['metadata']['filename'],
                'sections': len(doc['sections']),
                'services': doc['services'][:5] if doc['services'] else [],
                'has_contact': bool(doc['contact']),
                'has_hours': bool(doc['opening_hours'])
            })
        
        return summary


def main():
    """Hauptfunktion"""
    print("="*70)
    print("📚 Knowledge Base Extraction - Hausarztpraxis Orchideenkamp")
    print("="*70)
    print()
    
    # Verzeichnis mit HTML-Dateien
    html_dir = Path(__file__).parent
    
    # Extractor initialisieren
    extractor = HTMLKnowledgeExtractor(html_dir)
    
    # Alle Dateien verarbeiten
    extractor.process_all_files()
    
    # Outputs erstellen
    output_dir = html_dir / 'knowledge_base'
    output_dir.mkdir(exist_ok=True)
    
    print("\n" + "="*70)
    print("💾 Speichere Knowledge Base...")
    print("="*70)
    
    # 1. Vollständige strukturierte Daten (JSON)
    extractor.save_json(output_dir / 'knowledge_base_full.json')
    
    # 2. Text-Chunks für Vector Database
    extractor.save_text_chunks(output_dir / 'knowledge_base_chunks.json', chunk_size=800)
    
    # 3. Zusammenfassung
    summary = extractor.create_summary()
    with open(output_dir / 'knowledge_base_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"📊 Zusammenfassung gespeichert: knowledge_base_summary.json")
    
    # Statistiken ausgeben
    print("\n" + "="*70)
    print("📊 STATISTIKEN")
    print("="*70)
    print(f"  Dokumente:          {summary['total_documents']}")
    print(f"  Sections:           {summary['total_sections']}")
    print(f"  Gesamtlänge:        {summary['total_content_length']:,} Zeichen")
    print(f"  Output-Verzeichnis: {output_dir.absolute()}")
    print("="*70)
    
    print("\n✨ Fertig! Die Knowledge Base ist bereit für Ihren Chatbot/Voice Agent.")
    print("\n📝 Nächste Schritte:")
    print("  1. Verwenden Sie 'knowledge_base_chunks.json' für Vector Database (ChromaDB, Pinecone)")
    print("  2. Verwenden Sie 'knowledge_base_full.json' für strukturierte Queries")
    print("  3. Integrieren Sie mit LangChain oder Ihrem bevorzugten Framework")


if __name__ == '__main__':
    main()

