# Week 15 – Day 3: Windows Troubleshooting and System Diagnostics

## Ticket Information

- **Ticket ID:** HD-1503
- **Priority:** Normal
- **Category:** Windows System Diagnostics
- **System:** Windows 11 Pro N for Workstations
- **Computer:** WIN-11-PC1
- **Status:** Diagnostic review completed; root cause not confirmed

## 1. Issue Reported

The user reported that some applications occasionally stop responding and wanted to know whether Windows had recorded related errors.

The goal was to review Windows Application and System logs, identify relevant events, and document the findings without making unnecessary system changes.

## 2. Application Log Findings

### Security-SPP – Event ID 8198

- **Source:** Microsoft-Windows-Security-SPP
- **Level:** Error
- **Description:** License activation failed.
- **Error code:** `0x8007232B`
- **Action:** AutoActivate
- **Trigger:** NetworkAvailable

Additional checks:

- `slmgr /dlv` showed the Windows licensing channel as `VOLUME_KMSCLIENT`.
- License status showed `Notification`.
- An SRV lookup for `_vlmcs._tcp` did not return a KMS service record.

**Observation:** Windows activation was unsuccessful. The available evidence does not establish whether this is related to the reported application behavior.

## 3. System Log Findings

### Downloaded Maps Manager – Event ID 7023

- **Service:** MapsBroker
- **Status:** Stopped
- **Startup type:** Automatic
- **Error:** The request is not supported.

### Windows Camera Frame Server Monitor – Event ID 7023

- **Service:** FrameServerMonitor
- **Status:** Stopped
- **Startup type:** Manual
- **Error:** The specified module could not be found.

### Windows Camera Frame Server

- **Service:** FrameServer
- **Status:** Stopped
- **Startup type:** Manual

The two camera-related services were configured for manual startup. Their stopped status alone does not establish a service failure.

### Event Review

The 10 most recent System Event ID 7023 records included:
- 3 MapsBroker events
- 5 Windows Camera Frame Server Monitor events
- 2 Microsoft Usage and Quality Insights events

Some records reported that a system shutdown was in progress.

## 4. Application Crash and Hang Checks

PowerShell queries were used to check the VM's Application log:

| Event ID | Description | Result |
|---|---|---|
| 1000 | Application Error | No matching events found |
| 1002 | Application Hang | No matching events found |

The host computer's Event ID 1000 was excluded because the ticket concerns the Windows 11 virtual machine.

## 5. Troubleshooting Performed

- Reviewed Windows Application event logs.
- Reviewed Windows System event logs.
- Examined Event ID 8198 and Event ID 7023.
- Checked Windows activation and licensing information.
- Checked the KMS DNS SRV record.
- Checked the status and startup types of Windows services.
- Searched for Application Error and Application Hang events.

## 6. Assessment

Windows recorded activation and service-related errors. However, the Application log checks did not return matching Event ID 1000 or 1002 records.

The available evidence does not confirm the cause of the reported application unresponsiveness. No direct connection between the recorded service errors, activation failure, and application behavior was established.

## 7. Resolution and Recommendations

**Resolution:** No confirmed root cause or fix identified.

Recommended follow-up:
- Record the application name and time whenever the issue occurs.
- Check whether the issue affects one application or multiple applications.
- Review relevant event logs immediately after another occurrence.
- Investigate Windows activation separately if the system is expected to use a valid organizational KMS license.

No service startup settings, licensing settings, or other system configurations were changed during this diagnostic exercise.

## 8. Skills Practiced

- Windows Event Viewer
- PowerShell event log filtering with `Get-WinEvent`
- Windows service inspection with `Get-Service`
- Service configuration inspection with `sc.exe qc`
- Windows activation diagnostics with `slmgr`
- DNS SRV record lookup with `nslookup`
- Evidence-based troubleshooting and documentation

---

**Lab takeaway:** Windows troubleshooting involves collecting evidence before making changes. An error recorded in Event Viewer does not automatically identify the cause of a user's reported problem.
