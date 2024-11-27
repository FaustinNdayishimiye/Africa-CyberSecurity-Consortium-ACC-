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
  string   CreationClassName;
  string   Caption;
  string   CommandLine;
  datetime CreationDate;
  string   CSCreationClassName;
  string   CSName;
  string   Description;
  string   ExecutablePath;
  uint16   ExecutionState;
  string   Handle;
  uint32   HandleCount;
  datetime InstallDate;
  uint64   KernelModeTime;
  uint32   MaximumWorkingSetSize;
  uint32   MinimumWorkingSetSize;
  string   Name;
  string   OSCreationClassName;
  string   OSName;
  uint64   OtherOperationCount;
  uint64   OtherTransferCount;
  uint32   PageFaults;
  uint32   PageFileUsage;
  uint32   ParentProcessId;
  uint32   PeakPageFileUsage;
  uint64   PeakVirtualSize;
  uint32   PeakWorkingSetSize;
  uint32   Priority;
  uint64   PrivatePageCount;
  uint32   ProcessId;
  uint32   QuotaNonPagedPoolUsage;
  uint32   QuotaPagedPoolUsage;
  uint32   QuotaPeakNonPagedPoolUsage;
  uint32   QuotaPeakPagedPoolUsage;
  uint64   ReadOperationCount;
  uint64   ReadTransferCount;
  uint32   SessionId;
  string   Status;
  datetime TerminationDate;
  uint32   ThreadCount;
  uint64   UserModeTime;
  uint64   VirtualSize;
  string   WindowsVersion;
  uint64   WorkingSetSize;
  uint64   WriteOperationCount;
  uint64   WriteTransferCount;
};

Source 2: The Win32_Process WMI class represents a process on an operating system: https://powershell.one/wmi/root/cimv2/win32_process

'''

import wmi
conn = wmi.WMI()
for process in conn.Win32_Process():
    print(process.ProcessID, process.HandleCount, process.Name, process.ParentProcessId, process.ExecutablePath,)
    
    print(" ")
    print("########################################################################################")