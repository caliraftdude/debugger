#import printf
#import unions
#printf.run()
#unions.run()


# important:  If you are using this on a 64-bit version of Windows then you have
# to run processes that are 32-bit.  Instead of the normal calc.exe, run the file
# that is in c:\windows\sysWOW64\ instead.. this will result in the 32-bit version
# running.  You will see this in the task list accordingly.

import debugger
dbg = debugger.debugger()
pid = raw_input("Enter the PID of the process to attach to: ")
print("")

dbg.attach(int(pid))
printf_address = dbg.func_resolve("msvcrt.dll", "printf")
print "[*] Address of printf: 0x%08x" % printf_address
dbg.bp_set(printf_address)

"""
list = dbg.enumerate_threads()

# For each thread in the list we want to grab the value of each of the registers
for thread in list:
    thread_context = dbg.get_thread_context(thread)

    # Now let's output the contents of some of the registers
    print "[*] Dumping registers for thread ID: 0x%08x" % thread
    print "[**] EIP: 0x%08x" % thread_context.Eip
    print "[**] ESP: 0x%08x" % thread_context.Esp
    print "[**] EBP: 0x%08x" % thread_context.Ebp
    print "[**] EAX: 0x%08x" % thread_context.Eax
    print "[**] EBX: 0x%08x" % thread_context.Ebx
    print "[**] ECX: 0x%08x" % thread_context.Ecx
    print "[**] EDX: 0x%08x" % thread_context.Edx
    print "[*] END DUMP"
    print ""
"""

dbg.run()
dbg.detach()

#dbg.load("C:\\WINDOWS\\system32\\calc.exe")