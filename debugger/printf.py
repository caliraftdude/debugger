
def run():
    import os
    from ctypes import cdll, CDLL

    message_string = "Hello World!\n"

    if os.name == 'nt':
        msvcrt = cdll.msvcrt
        msvcrt.printf("Testing: %s", message_string)
    else:
        libc = CDLL("libc.so.6")
        libc.printf("Testing: %s", message_string)
