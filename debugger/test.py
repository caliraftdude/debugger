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
dbg.detach()

#dbg.load("C:\\WINDOWS\\system32\\calc.exe")