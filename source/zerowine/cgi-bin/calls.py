# If I missed something, please let me know.

INTERESTING_CALLS = {# "shdocvw":"",
                     # "http://":"",
                     "^([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])": "",
                     # Common debugger detection techniques
                     "KERNEL32\.OutputDebugString": "",
                     "KERNEL32\.IsDebuggerPresent": "",
                     "KERNEL32\.CheckRemoteDebuggerPresent": "",
                     "KERNEL32\.SetUnhandledExceptionFilter": "", # Need more tests
                     "KERNEL32\.UnhandledExceptionFilter": "",
                     "user32\.FindWindow": "", # For OllyDbg, i.e.
                     # Add more interesting calls
                     # Advapi32
                     "advapi32\.RegOpenKey": "",
                     "advapi32\.RegCreate": "",
                     "advapi32\.RegDelete": "",
                     "advapi32\.RegGet": "",
                     "advapi32\.RegSetValue": "",
                     "advapi32\.RegQueryValue": "",
                     "advapi32\.CreateService": "/* Suspicious behavior: Create service object without user interaction, Possible malware prefix: Trojan, False positive rate: Medium */\n",
                     "advapi32\.OpenService": "",
                     "advapi32\.StartService": "",
                     # Ntdll
                     "ntdll\.NtCreateFile": "",
                     "ntdll\.ZwCreateFile": "",
                     "ntdll\.NtDeleteFile": "",
                     "ntdll\.ZwDeleteFile": "",
                     #	"ntdll\.NtWriteFile":"",
                     #	"ntdll\.ZwWriteFile":"",
                     "ntdll\.NtLoadDriver": "/* Suspicious behavior: Load device driver without user interaction, Possible malware prefix: Trojan-Rootkit, False positive rate: Medium */\n",
                     "ntdll\.ZwLoadDriver": "/* Suspicious behavior: Load device driver without user interaction, Possible malware prefix: Trojan-Rootkit, False positive rate: Medium */\n",
                     "ntdll\.NtMapViewOfSection": "",
                     "ntdll\.ZwMapViewOfSection": "",
                     "ntdll\.NtUnmapViewOfSection": "",
                     "ntdll\.ZwUnmapViewOfSection": "",
                     "ntdll\.NtSystemDebugControl": "",
                     "ntdll\.ZwSystemDebugControl": "",
                     "ntdll\.NtQueryInformationProcess": "", # Need more tests
                     "ntdll\.ZwQueryInformationProcess": "", # Need more tests
                     "ntdll\.NtQueryObject": "", # Need more tests
                     "ntdll\.ZwQueryObject": "", # Need more tests
                     # Kernel32
                     "KERNEL32\.CreateSemaphore": "",
                     "KERNEL32\.CreateMutex": "",
                     "KERNEL32\.CreateProcess": "",
                     #	"KERNEL32\.CreateThread":"",
                     "KERNEL32\.CreateRemoteThread": "",
                     "KERNEL32\.CreateToolhelp32Snapshot": "", # Need more tests
                     "KERNEL32\.Process32First": "",
                     "KERNEL32\.Process32Next": "",
                     "KERNEL32\.TerminateProcess": "",
                     #	"KERNEL32\.ExitProcess":"",
                     "KERNEL32\.CreateFile": "",
                     "KERNEL32\.DeleteFile": "",
                     #	"KERNEL32\.WriteFile":"",
                     "KERNEL32\.CopyFile": "",
                     "KERNEL32\.MoveFile": "",
                     "KERNEL32\.SetFileAttributes": "",
                     "KERNEL32\.GetFileTime": "",
                     "KERNEL32\.SetFileTime": "",
                     "KERNEL32\.CreateDirectory": "",
                     "KERNEL32\.RemoveDirectory": "",
                     #	"KERNEL32\.GetProcAddress":"",
                     "KERNEL32\.GetThreadContext": "",
                     "KERNEL32\.ReadProcessMemory": "",
                     "KERNEL32\.VirtualAllocEx": "",
                     "KERNEL32\.WriteProcessMemory": "",
                     "KERNEL32\.SetThreadContext": "",
                     "KERNEL32\.ResumeThread": "",
                     "KERNEL32\.DeviceIoControl": "/* Suspicious behavior: Send control code directly to specified device driver without user interaction, Possible malware prefix: Trojan-Rootkit, False positive rate: Medium */\n",
                     "KERNEL32\.WinExec": "",
                     "KERNEL32\.GetTempPath": "",
                     #	"KERNEL32\.OpenEvent":"",
                     "KERNEL32\.GetCurrentProcess": "", # Need more tests
                     "KERNEL32\.GetVersion": "", # Need more tests
                     'KERNEL32\.GetProcAddress(.*"CsrGetProcessId")': "/* Not implemented yet. Tested under pure Wine 1.5.23. */\n",
                     'KERNEL32\.GetProcAddress(.*"wine_get_.*_file_name")': "/* Warning: Possible Wine detection. */\n",
                     'KERNEL32\.GetLocalTime': "",
                     # Winsock
                     "trace:winsock:WSASocket.*created": "",
                     "trace:winsock:WS_bind": "",
                     "trace:winsock:WS_connect": "", "trace:winsock:WS_listen": "",
                     "trace:winsock:WS_accept": "",
                     "trace:winsock:WSASendTo": "",
                     "trace:winsock:WSARecvFrom": "",
                     "trace:winsock:WS_closesocket": "",
                     "trace:winsock:WS_getaddrinfo": "",
                     "trace:winsock:WS_gethostbyname": "",
                     #	"ws2_32\.bind":"",
                     #	"ws2_32\.connect":"", "ws2_32\.listen":"",
                     #	"ws2_32\.accept":"",
                     #	"ws2_32\.send":"",
                     #	"ws2_32\.recv":"",
                     #	"ws2_32\.getaddrinfo":"",
                     #	"ws2_32\.gethostbyname":"",
                     "ws2_32\.WSCInstallProvider": "/* Suspicious behavior: Install transport provider without user interaction, Possible malware prefix: Trojan, False positive rate: Low */\n",
                     "ws2_32\.WSCWriteProviderOrder": "",
                     # Shell32
                     "shell32\.ShellExecute": "",
                     "shell32\.FindExecutable": "",
                     "shell32\.SHGetSpecialFolderPath": "",
                     # User32
                     "user32\.MessageBox": "",
                     "user32\.SetDlgItemText": "",
                     "user32\.SetWindowText": "",
                     "user32\.DrawText": "",
                     #	"user32\.CreateWindow":"",
                     "user32\.SetWindowsHookEx": "/* Suspicious behavior: Install application-defined hook procedure without user interaction, Possible malware prefix: Trojan, False positive rate: High */\n",
                     "user32\.GetShellWindow": "", # Need more tests
                     "user32\.GetWindowThreadProcessId": "", # Need more tests
                     "user32\.GetCursorPos": "", # Need more tests
                     # Wininet
                     #	"trace:wininet:InternetOpen":"",
                     #	"trace:wininet:InternetCrack":"",
                     #	"trace:wininet:InternetConnect":"",
                     #	"trace:wininet:InternetClose":"",
                     #	"trace:wininet:HttpOpen":"",
                     #	"trace:wininet:HttpSend":"",
                     #	"trace:wininet:Ftp":"",
                     #	"trace:wininet:Internet_ConfigureProxy":"",
                     "wininet\.InternetOpen": "",
                     "wininet\.InternetCrack": "",
                     "wininet\.InternetConnect": "",
                     "wininet\.InternetClose": "",
                     "wininet\.HttpOpen": "",
                     "wininet\.HttpSend": "",
                     #	"wininet\.Ftp":"",
                     # Winspool
                     "winspool\.drv\.GetPrintProcessorDirectory": "",
                     "winspool\.drv\.AddPrintProcessor": "/* Suspicious behavior: Install print processor without user interaction, Possible malware prefix: Trojan-Rootkit, False positive rate: Low */\n",
                     "winspool\.drv\.DeletePrintProcessor": "",
                     # load_native_dll
                     "trace:loaddll:load_native_dll": "",
                     # Starting process
                     "Starting process": "",
                     # Starting thread
                     "Starting thread proc": "",
                     # Urlmon
                     "urlmon\.URL": "",
                     # Driver init
                     "Call driver init ": "",
                     # Fltlib
                     "fltlib.FilterUnload": "/* Suspicious behavior: Unload minifilter without user interaction, Possible malware prefix: Trojan, False positive rate: Low */\n",
                     # Netapi32
                     "netapi32.NetScheduleJobAdd": "/* Suspicious behavior: Schedule job to run without user interaction, Possible malware prefix: Trojan, False positive rate: Low */\n",

                     # Errors
                     # Wine
                     "wine: cannot find": "",
                     "wine: Install Mono for Windows to run .NET applications.": "",
                     # can't load dll
                     "can't load DLL:": "",
                     # Module
                     "err:module:import_dll": "",
                     "err:module:LdrInitializeThunk": "",
                     "err:module:attach_process_dlls": "",
                     # WinMain
                     "err:rundll32:wWinMain": "",
                     "err:rundll32:WinMain": "",
                     # TLS callback
                     "Call TLS callback ": ""
}

