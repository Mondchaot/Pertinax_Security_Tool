
# Pertinax Mining- und Analyseprogramm – Strukturübersicht

## 1. Benutzeroberfläche (GUI)
- Android App (via Chaquopy / Kotlin GUI)
- Icons für alle Module (SVG-Material)
- Bildschirmzoom (Pinch-to-Zoom)
- Energiespar-/Standby-Modus bei Überhitzung

## 2. Miner-System
- Mining-Manager mit:
  - Algorithmuswahl (SHA-256, ChaCha20-Poly1305, etc.)
  - Temperaturprüfung und automatischer Pausierung (2h bei Überhitzung)
  - Autoswitch bei ineffizientem Mining
  - Poolzugang via benutzerdefiniertem Code
  - Hardwarebindung optional (z. B. ZTE Blade, Lenovo)
  - Staking bei unterstützten Coins
- Logging (z. B. Temperatur, Hashrate, Switch-Ereignisse)

## 3. Wallet- und Coin-Modul
- Walletmodell mit:
  - Konten für: Bitcoin, Ethereum, Ethereum Classic, Litecoin, Solana, Polygon, Cardano, Tron, Dogecoin, Bitcoin Cash, BNB, Polkadot
  - Transaktionsübersicht
  - Transferfunktionen (inkl. QR-Code/Adresse)
  - Zugriffsschutz (2FA, Gerätebindung)
- Integration von Cookie-Wallets für Analyse und Mining

## 4. Cookie-Analyse & Sicherheit
- Cookie-Sammlung für o. g. Coins
- Analyse von Miningfähigkeit und Sicherheitsrisiken
- Erkennung von Phishingcode in Webseiten
- API/Webhook zur Meldung verdächtiger Aktivitäten
- Speicherung der Cookie-Ergebnisse optional in Blockchain

## 5. Netzwerk & Datenschutz
- VPN-basierter Netzwerkmonitor (Android)
- Erkennung verdächtiger Verbindungen (Sniffer ohne Root)
- Analyse von Cookies, Domainzugriffen, Downloads
- Blockierung gefährlicher Verbindungen (via DNS/Firewall-Regeln)

## 6. Systemdiagnose
- Module zur Hardwareüberprüfung:
  - CPU, GPU, RAM, Bluetooth-Chip
  - Übertragungsrate, Hotfix, Speicherzugriff
- Treiberprüfung (ZTE, Lenovo etc.)
- Selbsttest der Programmstruktur (KI-gestützt)
- Grundsystemprüfung (z. B. Startpartition, Betriebssystem-Code)

## 7. Wirtschaft & Abrechnung
- Stromgeldkollektor:
  - Tracking des Stromverbrauchs
  - Verteilung auf Poolmitglieder nach KWh
- Steuerrechner:
  - Übersicht über Einnahmen/Ausgaben
  - Export für Finanzamt
- Automatische Gebührenverteilung

## 8. Zusätzliche Module
- KI-Suchfunktion zur Problemerkennung
- Sprachcompiler für technische Anfragen
- ADB-Steuerung bei Root
- Kompilerprüfung, Selbsttests und Fehlerbehandlung
