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
  boolean  AcceptPause;
  boolean  AcceptStop;
  string   Caption;
  uint32   CheckPoint;
  string   CreationClassName;
  boolean  DelayedAutoStart;
  string   Description;
  boolean  DesktopInteract;
  string   DisplayName;
  string   ErrorControl;
  uint32   ExitCode;
  datetime InstallDate;
  string   Name;
  string   PathName;
  uint32   ProcessId;
  uint32   ServiceSpecificExitCode;
  string   ServiceType;
  boolean  Started;
  string   StartMode;
  string   StartName;
  string   State;
  string   Status;
  string   SystemCreationClassName;
  string   SystemName;
  uint32   TagId;
  uint32   WaitHint;
};

'''

import wmi
from prettytable import PrettyTable
from datetime import datetime

for service in conn.Win32_Service():
    print(service.ProcessID, service.Name, service.DisplayName, service.Description, service.PathName, service.InstallDate, service.ServiceType)

    # Initialize the WMI client
    conn = wmi.WMI()
    table = PrettyTable()
    table.field_names = ["Process ID", "Name", "Display Name", "Description", "Path Name", "Install Date",
                         "Service Type", "Start Mode", "State", "Status"]
#information about each service
    for service in conn.Win32_Service():
        install_date = service.InstallDate
        if install_date:
            # Format the install date
            install_date = datetime.strptime(str(install_date), "%Y%m%d%H%M%S.%f%z").strftime("%Y-%m-%d %H:%M:%S")
        table.add_row(
            [service.ProcessId, service.Name, service.DisplayName, service.Description, service.PathName, install_date,
             service.ServiceType, service.StartMode, service.State, service.Status])

    print(" ")
    print("########################################################################################")