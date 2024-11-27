# Application: Analysis of installed software
'''
Instruction to better attempt the assignment:
1) Feel free to modified the Python Codes to your own design to ensure better reporting like table format if you can.
2) These Python codes are missing the script to collect the operating sytem, the firmware and software drivers information from your personal computers. You will be the one to add more Python Script to collect those missing information.
3) Some information can be obtained online and you are the one to decide how to finalize your assignemnt by conducting online research of the missing information to have a better report.


References:
Source 1: winreg — Windows registry access
https://docs.python.org/3/library/winreg.html


HKEY_LOCAL_MACHINE Properties to be used to collect necessary information of installed software:
{
1.	AuthorizedCDFPrefix
2.	BundleAddonCode
3.	BundleCachePath
4.	BundleDetectCode
5.	BundlePatchCode
6.	BundleProviderKey
7.	BundleTag
8.	BundleUpgradeCode
9.	BundleVersion
10.	Comments
11.	Contact
12.	DisplayIcon
13.	DisplayName
14.	DisplayVersion
15.	EstimatedSize
16.	HelpLink
17.	HelpTelephone
18.	Inno Setup
19.	Inno Setup CodeFile
20.	InstallDate
21.	Installed
22.	InstallLanguage
23.	InstallLocation
24.	InstallSource
25.	InstallType
26.	Language
27.	MajorVersion
28.	MinorVersion
29.	ModifyPath
30.	NoElevateOnModify
31.	NoModify
32.	NoRemove
33.	NoRepair
34.	PSChildName
35.	PSDrive
36.	PSParentPath
37.	PSPath
38.	PSProvider
39.	Publisher
40.	QuietUninstallString
41.	Readme
42.	Size  
43.	SystemComponent
44.	UninstallString
45.	URLInfoAbout
46.	URLUpdateInfo
47.	Version
48.	VersionBuild
49.	VersionMajor
50.	VersionTimestamp
51.	WindowsInstaller

}

Source 2: Winreg — Python Library to Retrieve Installed Software Information on Windows Machines
https://medium.com/@tubelwj/winreg-python-library-to-retrieve-installed-software-information-on-windows-machines-f1f14b39650f

Source 3: Get Windows Installed Software by Winreg
https://averainy.com/post/get-windows-installed-software-by-winreg

'''
import winreg

def foo(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            try:
                software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
            except EnvironmentError:
                software['version'] = 'undefined'
            try:
                software['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
            except EnvironmentError:
                software['publisher'] = 'undefined'
            try:
                software['InstallDate'] = winreg.QueryValueEx(asubkey, "InstallDate")[0]
            except EnvironmentError:
                software['InstallDate'] = 'undefined'
            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list

software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + foo(winreg.HKEY_CURRENT_USER, 0)

for software in software_list:
    print('Name=%s, Version=%s, Publisher=%s, InstallDate=%s,' % (software['name'], software['version'], software['publisher'],software['InstallDate']))
print('Number of installed apps: %s' % len(software_list))