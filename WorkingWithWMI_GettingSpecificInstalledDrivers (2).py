# Analysis of drivers installed on your computer
'''
Source 1: Win32_PnPSignedDriver
class Win32_PnPSignedDriver : CIM_Service
{
1.	  string   ClassGuid;
2.	  string   CompatID;
3.	  string   Description;
4.	  string   DeviceClass;
5.	  string   DeviceID;
6.	  string   DeviceName;
7.	  string   DevLoader;
8.	  string   DriverDate;
9.	  string   DriverName;
10.	  string   DriverVersion;
11.	  string   FriendlyName;
12.	  string   HardWareID;
13.	  string   InfName;
14.	  datetime InstallDate;
15.	  boolean  IsSigned;
16.	  string   Location;
17.	  string   Manufacturer;
18.	  string   Name;
19.	  string   PDO;
20.	  string   DriverProviderName;
21.	  string   Signer;
22.	  boolean  Started;
23.	  string   StartMode;
24.	  string   Status;
25.	  string   SystemCreationClassName;
26.	  string   SystemName;

};


Source 2: Win32_SystemDriver 
https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-systemdriver

[Dynamic, Provider("CIMWin32"), SupportsUpdate, UUID("{8502C4C5-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SystemDriver : Win32_BaseService
{
1.	  boolean  AcceptPause;
2.	  boolean  AcceptStop;
3.	  string   Caption;
4.	  string   CreationClassName;
5.	  string   Description;
6.	  boolean  DesktopInteract;
7.	  string   DisplayName;
8.	  string   ErrorControl;
9.	  uint32   ExitCode;
10.	  datetime InstallDate;
11.	  string   Name;
12.	  string   PathName;
13.	  uint32   ServiceSpecificExitCode;
14.	  string   ServiceType;
15.	  boolean  Started;
16.	  string   StartMode;
17.	  string   StartName;
18.	  string   State;
19.	  string   Status;
20.	  string   SystemCreationClassName;
21.	  string   SystemName;
22.	  uint32   TagId;

};


Source 3: Win32_SystemDriver - The Win32_SystemDriver class represents the system driver for a base service.
https://powershell.one/wmi/root/cimv2/win32_systemdriver

'''

import wmi
conn = wmi.WMI()
for driver in conn.Win32_PnPSignedDriver():
    print(driver.DeviceName, driver.DriverVersion, driver.FriendlyName, driver.InfName, driver.InstallDate, driver.IsSigned, driver.Location, driver.Manufacturer, driver.Name, driver.PDO, driver.DriverProviderName, driver.Signer, driver.Started, driver.StartMode, driver.Status, driver.SystemCreationClassName, driver.SystemName)
    
    print(" ")
    print("########################################################################################")
    
    