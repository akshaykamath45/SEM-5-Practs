; multi-segment executable file template
data segment
seg1 db 1h ,2h ,3h
ends
extra segment
seg2 db ?
ends
code segment
start:
; set segment registers:
mov ax, data
mov ds, ax
mov ax, extra
mov es, ax
; add your code here
lea si , seg1
lea di , seg2 
mov cx, 03h
x: mov ah,ds:[si]
mov es:[di],ah

inc si
inc di
dec cx 
jnz x
int 3

ends
end start ; set entry point and stop the assembler.
