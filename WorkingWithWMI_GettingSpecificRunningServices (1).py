# Analysis of services running on your computer
'''
Instruction to better attempt the assignment:
1) Feel free to modified the Python Codes to your own design to ensure better reporting like table format if you can.
2) These Python codes are missing the script to collect other extra information from your personal computers. You will be the one to add more Python Script to collect those missing information.
3) Some information can be obtained online and you are the one to decide how to finalize your assignemnt by conducting online research of the missing information to have a better report.
4) The Python code should be annotated (commented) to indicate what they are actually doing.

References:
Source: https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-service

[Dynamic, Provider("CIMWin32"), SupportsUpdate, UUID("{8502C4D9-5FBB-11D2-AAC1-006008C78BC7}"), DisplayName("Services"), AMENDMENT]
class Win32_Service : Win32_BaseService
{
1.	  boolean  AcceptPause;
2.	  boolean  AcceptStop;
3.	  string   Caption;
4.	  uint32   CheckPoint;
5.	  string   CreationClassName;
6.	  boolean  DelayedAutoStart;
7.	  string   Description;
8.	  boolean  DesktopInteract;
9.	  string   DisplayName;
10.	  string   ErrorControl;
11.	  uint32   ExitCode;
12.	  datetime InstallDate;
13.	  string   Name;
14.	  string   PathName;
15.	  uint32   ProcessId;
16.	  uint32   ServiceSpecificExitCode;
17.	  string   ServiceType;
18.	  boolean  Started;
19.	  string   StartMode;
20.	  string   StartName;
21.	  string   State;
22.	  string   Status;
23.	  string   SystemCreationClassName;
24.	  string   SystemName;
25.	  uint32   TagId;
26.	  uint32   WaitHint;

};

'''

import wmi
conn = wmi.WMI()
for service in conn.Win32_Service():
    print(service.ProcessID, service.Name, service.DisplayName, service.Description, service.PathName, service.InstallDate, service.ServiceType)
    
    print(" ")
    print("########################################################################################")