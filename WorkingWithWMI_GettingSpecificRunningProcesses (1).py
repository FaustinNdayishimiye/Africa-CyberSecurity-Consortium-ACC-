# Analysis of processes running on your computer
'''
Instruction to better attempt the assignment:
1) Feel free to modified the Python Codes to your own design to ensure better reporting like table format if you can.
2) These Python codes are missing the script to collect other extra information from your personal computers. You will be the one to add more Python Script to collect those missing information.
3) Some information can be obtained online and you are the one to decide how to finalize your assignemnt by conducting online research of the missing information to have a better report.
4) The Python code should be annotated (commented) to indicate what they are actually doing.

References:

1) Source 1: https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-process

[Dynamic, Provider("CIMWin32"), SupportsCreate, CreateBy("Create"), SupportsDelete, DeleteBy("DeleteInstance"), UUID("{8502C4DC-5FBB-11D2-AAC1-006008C78BC7}"), DisplayName("Processes"), AMENDMENT]
class Win32_Process : CIM_Process
{
1.	string   CreationClassName;
2.	string   Caption;
3.	string   CommandLine;
4.	datetime CreationDate;
5.	string   CSCreationClassName;
6.	string   CSName;
7.	string   Description;
8.	string   ExecutablePath;
9.	uint16   ExecutionState;
10.	string   Handle;
11.	uint32   HandleCount;
12.	datetime InstallDate;
13.	uint64   KernelModeTime;
14.	uint32   MaximumWorkingSetSize;
15.	uint32   MinimumWorkingSetSize;
16.	string   Name;
17.	string   OSCreationClassName;
18.	string   OSName;
19.	uint64   OtherOperationCount;
20.	uint64   OtherTransferCount;
21.	uint32   PageFaults;
22.	uint32   PageFileUsage;
23.	uint32   ParentProcessId;
24.	uint32   PeakPageFileUsage;
25.	uint64   PeakVirtualSize;
26.	uint32   PeakWorkingSetSize;
27.	uint32   Priority;
28.	uint64   PrivatePageCount;
29.	uint32   ProcessId;
30.	uint32   QuotaNonPagedPoolUsage;
31.	uint32   QuotaPagedPoolUsage;
32.	uint32   QuotaPeakNonPagedPoolUsage;
33.	uint32   QuotaPeakPagedPoolUsage;
34.	uint64   ReadOperationCount;
35.	uint64   ReadTransferCount;
36.	uint32   SessionId;
37.	string   Status;
38.	datetime TerminationDate;
39.	uint32   ThreadCount;
40.	uint64   UserModeTime;
41.	uint64   VirtualSize;
42.	string   WindowsVersion;
43.	uint64   WorkingSetSize;
44.	uint64   WriteOperationCount;
45.	uint64   WriteTransferCount;

};

Source 2: The Win32_Process WMI class represents a process on an operating system: https://powershell.one/wmi/root/cimv2/win32_process

'''

import wmi
conn = wmi.WMI()
for process in conn.Win32_Process():
    print(process.ProcessID, process.HandleCount, process.Name, process.ParentProcessId, process.ExecutablePath,)
    
    print(" ")
    print("########################################################################################")