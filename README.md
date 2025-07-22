# Pertinax Security Tool

Modular Security Suite

© Pertinax Design, 2025, Sonja Müller

Also wie man erkennen kann noch keine richtig klare Struktur, abgesehen davon konnte ich keine Ordner hochladen, was mich auch nervt, weil es das Gesamtkuddelmuddel vervollständigt. Ich hoffe du kommst damit klar. Alle ist irgendwie chronologisch sortiert.  Ich hatte alle geschriebenen Dateien zusammengelegt und in einen Ordner gesteckt.
Irgendwie habe ich noch ein paar MOdule auf dem Rechner, aber ich muss die erst mal angucken, um zu entscheiden, ob ich sie nun noch hochladen muss oder nicht.



Pertinax Security Tool – Benutzerhandbuch
Hybridschutz
Modul zur kombinierten Erkennung von Keyloggern, Spyware und versteckten Hintergrundprozessen. Echtzeitabschirmung durch KI.
Feindortung
Erkennt potenzielle Angreifer in Echtzeit mittels GeoSniffer-Analyse und Standortabgleich.
Abgeschirmter Funkverkehr
Schützt WLAN- und Bluetooth-Schnittstellen vor unbefugtem Zugriff, inkl. Scan-Monitoring.
Schirm
Live-Monitor zeigt laufende Netzwerkverbindungen, Prozesse und Schutzstatus im Überblick.
Selbstreparaturmodul
Führt automatisch oder manuell Initiierte Selbsttests durch. Erkennt und repariert kritische Systemfehler.
Computeranalyse
Modul mit KI-gestützter Verhaltens- und Musteranalyse zur Erkennung von Abweichungen im Systemverhalten.
Bordsensoren
Integrierter Modulcheck für Firmware, Treiber, Hardware-Komponenten und deren Stabilität.
Statistik Monitor
Grafische Übersicht über erkannte Bedrohungen und Scans. Zeitlich einstellbar (Woche, Monat, Halbjahr).
Benutzerhandbuch
Zeigt alle Modulbeschreibungen direkt als PDF an. Zugriff über das Widget mit Buch-Symbol.


Gesamtsystem: KI-gestützte Firewall- und Cyber-Abwehrplattform „Project AEGIS“
Advanced Enhanced Guardian & Intelligence System

? Modulstruktur / Komponentenübersicht
1. ? Firewall-System
Paketfilter (IPTables/NFTables Wrapper)
Deep Packet Inspection
Geo-IP-Blocking
Port-Honeypot-Systeme (mit Logging)
Man-in-the-Middle-Erkennung
Mobilefirewall + Android/iOS-Schnittstelle
Bluetooth-Firewall + Low Energy Scanner

2. ? KI-Unterstützte Analyse + Abwehr
Threat Detection AI (scikit-learn / Tensorflow Lite)
Live-Traffic-Scoring
Phishing-Datenbank mit Online-Scanner (z. B. via PhishTank)
Scam-Erkennung via NLP
Cookie-Transfer-Analyse (DOM-Inspektor + Sniffer)
Webseiten- und JavaScript-Forensik
KI-Trainingsmodul für Benutzerfeedback

3. ? Forensik & Speicheranalyse
Live-Memory Dump Scanner (Volatility)
HDD/SSD/MicroSD/USB-Sektorprüfer
Stack Tracer
Keylogger-Detektor + Heuristic
Hardware-ID + Serial Logging
Secure Memory Snapshot-Export (mit Cloudsync)

4. ⚙️ Hardware- und Softwareprüfung
Hardware-Checker
CPU/GPU/TMP/Shader/Touch/Stack etc.
Bluetoothgeräte, Speicherchips, Sensoren
Temperatur, Spannung, Firmware
Fehlerdatenbankabgleich
KI-gestützte Reparaturvorschläge
Software-Checker
Signaturprüfung, Hashing
Lizenzprüfung
Debugging-Schutz (Anti-Flashbox)
Erkennung von BASH Squirrels & Rootkits

5. ? Reparaturmodul
Modul: DeviceRepairManager
Automatische Fehlerkorrektur via Heuristik
Überschreibfunktion mit vorherigem Memory-Abbild
Manuelle Geräteangabe (z. B. via Textfeld)
Herstellerdatenbank-Zugriff
Reparatur-Protokollierung

6. ?￯ﾸﾏ Kommunikationsschutz
Kamera- & Mikrofonblocker
SecureMailAnalyzer (Scam/Phishing)
Chat & Mailbox-Filter
VPN-Leak-Detector
Router Control Tool (QoS, Bandbreite)
MITM-Detection

7. ?￯ﾸﾏ Crypto- & Quantum-Schutz
Verschlüsselung mit ChaCha20-Poly1305
Secure Random Module (Entropieprüfung)
Quantenresistenter Schutz (McEliece, NTRU, Kyber)
TPM-Verschlüsselung (TPM 2.0 API)
Anti-Jammer + GPS-Spoof-Erkennung

8. ? Studiohardware & Musiker-Support
Herstellerdatenbank (z. B. RME, Focusrite, AKAI etc.)
Treiberprüfung + KI-Tuning
Hardwarereparaturassistent
Audio-Puffer-Optimierung

9. ☁️ Backup, Cloud & Logging
Cloudspeicherung für:
Hardwareabbilder
Fehlerprotokolle (PDF & Email)
Auto-Backup & Wiederherstellung
Logging mit AuditTrail + Zeitstempel
Bug-Tracker + Malware-Quarantäne

10. ? UI/UX & Plattform-Integration
Eigene UIX mit Custom Logo/Design
Multiplattform: Windows, Android, Linux, macOS
Selfextracting Exe Builder
Setup mit Lizenzcodeabfrage
GeoTracker bei Angriffen
Autoupdater & Treiber-Updater
Sprache & Frameworks:
Python (Backend + AI)
C/C++ für Low-Level (Treiber, Temp/TPM)
Rust für Quantenkryptografie & Antidebug
PyInstaller / cx_Freeze für Executables
NSIS/Inno für Installer
Electron oder Qt für UI/UX
Libraries / Tools:
scapy, volatility, psutil, tensorflow, pycryptodome
PyBluez für Bluetooth-Stack
libTPM, ChaCha20Poly1305, secrets, PyCryptoLib
PySide6 oder ElectronJS für GUI
aiohttp, Flask oder FastAPI für Web-API
