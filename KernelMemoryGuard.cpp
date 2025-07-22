
// Datei: KernelMemoryGuard.cpp
#include <windows.h>
#include <iostream>
#include <psapi.h>

bool CheckMemoryWriteAccess(LPVOID addr) {
    MEMORY_BASIC_INFORMATION mbi;
    if (VirtualQuery(addr, &mbi, sizeof(mbi))) {
        return (mbi.Protect & PAGE_EXECUTE_READWRITE || mbi.Protect & PAGE_READWRITE);
    }
    return false;
}

int main() {
    SYSTEM_INFO si;
    GetSystemInfo(&si);
    for (LPBYTE addr = (LPBYTE)si.lpMinimumApplicationAddress; addr < (LPBYTE)si.lpMaximumApplicationAddress; addr += 0x10000) {
        if (CheckMemoryWriteAccess(addr)) {
            std::cout << "Warnung: Schreibbarer Speicher entdeckt: " << static_cast<void*>(addr) << std::endl;
        }
    }
    return 0;
}
