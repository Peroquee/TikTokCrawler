# 🎩 Herr Götzes gesammelte Werke

> Hierbei handelt es sich um eine ansammlung an geklautem code, der folgende dinge macht:  
> - TikTok Crawler: zum Crawlen von TikTok-Videos und speichern der Links wenn ein bestimmter String in der Beschreibung vorkommt.   
> - TikTok Downloader: zum downloaden der Videos hinter den durch den crawler gespeicherten Links  
> - AdioExtraction: extahiert die Tonspur von den runtergeladenen videos
> - Transcribing: Transcribiert die Audiodateien zur verwertung von llm? (nicht implemntiert)
> - Analyse: LLM? das die textdateien auf muster bzw sinnvollen inhalt analysiert (nicht implementiert)
>
---

## 🛠 Voraussetzungen

- Python 3.x  
- [Robot Framework](https://robotframework.org/) installiert (`pip install robotframework`)
- Windows (Getestet unter Windows 10/11)

---

## 🚀 Installation & Start

1. Klone dieses Repository oder lade es herunter  
2. Öffne eine PowerShell bzw. Eingabeaufforderung  
3. Alle komponenten werden aus folgendem Verzeichnis gestartet:
   ```powershell
   cd C:\....\....\...\HerrGoetz1stTry\

## 🐜 Crawler
1. Konfiguriere den Crawler, indem du ${ANZAHL_POSTS} auf die anzahl der Posts setzt die du crawlen willst (tool zum überprüfen wie viele videos ein bestimmter acc hochgeladen hat: https://tokcounter.com/de?user=)
2. Zusätzlich muss noch ${STARTSEITE} auf die startseite des accounts den du crawlen willst gesetzt werden
2. Zum starten des Crawlers gib folgenden Befehl ein:
   ```
   robot --outputdir reports .idea\TikTok_Crawler\tiktokCrawler.robot


