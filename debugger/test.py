#import printf
#import unions
#printf.run()
#unions.run()

import debugger
dbg = debugger.debugger()
pid = raw_input("Enter the PID of the process to attach to: ")
print("")

dbg.attach(int(pid))
dbg.detach()

#dbg.load("C:\\WINDOWS\\system32\\calc.exe")