
.section __TEXT,__text,regular,pure_instructions
.globl _start

_start:
    call _check_hooks
    call _exit_cleanly

_check_hooks:
    movl $0x10000000, %esi     ; Beispieladresse
    movl $256, %ecx

.loop:
    movb (%esi), %al
    cmpb $0xE9, %al            ; JMP Opcode prüfen
    je _hook_detected
    incl %esi
    loop .loop
    ret

_hook_detected:
    movl $0x2000004, %eax      ; write syscall
    movl $1, %ebx
    movl $msg_hook, %ecx
    movl $msglen, %edx
    int $0x80
    ret

_exit_cleanly:
    movl $0x2000001, %eax      ; exit syscall
    xorl %ebx, %ebx
    int $0x80

.section __TEXT,__cstring
msg_hook:
    .asciz "macOS Hook erkannt\n"
msglen = . - msg_hook
