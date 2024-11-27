# Analysis of drivers installed on your computer
'''
Source 1: Win32_PnPSignedDriver
class Win32_PnPSignedDriver : CIM_Service
{
  string   ClassGuid;
  string   CompatID;
  string   Description;
  string   DeviceClass;
  string   DeviceID;
  string   DeviceName;
  string   DevLoader;
  string   DriverDate;
  string   DriverName;
  string   DriverVersion;
  string   FriendlyName;
  string   HardWareID;
  string   InfName;
  datetime InstallDate;
  boolean  IsSigned;
  string   Location;
  string   Manufacturer;
  string   Name;
  string   PDO;
  string   DriverProviderName;
  string   Signer;
  boolean  Started;
  string   StartMode;
  string   Status;
  string   SystemCreationClassName;
  string   SystemName;
};


Source 2: Win32_SystemDriver 
https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-systemdriver

[Dynamic, Provider("CIMWin32"), SupportsUpdate, UUID("{8502C4C5-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SystemDriver : Win32_BaseService
{
  boolean  AcceptPause;
  boolean  AcceptStop;
  string   Caption;
  string   CreationClassName;
  string   Description;
  boolean  DesktopInteract;
  string   DisplayName;
  string   ErrorControl;
  uint32   ExitCode;
  datetime InstallDate;
  string   Name;
  string   PathName;
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
    
    