# Knowledge Base - Hausarztpraxis Orchideenkamp

## 📚 Übersicht

Diese Knowledge Base enthält alle strukturierten Informationen über die Hausarztpraxis Orchideenkamp von Dr. med. Carsten Schmidt in **drei verschiedenen Formaten** für optimale Nutzung durch Voice Agents und Chatbots.

**Letzte Aktualisierung:** 13. Dezember 2025  
**Version:** 1.0  
**Sprache:** Deutsch

---

## 📁 Dateien

### 1. `knowledge_base_full.json` (18 KB)
**Vollständige strukturierte Wissensdatenbank**

Enthält alle Praxisinformationen in einem einzigen JSON-Dokument:
- ✅ Praxisinformationen (Adresse, Kontakt, Öffnungszeiten, Notfallnummern)
- ✅ Arztinformationen (Qualifikationen, Ausbildung, Ansatz)
- ✅ Team (7 Mitarbeiter mit Spezialisierungen)
- ✅ 10 Leistungsbereiche (detailliert beschrieben)
- ✅ FAQ (4 Kategorien: Allgemein, Versicherung, Telemedizin, Notfall)
- ✅ Medizinische Fachartikel (inkl. Mikrobiom-Forschung)
- ✅ Datenschutzinformationen
- ✅ Chatbot-Richtlinien mit Gesprächsbeispielen

**Verwendung:**
```python
import json

with open('knowledge_base_full.json', 'r', encoding='utf-8') as f:
    kb = json.load(f)

# Beispiel: Praxistelefon abrufen
phone = kb['practice_info']['contact']['phone']
print(phone)  # (04488) 528140
```

---

### 2. `knowledge_base_chunks.json` (22 KB)
**Thematisch aufgeteilte Chunks für effizientes Retrieval**

17 thematische Chunks mit Kategorisierung und Keywords:
- 📌 Chunk 1: Praxisinformationen
- 📌 Chunk 2: Arztinformationen
- 📌 Chunk 3: Team
- 📌 Chunks 4-13: Einzelne Leistungsbereiche
- 📌 Chunk 14: FAQ
- 📌 Chunk 15: Medizinische Artikel
- 📌 Chunk 16: Datenschutz
- 📌 Chunk 17: Chatbot-Richtlinien

**Chunk-Struktur:**
```json
{
  "id": "practice_info",
  "title": "Praxisinformationen",
  "category": "general",
  "content": { ... },
  "keywords": ["praxis", "adresse", "kontakt", "öffnungszeiten", "notfall"]
}
```

**Verwendung:**
```python
import json

with open('knowledge_base_chunks.json', 'r', encoding='utf-8') as f:
    chunks = json.load(f)

# Beispiel: Finde Chunk zu "Impfungen"
impfungen_chunk = next((c for c in chunks if 'impfungen' in c['id']), None)
print(impfungen_chunk['title'])  # Impfungen & Impfberatung
```

**Ideal für:**
- Vector-Datenbanken (z.B. Pinecone, Weaviate, Chroma)
- RAG (Retrieval-Augmented Generation)
- Semantische Suche
- Chunked Embeddings

---

### 3. `knowledge_base_summary.json` (1.1 KB)
**Kompakte Zusammenfassung für schnellen Zugriff**

Enthält die wichtigsten Informationen:
- 🔹 Praxisname und Arzt
- 🔹 Kontaktdaten (Telefon, Adresse)
- 🔹 Notfallnummern
- 🔹 Öffnungszeiten
- 🔹 Übersicht aller 10 Leistungen
- 🔹 Teamgröße (7 Mitarbeiter)
- 🔹 Statistiken (15+ Jahre, 5000+ Patienten)

**Verwendung:**
```python
import json

with open('knowledge_base_summary.json', 'r', encoding='utf-8') as f:
    summary = json.load(f)

# Beispiel: Schnellzugriff auf Notfallnummer
emergency = summary['quick_info']['emergency']['life_threatening']
print(emergency)  # 112
```

**Ideal für:**
- Initial Context für Chatbots
- Quick Reference
- API Response Caching
- Mobile Apps mit begrenzter Bandbreite

---

## 🎯 Verwendungszwecke

### 1. Voice Agent / Chatbot Training
```python
# Lade vollständige Knowledge Base
with open('knowledge_base_full.json', 'r') as f:
    kb = json.load(f)

# Verwende Chatbot Guidelines
guidelines = kb['chatbot_guidelines']
tone = guidelines['tone']  # "Professionell aber freundlich..."
examples = guidelines['conversation_examples']
```

### 2. RAG (Retrieval-Augmented Generation)
```python
# Lade Chunks für Embedding
with open('knowledge_base_chunks.json', 'r') as f:
    chunks = json.load(f)

# Erstelle Embeddings für jeden Chunk
for chunk in chunks:
    text = f"{chunk['title']}: {json.dumps(chunk['content'])}"
    embedding = create_embedding(text)
    store_in_vector_db(chunk['id'], embedding, chunk)
```

### 3. FAQ-System
```python
# Lade FAQ
with open('knowledge_base_full.json', 'r') as f:
    kb = json.load(f)

faq = kb['faq']
# Kategorien: allgemein, versicherung, telemedizin, notfall
```

