package com.pertinax.security.ai

import android.content.Context
import android.graphics.Bitmap
import android.util.Log
import com.pertinax.utils.ImageExporter

class VisualGenerator(private val context: Context) {
    fun generateImageFromText(prompt: String): Bitmap {
        Log.i("VisualGen", "Prompt erhalten: $prompt")
        return ImageExporter.generateMockImage(prompt)
    }
}