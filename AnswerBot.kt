package com.pertinax.security.ai

class AnswerBot {
    fun answer(question: String): String {
        return when {
            question.contains("was ist ein VPN", true) -> "Ein VPN ist ein virtuelles privates Netzwerk, das deine Verbindung verschlüsselt."
            question.contains("wie funktioniert das Tool", true) -> "Das Pertinax Security Tool scannt dein Gerät, blockiert Angriffe und meldet Sicherheitsprobleme."
            else -> "Die Frage wurde erkannt. Eine KI-Auswertung läuft im Hintergrund."
        }
    }
}