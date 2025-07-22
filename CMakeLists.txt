
add_executable(kernel_protect kernel_protect.asm)
set_source_files_properties(kernel_protect.asm PROPERTIES LANGUAGE ASM_NASM)

install(FILES kernel_protect.asm DESTINATION src/Assembler)
install(TARGETS kernel_protect DESTINATION bin)
