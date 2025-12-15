#!/usr/bin/env python3
"""
Update Knowledge Base Files
Aktualisiert knowledge_base_full.json und knowledge_base_chunks.json
mit der vollständigen deutschen Wissensdatenbank
"""

import json
from datetime import datetime

# Vollständige strukturierte Wissensdatenbank
knowledge_base_data = {
    "metadata": {
        "title": "Hausarztpraxis Orchideenkamp - Vollständige Wissensdatenbank",
        "version": "1.0",
        "last_updated": datetime.now().isoformat(),
        "language": "de",
        "practice_name": "Hausarztpraxis Orchideenkamp",
        "doctor": "Dr. med. Carsten Schmidt"
    },
    
    "practice_info": {
        "name": "Hausarztpraxis Orchideenkamp",
        "address": {
            "street": "Neuer Bahnweg 11",
            "zip": "26655",
            "city": "Westerstede",
            "country": "Deutschland"
        },
        "contact": {
            "phone": "(04488) 528140",
            "fax": "(04488) 5281429",
            "email": "info@hausarztpraxis-orchideenkamp.de"
        },
        "hours": {
            "monday_friday_morning": "8:00 - 13:00",
            "monday_friday_afternoon": "15:00 - 18:30",
            "saturday": "9:00 - 12:00",
            "telemedicine": "Dienstag 16:30 - 18:30"
        },
        "emergency": {
            "life_threatening": "112",
            "medical_emergency": "116 117",
            "poison_control": "0551 19240"
        },
        "statistics": {
            "years_experience": "15+",
            "patients": "5000+",
            "service_areas": "10+",
            "commitment": "100%"
        },
        "motto": "Ihre Gesundheit liegt uns am Herzen"
    },
    
    "doctor": {
        "name": "Dr. med. Carsten Schmidt",
        "title": "Facharzt für Allgemeinmedizin",
        "qualifications": [
            "Facharzt für Allgemeinmedizin (seit 2009)",
            "Diplom-Biologe",
            "Dr. med. (Promotion: Magna cum laude)"
        ],
        "education": [
            "Biologiestudium: TU Braunschweig, Universität Oldenburg",
            "Diplom-Biologe (1992-1995): Note Sehr gut",
            "Studium Humanmedizin: Universität Göttingen",
            "Promotion: Dr. med. Magna cum laude"
        ],
        "additional_qualifications": [
            "Notfallmedizin",
            "Ernährungsmedizin",
            "Verkehrsmedizin"
        ],
        "experience": "Eigene Praxis in Westerstede seit April 2009",
        "approach": [
            "Evidenzbasierte Medizin",
            "Persönliche Zuwendung und Zeit für Patienten",
            "Kombination aus modernster Technik und persönlicher Betreuung",
            "Wissenschaftliche Expertise durch biologischen Hintergrund",
            "Langfristige Patientenbeziehungen"
        ]
    },
    
    "team": [
        {
            "name": "Dr. med. Carsten Schmidt",
            "role": "Praxisinhaber",
            "specializations": ["Allgemeinmedizin", "Notfallmedizin", "Ernährungsmedizin", "Verkehrsmedizin"]
        },
        {
            "name": "Sandra Müller",
            "role": "Medizinische Fachangestellte",
            "specializations": ["Terminverwaltung & Empfang", "Patientenbetreuung", "Blutentnahmen", "EKG & Lungenfunktion"]
        },
        {
            "name": "Julia Weber",
            "role": "Medizinische Fachangestellte",
            "specializations": ["Behandlungsassistenz", "Wundversorgung", "Impfungen", "Labor & Diagnostik"]
        },
        {
            "name": "Anna Schneider",
            "role": "Medizinische Fachangestellte",
            "specializations": ["Vorsorgeuntersuchungen", "Gesundheitsberatung", "DMP-Programme", "Patientenschulungen"]
        },
        {
            "name": "Petra Hoffmann",
            "role": "Praxismanagerin",
            "specializations": ["Praxisorganisation", "Abrechnungswesen", "Qualitätsmanagement", "Personalkoordination"]
        },
        {
            "name": "Lena Fischer",
            "role": "Auszubildende zur MFA (2. Lehrjahr)",
            "specializations": ["Empfang & Terminvergabe", "Patientenbetreuung", "Assistenz im Behandlungsraum", "Verwaltungsaufgaben"]
        },
        {
            "name": "Maria Rossi",
            "role": "Hygienebeauftragte & Reinigung",
            "specializations": ["Praxishygiene", "Desinfektion & Sterilisation", "Hygienestandards", "Materialverwaltung"]
        }
    ],
    
    "services": {
        "hausaerztliche_versorgung": {
            "name": "Hausärztliche Versorgung",
            "description": "Erste Anlaufstelle für alle gesundheitlichen Fragen",
            "includes": [
                "Diagnostik, Behandlung und Prävention akuter und chronischer Erkrankungen",
                "Koordination mit Fachärzten und Kliniken",
                "Umfassende Kenntnis Ihrer Krankengeschichte",
                "Hausbesuche bei Bedarf"
            ],
            "specific_services": [
                "Akutversorgung bei Erkältungen, Infektionen, Verletzungen, Schmerzen",
                "Chronische Krankheiten (Diabetes, Bluthochdruck, Asthma, COPD)",
                "Psychosomatische Grundversorgung",
                "Notfallmanagement",
                "Wundversorgung und kleine chirurgische Eingriffe",
                "Geriatrische Betreuung älterer Patienten",
                "Palliativmedizinische Betreuung",
                "DMP-Programme"
            ]
        },
        "diagnostik": {
            "name": "Diagnostik",
            "description": "Moderne apparative Diagnostik direkt in unserer Praxis",
            "services": {
                "EKG": {
                    "types": ["Ruhe-EKG", "Belastungs-EKG auf Fahrrad-Ergometer"],
                    "detects": "Herzrhythmusstörungen, Durchblutungsstörungen des Herzens (Koronare Herzkrankheit)"
                },
                "Sonographie": {
                    "areas": ["Bauchorgane", "Schilddrüse", "Lymphknoten", "Gefäße", "Weichteile und Gelenke"]
                },
                "Langzeit_Blutdruck": {
                    "description": "24-Stunden-Blutdruckmessung",
                    "purpose": "Diagnose und Therapiekontrolle von Bluthochdruck"
                },
                "Lungenfunktion": {
                    "type": "Spirometrie",
                    "for": "Asthma, COPD-Diagnose"
                },
                "weitere": ["Langzeit-EKG", "Blutzuckermessung", "Schnelltests (CRP, Troponin, D-Dimer)", "Urinuntersuchungen", "Wundabstriche"]
            }
        },
        "labor": {
            "name": "Laboruntersuchungen",
            "description": "Moderne Labordiagnostik mit schnellen Ergebnissen",
            "routine": [
                "Großes und kleines Blutbild",
                "Blutzucker und HbA1c",
                "Cholesterin und Blutfettwerte",
                "Leber- und Nierenwerte",
                "Schilddrüsenwerte (TSH, fT3, fT4)",
                "Vitamine und Mineralstoffe",
                "Entzündungsparameter (CRP, BSG)"
            ],
            "special": [
                "Hormonuntersuchungen",
                "Tumormarker",
                "Allergietests",
                "Covid-19 PCR- und Antigen-Tests"
            ],
            "turnaround_time": "1-3 Tage"
        },
        "vorsorge": {
            "name": "Vorsorgeuntersuchungen",
            "description": "Früherkennung ist der beste Schutz",
            "programs": {
                "check_up_35": {
                    "name": "Check-up 35",
                    "frequency": "Ab 35 Jahren alle 3 Jahre",
                    "covered_by": "Gesetzliche Krankenversicherung",
                    "includes": ["Anamnese", "Körperliche Untersuchung", "Blutdruckmessung", "Bluttests", "Urintest"]
                },
                "hautkrebs_screening": {
                    "name": "Hautkrebs-Screening",
                    "frequency": "Ab 35 Jahren alle 2 Jahre",
                    "type": "Ganzkörperuntersuchung der Haut"
                },
                "krebs_frueherkennung": [
                    "Darmkrebsvorsorge",
                    "Prostatakrebsvorsorge (Männer ab 45)",
                    "Brustkrebsvorsorge",
                    "Gebärmutterhalskrebsvorsorge"
                ]
            }
        },
        "impfungen": {
            "name": "Impfungen & Impfberatung",
            "description": "Umfassender Impfschutz für alle Altersgruppen",
            "standard": [
                "Tetanus", "Diphtherie", "Pertussis", "Poliomyelitis",
                "Masern, Mumps, Röteln (MMR)", "Meningokokken-Meningitis",
                "Hepatitis A und B", "Pneumokokken", "FSME",
                "Herpes Zoster", "HPV"
            ],
            "saisonal": [
                "Influenza (jährlich)",
                "Covid-19 (mRNA-Impfstoffe)"
            ],
            "reise": [
                "Gelbfieber", "Typhus", "Tollwut", "Japanische Enzephalitis",
                "Dengue-Fieber", "Cholera", "Meningokokken ACWY"
            ]
        },
        "reisemedizin": {
            "name": "Reisemedizin",
            "description": "Gesund auf Reisen",
            "booking_time": "3-4 Monate vor Abreise",
            "services": [
                "Umfassende reisemedizinische Beratung",
                "Länderspezifische Gesundheitsrisiko-Information",
                "Impfempfehlungen",
                "Malariaprophylaxe",
                "Reiseapotheken-Zusammenstellung"
            ],
            "cost": "Private Abrechnung (teilweise Erstattung durch Krankenkassen)"
        },
        "atteste": {
            "name": "Atteste & Bescheinigungen",
            "description": "Medizinische Bescheinigungen für Sport, Beruf und Behörden",
            "types": [
                "Arbeitsunfähigkeitsbescheinigung",
                "Schulatteste und Sportbefreiungen",
                "Gesundheitszeugnisse für Führerschein",
                "Flugtauglichkeitsbescheinigungen",
                "Sporttauglichkeitsatteste",
                "Tauchuntersuchungen",
                "Bescheinigungen für Versicherungen",
                "Atteste für Behörden",
                "Pflegegradanträge",
                "Reha-Bescheinigungen"
            ],
            "cost": "Private Abrechnung nach GOÄ"
        },
        "telemedizin": {
            "name": "Telemedizin",
            "description": "Moderne Medizin von zu Hause",
            "video_consultation": {
                "schedule": "Dienstags 16:30-18:30",
                "suitable_for": [
                    "Folgetermine",
                    "Befundbesprechungen",
                    "Therapiekontrollen",
                    "Rezeptanfragen",
                    "Krankschreibungen bei bekannten Erkrankungen",
                    "Psychosomatische Gespräche"
                ],
                "requirements": "Gerät mit Kamera und Internet"
            },
            "e_rezept": {
                "available": True,
                "benefits": ["Kein Verlust", "Direkte Übermittlung", "App-verfügbar"]
            },
            "limitations": [
                "Keine Erstvorstellung neuer Patienten",
                "Keine akuten Notfälle",
                "Keine körperlichen Untersuchungen",
                "Keine Diagnostik (EKG, Ultraschall)",
                "Keine Impfungen und Blutentnahmen"
            ]
        },
        "ernaehrungsberatung": {
            "name": "Ernährungsberatung",
            "description": "Gesunde Ernährung für mehr Lebensqualität",
            "areas": [
                "Gewichtsmanagement",
                "Ernährung bei chronischen Erkrankungen",
                "Nahrungsmittelunverträglichkeiten & Allergien",
                "Gesunde Ernährung im Alltag"
            ],
            "diseases": [
                "Diabetes mellitus",
                "Bluthochdruck",
                "Fettstoffwechselstörungen",
                "Gicht",
                "Nierenerkrankungen",
                "Magen-Darm-Erkrankungen",
                "Osteoporose"
            ],
            "cost": "Bei ernährungsbedingten Erkrankungen teilweise Kassenleistung"
        },
        "spezialsprechstunden": {
            "name": "Spezialsprechstunden",
            "description": "Spezialisierte Betreuung für besondere Bedürfnisse",
            "types": {
                "diabetes": {
                    "services": [
                        "Blutzuckeroptimierung",
                        "Diabetes-Schulung",
                        "Ernährungsberatung",
                        "Folgeerkrankungen-Kontrolle",
                        "Medikamentenanpassung",
                        "DMP-Teilnahme",
                        "Fußuntersuchungen"
                    ]
                },
                "psychosomatik": {
                    "treats": [
                        "Stressbedingte Beschwerden",
                        "Chronische Schmerzen ohne organische Ursache",
                        "Burnout",
                        "Schlafstörungen",
                        "Angststörungen",
                        "Depressive Verstimmungen",
                        "Psychosomatische Beschwerden"
                    ]
                },
                "geriatrie": {
                    "services": [
                        "Geriatrische Beurteilung",
                        "Medikamentenmanagement",
                        "Sturzprophylaxe",
                        "Demenzdiagnostik",
                        "Pflegegradanträge",
                        "Palliativmedizin"
                    ]
                },
                "dmp": {
                    "programs": [
                        "Diabetes mellitus Typ 1 & 2",
                        "Koronare Herzkrankheit (KHK)",
                        "Asthma bronchiale",
                        "COPD"
                    ]
                }
            }
        }
    },
    
    "faq": {
        "allgemein": [
            {
                "frage": "Brauche ich einen Termin?",
                "antwort": "Ja, Termine werden empfohlen. Für akute Notfälle versuchen wir, Sie während der Sprechzeiten unterzubringen."
            },
            {
                "frage": "Was soll ich zum ersten Termin mitbringen?",
                "antwort": "Versichertenkarte, frühere medizinische Unterlagen, aktuelle Medikamentenliste, Impfpass (falls vorhanden)."
            },
            {
                "frage": "Nehmen Sie neue Patienten an?",
                "antwort": "Ja, wir heißen neue Patienten willkommen. Bitte rufen Sie an, um einen Ersttermin zu vereinbaren."
            },
            {
                "frage": "Machen Sie Hausbesuche?",
                "antwort": "Ja, Hausbesuche sind für Patienten möglich, die aus gesundheitlichen Gründen nicht in die Praxis kommen können."
            }
        ],
        "versicherung": [
            {
                "frage": "Welche Versicherungen akzeptieren Sie?",
                "antwort": "Wir akzeptieren alle gesetzlichen Krankenversicherungen und private Krankenversicherungen."
            },
            {
                "frage": "Welche Leistungen sind privat zu bezahlen?",
                "antwort": "Reisemedizinische Beratungen, Reiseimpfungen, medizinische Atteste, individuelle Gesundheitsleistungen (IGeL), teilweise Ernährungsberatung."
            }
        ],
        "telemedizin": [
            {
                "frage": "Wie funktioniert die Videosprechstunde?",
                "antwort": "Termin für Dienstag 16:30-18:30 buchen, sicheren Video-Link erhalten, von Ihrem Gerät mit Kamera und Internet teilnehmen."
            },
            {
                "frage": "Ist die Videosprechstunde sicher?",
                "antwort": "Ja, alle Telemedizin-Dienste sind DSGVO-konform und verschlüsselt nach höchsten Sicherheitsstandards."
            }
        ],
        "notfall": [
            {
                "frage": "Was mache ich bei einem medizinischen Notfall außerhalb der Sprechzeiten?",
                "antwort": "Rufen Sie 116 117 für ärztlichen Bereitschaftsdienst oder 112 für lebensbedrohliche Notfälle."
            },
            {
                "frage": "Was ist ein medizinischer Notfall?",
                "antwort": "Brustschmerzen, schwere Atemnot, plötzliche starke Blutung, Bewusstlosigkeit, Schlaganfall-Symptome."
            }
        ]
    },
    
    "medical_articles": {
        "mikrobiom": {
            "title": "Kann unser Darm uns steuern?",
            "category": "Neurologie & Mikrobiom",
            "date": "2025-12-01",
            "study": "Suzuki, T.A., Tanja, AS., Waters, J.L. et al. (2025). Nature Communications 16, 9482",
            "key_findings": [
                "Verhalten kann über Mikrobiom weitergegeben werden",
                "Lactobacillus beeinflusst Aktivitätslevel",
                "Indolmilchsäure (ILA) aus Tryptophan-Abbau",
                "Mikrobiom als 'zweiter Erbgutstrang'",
                "Anpassung in wenigen Generationen statt Jahrtausenden"
            ],
            "implications": [
                "Psychische Erkrankungen durch Bakterien behandeln",
                "Mikrobiom-Implantate gegen Angst, Depression, ADHS",
                "Ernährung als Verhaltenstherapie"
            ]
        },
        "categories": {
            "kardiologie": [
                "Neue Erkenntnisse zur Prävention von Herz-Kreislauf-Erkrankungen",
                "Bluthochdruck: Neue Grenzwerte und Behandlungsstrategien"
            ],
            "diabetes": [
                "GLP-1-Agonisten zeigen Langzeitwirkung",
                "Kontinuierliche Glukosemessung bei Typ-2-Diabetes"
            ],
            "praevention": [
                "Vitamin D und Immunfunktion",
                "Mediterrane Ernährung: Langzeitstudie"
            ],
            "neurologie": [
                "Früherkennung von Alzheimer: Neue Biomarker",
                "Mikrobiom und Verhalten"
            ]
        },
        "quality": {
            "verstaendlich": "Komplexe medizinische Fachsprache in einfache Sprache übersetzt",
            "wissenschaftlich": "Peer-reviewed Studien aus renommierten Fachzeitschriften",
            "transparent": "Vollständige Quellenangaben und Links"
        }
    },
    
    "datenschutz": {
        "verantwortlicher": {
            "name": "Hausarztpraxis Orchideenkamp",
            "doctor": "Dr. med. Carsten Schmidt",
            "address": "Neuer Bahnweg 11, 26655 Westerstede",
            "phone": "(04488) 528140",
            "email": "info@hausarztpraxis-orchideenkamp.de"
        },
        "patient_rights": [
            "Auskunft über gespeicherte Daten",
            "Berichtigung oder Löschung der Daten",
            "Einschränkung der Verarbeitung",
            "Datenübertragbarkeit",
            "Widerruf der Einwilligung",
            "Beschwerde bei Aufsichtsbehörde"
        ],
        "aufsichtsbehoerde": {
            "name": "Die Landesbeauftragte für den Datenschutz Niedersachsen",
            "address": "Prinzenstraße 5, 30159 Hannover",
            "phone": "0511 120-4500",
            "email": "poststelle@lfd.niedersachsen.de"
        },
        "patientendaten": {
            "schutz": "Ärztliche Schweigepflicht gemäß § 203 StGB",
            "rechtsgrundlage": "Art. 9 Abs. 2 lit. h DSGVO in Verbindung mit § 22 BDSG",
            "aufbewahrung": "10 Jahre nach Behandlungsabschluss gemäß § 630f BGB"
        }
    },
    
    "chatbot_guidelines": {
        "tone": "Professionell aber freundlich, empathisch, patientenzentriert",
        "language": "Sie (formelle deutsche Anrede)",
        "priorities": [
            "Kontaktdaten und Sprechzeiten",
            "Terminbuchungsprozess",
            "Notfallverfahren",
            "Häufige Leistungen",
            "Versicherungs- und Kosteninformationen"
        ],
        "escalation_triggers": {
            "medical_emergency": "Weiterleitung zu 112 oder 116 117",
            "complex_medical": "Empfehlung zur Terminbuchung",
            "complaints": "Weiterleitung zur Praxismanagerin",
            "privacy": "Verweis auf Datenschutzerklärung"
        },
        "cannot_provide": [
            "Spezifische medizinische Diagnosen",
            "Rezeptempfehlungen ohne Konsultation",
            "Medizinische Beratung bei Notfällen",
            "Persönliche Gesundheitsinformationen ohne Verifizierung",
            "Rechts- oder Versicherungsberatung"
        ],
        "conversation_examples": [
            {
                "scenario": "Terminbuchung",
                "user": "Ich brauche einen Termin",
                "agent": "Gerne helfe ich Ihnen bei der Terminvereinbarung mit Dr. Schmidt. Sie können uns unter (04488) 528140 während unserer Sprechzeiten anrufen: Montag bis Freitag 8:00-13:00 und 15:00-18:30, oder Samstag 9:00-12:00. Geht es um ein bestimmtes Anliegen oder eine Routineuntersuchung?"
            },
            {
                "scenario": "Notfall",
                "user": "Ich habe starke Brustschmerzen",
                "agent": "Das klingt nach einem medizinischen Notfall. Bitte rufen Sie sofort 112 an oder gehen Sie zur nächsten Notaufnahme. Warten Sie nicht."
            },
            {
                "scenario": "Impfung",
                "user": "Führen Sie Impfungen durch?",
                "agent": "Ja, wir bieten alle von der STIKO empfohlenen Standardimpfungen an, einschließlich saisonaler Impfungen wie Grippe und COVID-19, sowie Reiseimpfungen. Möchten Sie einen Impftermin vereinbaren?"
            }
        ]
    }
}

