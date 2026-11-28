# Week 15 – Day 5: Windows Updates and Device Manager

## Ticket Information

- **Ticket ID:** HD-1505
- **Priority:** Normal
- **Category:** Windows System Maintenance
- **Computer:** WIN-11-PC1
- **Status:** Diagnostic inspection completed

## 1. Issue Reported

A user reported inconsistent computer performance and wanted to know whether Windows needed updates or whether hardware devices were reporting problems.

The objective was to inspect Windows Update, Device Manager, system information, and protected Windows system files.

## 2. Windows Update Service

PowerShell command:

```powershell
Get-Service wuauserv | Select-Object Name, Status, StartType
```

Observed results:

- Service: wuauserv
- Status: Stopped
- Startup type: Manual

The service was inspected but not modified.

## 3. Installed Updates

Command used:

```powershell
Get-HotFix |
Sort-Object InstalledOn -Descending |
Select-Object -First 10 HotFixID, Description, InstalledOn
```

Seven update records were returned:

| HotFix ID | Description | Installed |
|---|---|---|
| KB5132057 | Update | 11/26/2026 |
| KB5132056 | Update | 11/26/2026 |
| KB5132688 | Security Update | 11/23/2026 |
| KB5127694 | Update | 10/16/2026 |
| KB5121794 | Update | 10/16/2026 |
| KB5128942 | Update | 10/13/2026 |
| KB5054156 | Update | 10/13/2026 |

These results show installed update records. Pending updates were not checked.

## 4. Device Manager Inspection

Device Manager was opened and visually inspected.

Observations:
- No yellow warning triangles observed.
- No red X symbols observed.
- No obvious device errors displayed.

This was a visual inspection, not a complete hardware diagnostic.

## 5. Windows System Information

The initial PowerShell output reported Windows 10. The edition and version were subsequently checked using `winver`.

Verified information:

- Edition: Windows 11 Pro N
- Version: 26H2
- OS build: 26300.10075
- Architecture: 64-bit

## 6. Windows System File Verification

Command used:

```powershell
sfc /verifyonly
```

Result:

`Windows Resource Protection did not find any integrity violations.`

The verification completed at 100%.

No repairs were performed.

## 7. Final Assessment

The inspection identified installed Windows updates, no visible Device Manager warnings, and no protected system-file integrity violations.

The Windows Update service was stopped with Manual startup, but this alone does not establish a problem.

The checks did not identify a confirmed cause of the reported inconsistent performance.

No updates, drivers, services, or system settings were changed.

## 8. Skills Practiced

- Windows Update service inspection
- Installed update history
- Device Manager troubleshooting
- Windows edition and build verification
- PowerShell system information
- System File Checker (`sfc /verifyonly`)
- Basic Windows maintenance
- Help Desk ticket documentation

## 9. Lab Takeaway

A Help Desk technician should inspect update history, device status, and system integrity before recommending maintenance or making changes. Findings should be documented accurately, including what was not tested.