JUNK_CALLS = ['L"Software\\\\\\\\Microsoft\\\\\\\\Windows\\\\\\\\CurrentVersion\\\\\\\\ThemeManager',
              'L"Software\\\\\\\\Microsoft\\\\\\\\Windows\\\\\\\\CurrentVersion\\\\\\\\Explorer\\\\\\\\User Shell Folders"',
              'L"Software\\\\\\\\Microsoft\\\\\\\\Windows\\\\\\\\CurrentVersion\\\\\\\\Explorer\\\\\\\\Shell Folders"',
              'L"Software\\\\\\\\Microsoft\\\\\\\\Windows NT\\\\\\\\CurrentVersion\\\\\\\\ProfileList"',
              'Software\\\\\\\\Wine',
              'L"winedbg.exe"', '"RPCSSMasterMutex0x',
              'L"System\\\\\\\\CurrentControlSet\\\\\\\\Control\\\\\\\\NetworkProvider\\\\\\\\Order',
              # The following SHOULD be removed
              'L"DejaVu', 'Font', '() retval', '(TrueType)',
              'WindowMetrics', 'desktop.ini', 'Colors",00000000', '{9D20AAE8-0625-44B0-9CA7-71889C2254D9}',
              # Add more junk calls
              'c:!windows!',
              'c:!users!',

              'Reg(Set|Query)ValueEx.*L"Desktop"',
              'Reg(Set|Query)ValueEx.*L"Programs"',
              'Reg(Set|Query)ValueEx.*L"Personal"',
              'Reg(Set|Query)ValueEx.*L"Favorites"',
              'Reg(Set|Query)ValueEx.*L"StartUp"',
              'Reg(Set|Query)ValueEx.*L"Recent"',
              'Reg(Set|Query)ValueEx.*L"SendTo"',
              'Reg(Set|Query)ValueEx.*L"Start Menu"',
              'Reg(Set|Query)ValueEx.*L"NetHood"',
              'Reg(Set|Query)ValueEx.*L"Templates"',
              'Reg(Set|Query)ValueEx.*L"Common Start Menu"',
              'Reg(Set|Query)ValueEx.*L"Common Programs"',
              'Reg(Set|Query)ValueEx.*L"Common StartUp"',
              'Reg(Set|Query)ValueEx.*L"Common Desktop"',
              'Reg(Set|Query)ValueEx.*L"Common AppData"',
              'Reg(Set|Query)ValueEx.*L"Local AppData"',
              'Reg(Set|Query)ValueEx.*L"AppData"',
              'Reg(Set|Query)ValueEx.*L"PrintHood"',
              'Reg(Set|Query)ValueEx.*L"Common Favorites"',
              'Reg(Set|Query)ValueEx.*L"Cookies"',
              'Reg(Set|Query)ValueEx.*L"Cache"',
              'Reg(Set|Query)ValueEx.*L"History"',
              'Reg(Set|Query)ValueEx.*L"My Music"',
              'Reg(Set|Query)ValueEx.*L"My Videos"',
              'Reg(Set|Query)ValueEx.*L"My Pictures"',
              'Reg(Set|Query)ValueEx.*L"CommonMusic"',
              'Reg(Set|Query)ValueEx.*L"CommonPictures"',
              'Reg(Set|Query)ValueEx.*L"CommonVideo"',
              'Reg(Set|Query)ValueEx.*L"Common Templates"',
              'Reg(Set|Query)ValueEx.*L"Common Documents"',
              'Reg(Set|Query)ValueEx.*L"Common Administrative Tools"',
              'RegQueryValueEx.*L"ProfilesDirectory"',
              'RegQueryValueEx.*L"AllUsersProfile"',
              'RegQueryValueEx.*L"ThreadingModel"',
              'RegQueryValueEx.*L"Administrative Tools"',
              'RegQueryValueEx.*L"CD Burning"',
              'RegQueryValueEx.*"MS Shell Dlg 2"',

              'Reg(OpenKey|GetValue).*"\.\w{2,9}"',
              'Reg(OpenKey|GetValue).*L"\w{2,9}file"',
              'Reg(OpenKey|GetValue).*L"\w{2,9}\.file"',
              'Reg(OpenKey|GetValue).*L"\w{2,9} File"',
              'RegOpenKey.*L"\w{2,9}file\\\\\\\\DefaultIcon"', ###
              'RegOpenKey.*L"ProgID"',
              'RegOpenKey.*L"command"',
              'RegOpenKey.*L"shell"',
              'RegOpenKey.*L"open"',
              'RegOpenKey.*".*shell\\\\\\\\open\\\\\\\\command",', ##
              'RegOpenKey.*L"opennew"', ##
              'RegOpenKey.*L"edit"', ##
              'Reg(OpenKey|GetValue).*L".*wab_auto_file"', ##
              'Reg(OpenKey|GetValue).*L"InternetShortcut"', ##
              'RegOpenKey.*L"Generate Typelib"', ##
              'RegOpenKey.*L"Subscribe"', ##
              'RegOpenKey.*L"shellex\\\\\\\\ContextMenuHandlers"', #
              'RegGetValue.*L"Content Type",',
              'RegGetValue.*L"DefaultIcon",',
              'RegOpenKeyEx.*\(\w{8},\w{8},\w{8},\w{8},\w{8}\)',
              'RegSetValueEx.*\(\w{8},\w{8},\w{8},\w{8},\w{8},\w{8}\)',
              'RegQueryValue.*\(\w{8},\w{8},\w{8},\w{8}\)',
              'RegQueryValueEx.*\(\w{8},\w{8},\w{8},\w{8},\w{8},\w{8}\)',
              'RegSetValueExA.* ""',

              'RegCreateKey.*L"System\\\\\\\\CurrentControlSet\\\\\\\\Control\\\\\\\\Print\\\\\\\\Printers',
              'RegOpenKeyW.*L"System\\\\\\\\CurrentControlSet\\\\\\\\Control\\\\\\\\Keyboard Layouts\\\\\\\\04090409",',
              'RegOpenKeyEx.*"System\\\\\\\\CurrentControlSet\\\\\\\\Services\\\\\\\\BITS',

              'CreateFileW.*L"NUL",',

              'DrawText.* ""',
              'DrawText.* " "',
              'DrawText.* L" "',
              'SetWindowText.*""',
              'SetWindowText.* " "',
              'SetWindowText.*\(\w{8},\w{8}\)',
              'SetDlgItemText.*""',
              'CompareString',
              'MessageBox.*\(\w{8},\w{8},\w{8},\w{8}\)',

              'CreateSemaphore.*\(\w{8},\w{8},\w{8},\w{8}\)',
              'CreateMutex.*\(\w{8},\w{8},\w{8}\)',

              # Help
              'RegOpenKeyExA.*"Software\\\\\\\\Microsoft\\\\\\\\Windows",',
              'RegOpenKeyExA.*"HTML Help",',
              'RegOpenKeyExA.*"Help",',
              # Wininet & Internet Explorer
              'trace:wininet:',
              #	'fixme:wininet:',
              #	'fixme:urlmon:',
              'CreateFile.*C:\\\\\\\\users\\\\\\\\\w*\\\\\\\\Local Settings\\\\\\\\Temporary Internet Files\\\\\\\\Content\.IE5\\\\\\\\index\.dat"',
              'CreateFile.*C:\\\\\\\\users\\\\\\\\\w*\\\\\\\\Local Settings\\\\\\\\History\\\\\\\\History\.IE5\\\\\\\\index\.dat"',
              'CreateFile.*C:\\\\\\\\users\\\\\\\\\w*\\\\\\\\Cookies\\\\\\\\index\.dat"',
              'CreateFileMapping.*C:_users_\w*_Local Settings_Temporary Internet Files_Content\.IE5_index\.dat_',
              'CreateFileMapping.*C:_users_\w*_Local Settings_History_History\.IE5_index\.dat_',
              'CreateFileMapping.*C:_users_\w*_Cookies_index\.dat_',
              'CreateFileMapping.*\(\w{8},\w{8},\w{8},\w{8},\w{8},\w{8}\)',
              'CreateDirectory.*"C:\\\\\\\\users\\\\\\\\\w*\\\\\\\\Local Settings\\\\\\\\Temporary Internet Files\\\\\\\\Content\.IE5\\\\\\\\',
              'CreateDirectory.*"C:\\\\\\\\users\\\\\\\\\w*\\\\\\\\Local Settings\\\\\\\\History\\\\\\\\History\.IE5\\\\\\\\',
              'CreateDirectory.*"C:\\\\\\\\users\\\\\\\\\w*\\\\\\\\Cookies\\\\\\\\',
              'RegOpenKey.*"Software\\\\\\\\Classes\\\\\\\\Protocols\\\\\\\\Filter\\\\\\\\',
              'RegOpenKey.*L"Software\\\\\\\\Microsoft\\\\\\\\Internet Explorer\\\\\\\\International",',
              'RegOpenKey.*"Software\\\\\\\\Microsoft\\\\\\\\Windows\\\\\\\\CurrentVersion\\\\\\\\Internet Settings\\\\\\\\Cache\\\\\\\\Content",',
              'RegOpenKey.*L"PROTOCOLS\\\\\\\\Handler\\\\\\\\about",',
              'RegOpenKey.*"InternetExplorer\.Application",',
              'DrawTextW.*L"Back"',
              'DrawTextW.*L"Forward"',
              'DrawTextW.*L"Stop"',
              'DrawTextW.*L"Refresh"',
              'DrawTextW.*L"Home"',
              'DrawTextW.*L"Print..."',

              # msvcrt._mbs*
              'msvcrt\._mbs',
              # oleaut32
              'oleaut32.VarBstr',
              'oleaut32.Sys.*String',
              'trace:ole:dump_Variant',

              # Wine
              'CreateMutexW.*L"__WINE_.*_MUTEX__"',

              'RegCreateKeyW.*L"Software\\\\\\\\Wine\\\\\\\\FileOpenAssociations"',
              'RegCreateKeyW.*L"Software\\\\\\\\Wine\\\\\\\\MenuFiles"',
              'RegOpenKey.*"Software\\\\\\\\Wine\\\\\\\\Drivers"',
              'RegOpenKey.*"Software\\\\\\\\Wine\\\\\\\\Explorer"',
              'RegOpenKey.*"Software\\\\\\\\Wine\\\\\\\\X11 Driver"',
              'RegOpenKey.*"Software\\\\\\\\Wine\\\\\\\\Alsa Driver"',
              'RegOpenKey.*"Software\\\\\\\\Wine\\\\\\\\Network"',
              'RegOpenKey.*"Software\\\\\\\\Wine\\\\\\\\MSHTML"',
              'RegOpenKey.*"Software\\\\\\\\Wine\\\\\\\\WineFile"',
              # Wine (Console)
              'RegOpenKeyExW.*L"Software\\\\\\\\Microsoft\\\\\\\\Command Processor",',
              'RegOpenKeyW.*L"Console"',
              'RegCreateKeyW.*L"Console"',
              'RegSetValueExW.*L"CursorSize"',
              'RegSetValueExW.*L"CursorVisible"',
              'RegSetValueExW.*L"EditionMode"',
              'RegSetValueExW.*L"ExitOnDie"',
              'RegSetValueExW.*L"FaceName"',
              'RegSetValueExW.*L"HistoryBufferSize"',
              'RegSetValueExW.*L"HistoryNoDup"',
              'RegSetValueExW.*L"MenuMask"',
              'RegSetValueExW.*L"QuickEdit"',
              'RegSetValueExW.*L"ScreenBufferSize"',
              'RegSetValueExW.*L"WindowSize"',
              # Wine (ACM drivers)
              #	'RegOpenKeyExW.*L"Software\\\\\\\\Microsoft\\\\\\\\Windows NT\\\\\\\\CurrentVersion",',
              #	'RegOpenKeyExW.*L"Software\\\\\\\\Microsoft\\\\\\\\Windows NT\\\\\\\\CurrentVersion\\\\\\\\Drivers32",',
              #	'RegOpenKeyExW.*L"Drivers32",',

              'RegOpenKeyW.*L"Software\\\\\\\\Microsoft\\\\\\\\Multimedia\\\\\\\\Audio Compression Manager\\\\\\\\Priority v4.00"',
              'RegCreateKeyW.*L"Software\\\\\\\\Microsoft\\\\\\\\AudioCompressionManager\\\\\\\\DriverCache\\\\\\\\msacm\.imaadpcm"',
              'RegCreateKeyW.*L"Software\\\\\\\\Microsoft\\\\\\\\AudioCompressionManager\\\\\\\\DriverCache\\\\\\\\msacm\.msadpcm"',
              'RegCreateKeyW.*L"Software\\\\\\\\Microsoft\\\\\\\\AudioCompressionManager\\\\\\\\DriverCache\\\\\\\\msacm\.msg711"',
              'RegCreateKeyW.*L"Software\\\\\\\\Microsoft\\\\\\\\AudioCompressionManager\\\\\\\\DriverCache\\\\\\\\msacm\.winemp3"',
              'RegCreateKeyW.*L"Software\\\\\\\\Microsoft\\\\\\\\AudioCompressionManager\\\\\\\\DriverCache\\\\\\\\msacm\.msgsm610"',
              'RegCreateKeyW.*L"Software\\\\\\\\Microsoft\\\\\\\\AudioCompressionManager\\\\\\\\DriverCache\\\\\\\\msacm32\.dll"',
              'Reg(Set|Query)ValueExA.*"cFormatTags"',
              'Reg(Set|Query)ValueExA.*"cFilterTags"',
              'Reg(Set|Query)ValueExA.*"fdwSupport"',
              'Reg(Set|Query)ValueExA.*"aFormatTagCache"',
              # Wine (Gecko)
              'L"C:\\\\\\\\windows\\\\\\\\system32\\\\\\\\gecko\\\\\\\\1\.0\.0\\\\\\\\wine_gecko\\\\\\\\', # 1.0
              'RegOpenKeyA.*"1\.0\.0"', # 1.0
              'L"C:\\\\\\\\windows\\\\\\\\system32\\\\\\\\gecko\\\\\\\\1\.6\\\\\\\\wine_gecko\\\\\\\\', # 1.6
              'RegOpenKeyA.*"1\.6"', # 1.6
              'L"C:\\\\\\\\windows\\\\\\\\system32\\\\\\\\gecko\\\\\\\\1\.7\\\\\\\\wine_gecko\\\\\\\\', # 1.7
              'RegOpenKeyA.*"1\.7"', # 1.7
              # Windows Script Host
              'L"Software\\\\\\\\Microsoft\\\\\\\\Windows Script Host\\\\\\\\Settings"',
              '"VBSFile\\\\\\\\ScriptEngine"',
              '"VBEFile\\\\\\\\ScriptEngine"',
              '"JSFile\\\\\\\\ScriptEngine"',
              '"JSEFile\\\\\\\\ScriptEngine"',
              # CLSID
              'RegOpenKey.*L"Interface\\\\\\\\{.*}\\\\\\\\ProxyStubClsid32",',
              'RegOpenKey.*L"Interface\\\\\\\\{.*}\\\\\\\\Typelib",',
              'RegOpenKey.*L"Typelib\\\\\\\\',
              'RegOpenKey.*"CLSID\\\\\\\\',
              'RegOpenKey.*L"InprocServer32"',
              'RegOpenKey.*"TYPELIB\\\\\\\\{.*}\\\\\\\\6.0\\\\\\\\9",',
              'RegQueryValueW.*L".*\\\\\\\\win32"',
              'RegQueryValueExW.*L"CallForAttributes",',
              'RegQueryValueExW.*L"WantsForParsing",',

              'L"VBS.*\\\\\\\\CLSID"',
              #	'L"VBS Author\\\\\\\\CLSID"',
              #	'L"VBScript\\\\\\\\CLSID"',
              #	'L"VBScript Author\\\\\\\\CLSID"',
              #	'L"VBScript\.Encode\\\\\\\\CLSID"',
              #	'L"VBScript\.RegExp\\\\\\\\CLSID"',
              'L"JavaScript.*\\\\\\\\CLSID"',
              'L"JScript.*\\\\\\\\CLSID"',
              #	'L"JScript Author\\\\\\\\CLSID"',
              #	'L"JScript\.Encode\\\\\\\\CLSID"',
              'L"WScript.*\\\\\\\\CLSID"',
              #	'L"WScript\.Network\\\\\\\\CLSID"',
              #	'L"WScript\.Network\.1\\\\\\\\CLSID"',
              #	'L"WScript\.Shell\\\\\\\\CLSID"',
              #	'L"WScript\.Shell\.1\\\\\\\\CLSID"',
              'L"Scripting.*\\\\\\\\CLSID"',
              #	'L"Scripting\.Dictionary\\\\\\\\CLSID"',
              #	'L"Scripting\.Encoder\\\\\\\\CLSID"',
              #	'L"Scripting\.FileSystemObject\\\\\\\\CLSID"',
              #	'L"Scripting\.Signer\\\\\\\\CLSID"',
              'L"WinMgmts\\\\\\\\CLSID"',
              'L"Shell\.Application\\\\\\\\CLSID"',
              'L"HNetCfg\.FwMgr\\\\\\\\CLSID"',
              'L"ADODB\.Stream\\\\\\\\CLSID"',
              'L"Microsoft\.XMLHTTP\\\\\\\\CLSID"',
              'L"Shell\.Explorer\\\\\\\\CLSID"',
              # Windows Explorer
              '"Software\\\\\\\\Microsoft\\\\\\\\Windows\\\\\\\\CurrentVersion\\\\\\\\Explorer\\\\\\\\AutoComplete",',
              '"Software\\\\\\\\Microsoft\\\\\\\\Windows\\\\\\\\CurrentVersion\\\\\\\\Explorer\\\\\\\\Performance",',
              # Control Panel
              '"Control Panel\\\\\\\\Colors",',
              '"Control Panel\\\\\\\\International",',
              '"Control Panel\\\\\\\\Mouse",',
              # MIME
              'RegOpenKey.*"MIME\\\\\\\\Database\\\\\\\\Content Type\\\\\\\\',
              # Services
              'OpenService.*"BITS",',
              'OpenService.*"Eventlog",',
              'OpenService.*"MountMgr",',
              'OpenService.*"MSIServer",',
              'OpenService.*"Spooler",',
              'OpenService.*"stisvc",',
              'OpenService.*"TermService",',

              'OpenService.*"AppMgmt",',
              'OpenService.*"FastUserSwitchingCompatibility",',
              'OpenService.*"WmdmPmSN",',
              'OpenService.*"xmlprov",',
              'OpenService.*"EventSystem",',
              'OpenService.*"Ntmssvc",',
              'OpenService.*"upnphost",',
              'OpenService.*"SSDPSRV",',
              'OpenService.*"Netman",',
              'OpenService.*"Nla",',
              'OpenService.*"TapiSrv",',
              'OpenService.*"Browser",',
              'OpenService.*"CryptSvc",',
              'OpenService.*"helpsvc",',
              'OpenService.*"RemoteRegistry",',
              'OpenService.*"Schedule",',
              'OpenService.*"RasAuto",',
              'OpenService.*"Sharedaccess",',
              #	'OpenService.*"wscsvc",',
              'OpenService.*"Themes",',
              # Wine menubuilder
              'CreateSemaphore.*"winemenubuilder_semaphore"',
              'RegSetValueExA.*\(null\)\/.*\.desktop',
              'RegSetValueExA.*\(null\)\/.*\.menu',

              # MSTCP
              'RegOpenKeyExW.*L"System\\\\\\\\CurrentControlSet\\\\\\\\Services\\\\\\\\VxD\\\\\\\\MSTCP",',
              'RegQueryValueEx.*L"EnableDNS"',
              'RegQueryValueEx.*L"BcastNameQueryCount"',
              'RegQueryValueEx.*L"BcastNameQueryTimeout"',
              'RegQueryValueEx.*L"NameSrvQueryCount"',
              'RegQueryValueEx.*L"NameSrvQueryTimeout"',
              'RegQueryValueEx.*L"ScopeID"',
              'RegQueryValueEx.*L"CacheTimeout"',

              # WineDbg
              'RegQueryValueExA.*"BreakAllThreadsStartup"',
              'RegQueryValueExA.*"BreakOnCritSectTimeOut"',
              'RegQueryValueExA.*"BreakOnAttach"',
              'RegQueryValueExA.*"BreakOnFirstChance"',
              'RegQueryValueExA.*"BreakOnDllLoad"',
              'RegQueryValueExA.*"CanDeferOnBPByAddr"',
              'RegQueryValueExA.*"AlwaysShowThunks"',
              'RegQueryValueExA.*"AlsoDebugProcChild"',
              'RegQueryValueExA.*"ShowCrashDialog"',

              # Visual Basic
              #	'"SOFTWARE\\\\\\\\Microsoft\\\\\\\\VBA\\\\\\\\Monitors",',
              # Delphi
              #	'"Software\\\\\\\\Borland\\\\\\\\Locales",',
              #	'"Software\\\\\\\\Borland\\\\\\\\Delphi\\\\\\\\Locales",',
              # AutoIt v3
              #	'"Software\\\\\\\\AutoIt v3\\\\\\\\AutoIt",',
              # .NET
              #	'"Software\\\\\\\\Novell\\\\\\\\Mono",',
              # WinRAR SFX
              #	'"Software\\\\\\\\WinRAR SFX\\\\\\\\",',
]