def create_full_knowledge_base():
    """Erstellt knowledge_base_full.json"""
    output_path = "knowledge_base/knowledge_base_full.json"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(knowledge_base_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Erstellt: {output_path}")
    print(f"   Größe: {len(json.dumps(knowledge_base_data))} Bytes")

def create_chunked_knowledge_base():
    """Erstellt knowledge_base_chunks.json mit kleineren, thematischen Chunks"""
    chunks = []
    
    # Chunk 1: Praxisinformationen
    chunks.append({
        "id": "practice_info",
        "title": "Praxisinformationen",
        "category": "general",
        "content": knowledge_base_data["practice_info"],
        "keywords": ["praxis", "adresse", "kontakt", "öffnungszeiten", "notfall", "westerstede"]
    })
    
    # Chunk 2: Arztinformationen
    chunks.append({
        "id": "doctor_info",
        "title": "Dr. med. Carsten Schmidt",
        "category": "team",
        "content": knowledge_base_data["doctor"],
        "keywords": ["arzt", "qualifikation", "facharzt", "biologe", "ausbildung"]
    })
    
    # Chunk 3: Team
    chunks.append({
        "id": "team",
        "title": "Unser Team",
        "category": "team",
        "content": knowledge_base_data["team"],
        "keywords": ["team", "mitarbeiter", "mfa", "praxismanagerin", "auszubildende"]
    })
    
    # Chunks 4-13: Leistungen (einzeln)
    service_counter = 4
    for service_key, service_data in knowledge_base_data["services"].items():
        chunks.append({
            "id": f"service_{service_key}",
            "title": service_data["name"],
            "category": "services",
            "content": service_data,
            "keywords": [service_key, service_data["name"].lower(), "leistung", "behandlung"]
        })
        service_counter += 1
    
    # Chunk: FAQ
    chunks.append({
        "id": "faq",
        "title": "Häufig gestellte Fragen",
        "category": "faq",
        "content": knowledge_base_data["faq"],
        "keywords": ["faq", "fragen", "antworten", "hilfe"]
    })
    
    # Chunk: Medizinische Artikel
    chunks.append({
        "id": "medical_articles",
        "title": "Medizinische Fachartikel",
        "category": "articles",
        "content": knowledge_base_data["medical_articles"],
        "keywords": ["forschung", "studien", "artikel", "mikrobiom", "wissenschaft"]
    })
    
    # Chunk: Datenschutz
    chunks.append({
        "id": "datenschutz",
        "title": "Datenschutz",
        "category": "legal",
        "content": knowledge_base_data["datenschutz"],
        "keywords": ["datenschutz", "dsgvo", "rechte", "privatsphäre"]
    })
    
    # Chunk: Chatbot Guidelines
    chunks.append({
        "id": "chatbot_guidelines",
        "title": "Chatbot Richtlinien",
        "category": "internal",
        "content": knowledge_base_data["chatbot_guidelines"],
        "keywords": ["chatbot", "voice agent", "richtlinien", "antworten"]
    })
    
    output_path = "knowledge_base/knowledge_base_chunks.json"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Erstellt: {output_path}")
    print(f"   Anzahl Chunks: {len(chunks)}")
    print(f"   Größe: {len(json.dumps(chunks))} Bytes")

def create_summary():
    """Erstellt knowledge_base_summary.json"""
    summary = {
        "metadata": knowledge_base_data["metadata"],
        "quick_info": {
            "practice_name": "Hausarztpraxis Orchideenkamp",
            "doctor": "Dr. med. Carsten Schmidt",
            "phone": "(04488) 528140",
            "address": "Neuer Bahnweg 11, 26655 Westerstede",
            "emergency": {
                "life_threatening": "112",
                "medical": "116 117"
            },
            "hours": {
                "weekdays": "Mo-Fr: 8:00-13:00 & 15:00-18:30",
                "saturday": "Sa: 9:00-12:00",
                "telemedicine": "Di: 16:30-18:30"
            }
        },
        "services_overview": [service["name"] for service in knowledge_base_data["services"].values()],
        "team_count": len(knowledge_base_data["team"]),
        "statistics": knowledge_base_data["practice_info"]["statistics"]
    }
    
    output_path = "knowledge_base/knowledge_base_summary.json"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Erstellt: {output_path}")

if __name__ == "__main__":
    print("🚀 Aktualisiere Knowledge Base Dateien...\n")
    
    create_full_knowledge_base()
    print()
    create_chunked_knowledge_base()
    print()
    create_summary()
    
    print("\n✅ Alle Knowledge Base Dateien wurden erfolgreich aktualisiert!")
    print("\nDateien:")
    print("  - knowledge_base/knowledge_base_full.json")
    print("  - knowledge_base/knowledge_base_chunks.json")
    print("  - knowledge_base/knowledge_base_summary.json")