### 4. Appointment Booking Bot
```python
# Schneller Zugriff auf Kontakt & Öffnungszeiten
with open('knowledge_base_summary.json', 'r') as f:
    summary = json.load(f)

phone = summary['quick_info']['phone']
hours = summary['quick_info']['hours']
```

---

## 📊 Statistiken

| Metrik | Wert |
|--------|------|
| **Leistungsbereiche** | 10 |
| **Teammitglieder** | 7 |
| **FAQ-Kategorien** | 4 |
| **FAQ-Einträge** | 8+ |
| **Gesprächsbeispiele** | 3 |
| **Chunks** | 17 |
| **Gesamtgröße** | ~41 KB |

---

## 🔄 Aktualisierung

Die Knowledge Base kann mit dem bereitgestellten Python-Skript aktualisiert werden:

```bash
cd /Users/youssef/Desktop/hausarztpraxis-orchideenkamp
python3 update_knowledge_base.py
```

Das Skript generiert automatisch alle drei JSON-Dateien aus der strukturierten Datenbasis.

---

## 📝 Datenstruktur

### Hauptbereiche in `knowledge_base_full.json`:

```
{
  "metadata": { ... },
  "practice_info": { 
    "name", "address", "contact", "hours", "emergency", "statistics", "motto"
  },
  "doctor": {
    "name", "title", "qualifications", "education", "additional_qualifications", 
    "experience", "approach"
  },
  "team": [ ... 7 Mitarbeiter ... ],
  "services": {
    "hausaerztliche_versorgung": { ... },
    "diagnostik": { ... },
    "labor": { ... },
    "vorsorge": { ... },
    "impfungen": { ... },
    "reisemedizin": { ... },
    "atteste": { ... },
    "telemedizin": { ... },
    "ernaehrungsberatung": { ... },
    "spezialsprechstunden": { ... }
  },
  "faq": {
    "allgemein": [ ... ],
    "versicherung": [ ... ],
    "telemedizin": [ ... ],
    "notfall": [ ... ]
  },
  "medical_articles": { ... },
  "datenschutz": { ... },
  "chatbot_guidelines": { ... }
}
```

---

## 🚀 Integration Beispiele

### LangChain Integration
```python
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import json

# Lade Chunks
with open('knowledge_base_chunks.json', 'r') as f:
    chunks = json.load(f)

# Erstelle Dokumente
documents = [
    {"text": json.dumps(c['content']), "metadata": c}
    for c in chunks
]

# Erstelle Vector Store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(documents, embeddings)

# Query
results = vectorstore.similarity_search("Wie sind die Öffnungszeiten?")
```

### OpenAI Function Calling
```python
import json

with open('knowledge_base_full.json', 'r') as f:
    kb = json.load(f)

functions = [
    {
        "name": "get_practice_hours",
        "description": "Gibt die Öffnungszeiten der Praxis zurück",
        "parameters": {"type": "object", "properties": {}}
    }
]

def get_practice_hours():
    return kb['practice_info']['hours']
```

---

## 📞 Wichtige Kontaktdaten (Quick Reference)

| Info | Wert |
|------|------|
| **Praxis** | Hausarztpraxis Orchideenkamp |
| **Arzt** | Dr. med. Carsten Schmidt |
| **Telefon** | (04488) 528140 |
| **Fax** | (04488) 5281429 |
| **E-Mail** | info@hausarztpraxis-orchideenkamp.de |
| **Adresse** | Neuer Bahnweg 11, 26655 Westerstede |
| **Notfall (Leben)** | 112 |
| **Notfall (Medizin)** | 116 117 |
| **Gift-Notruf** | 0551 19240 |

---

## 🎨 Kategorien

Die Knowledge Base ist in folgende Hauptkategorien unterteilt:

- **general**: Allgemeine Praxisinformationen
- **team**: Team und Arztinformationen
- **services**: Medizinische Leistungen
- **faq**: Häufig gestellte Fragen
- **articles**: Medizinische Fachartikel
- **legal**: Datenschutz und rechtliche Informationen
- **internal**: Chatbot-Richtlinien und Guidelines

---

## ✅ Qualitätssicherung

- ✅ Alle Daten basieren auf offiziellen HTML-Seiten der Praxis
- ✅ Strukturiert und maschinenlesbar (JSON)
- ✅ UTF-8 Encoding für korrekte Umlaute
- ✅ Konsistente Datenstruktur
- ✅ Keywords für semantische Suche
- ✅ Chatbot-Richtlinien mit Gesprächsbeispielen
- ✅ Vollständige Kontakt- und Notfallinformationen

---

## 📄 Lizenz & Verwendung

Diese Knowledge Base ist für den internen Gebrauch der Hausarztpraxis Orchideenkamp bestimmt.

**Verwendungszweck:** Voice Agents, Chatbots, Informationssysteme

**Hinweis:** Alle medizinischen Informationen sind allgemeiner Natur. Bei konkreten Gesundheitsfragen kontaktieren Sie bitte die Praxis direkt.

---

**Erstellt:** Dezember 2025  
**Aktualisiert:** 13.12.2025  
**Autor:** Hausarztpraxis Orchideenkamp
