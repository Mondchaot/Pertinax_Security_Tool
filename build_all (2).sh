#!/bin/bash

echo "🔧 Starte Buildprozess für Pertinax Security Tool..."

# Windows-Teil
echo "🪟 Kompiliere Windows-Komponenten..."
mkdir -p build/windows
cp -r src/windows/* build/windows/
makensis windows_installer.nsi

# Android-Teil
echo "🤖 Kompiliere Android-Komponenten..."
cd src/android || exit
./gradlew clean assembleRelease
cd ../..

echo "📦 Paketierung der Builds..."
mkdir -p dist
cp src/android/app/build/outputs/apk/release/app-release.apk dist/pertinax_android.apk
cp PertinaxSecurityToolSetup.exe dist/

echo "✅ Alle Builds abgeschlossen und in dist/ bereitgestellt."