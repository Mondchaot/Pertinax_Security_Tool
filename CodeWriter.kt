package com.pertinax.security.ai

class CodeWriter {
    fun generateCode(language: String, task: String): String {
        return when (language.lowercase()) {
            "kotlin" -> "// Kotlin-Code für $task\nfun main() = println(\"$task erledigt\")"
            "python" -> "# Python-Code für $task\ndef main():\n    print('$task erledigt')"
            "java"   -> "// Java-Code für $task\npublic class Main { public static void main(String[] args) { System.out.println(\"$task erledigt\"); }}"
            else     -> "// Unbekannte Sprache"
        }
    }
}