package com.pertinax.security.ai

import android.content.Context
import android.speech.tts.TextToSpeech
import android.util.Log
import java.util.*

class SpeechOutput(context: Context) {
    private val tts: TextToSpeech = TextToSpeech(context) { status ->
        if (status == TextToSpeech.SUCCESS) {
            tts.language = Locale.GERMANY
        }
    }

    fun speak(text: String) {
        Log.i("TTS", "Spricht: $text")
        tts.speak(text, TextToSpeech.QUEUE_FLUSH, null, null)
    }
}