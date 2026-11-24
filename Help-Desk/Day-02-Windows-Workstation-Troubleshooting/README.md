# Week 15 – Day 2: Windows Workstation Performance Troubleshooting

## Lab Information

- **Ticket ID:** HD-1502
- **Priority:** Normal
- **Category:** Windows Performance
- **Operating System:** Windows 11
- **Lab Type:** Help Desk / IT Support

## 1. Scenario

A user reported that their Windows workstation had become slow. Applications took a long time to open, and the computer occasionally froze.

The objective was to investigate system resource utilization, identify possible causes, and document findings before making changes.

## 2. CPU Investigation

Opened Task Manager and navigated to Performance → CPU.

**Observation:**
- CPU utilization: 8%

CPU usage was relatively low at the time of testing. No unusually high CPU utilization was observed.

## 3. Memory Investigation

Navigated to Task Manager → Performance → Memory.

**Observations:**
- Installed RAM: 4 GB
- Memory utilization: 70%
- Available memory: 1.5 GB
- Committed memory: 3.0 / 4.8 GB

The workstation had 4 GB of installed RAM. This limited capacity could contribute to performance problems when multiple applications are running.

### Top Memory-Using Processes

Reviewed Task Manager's Processes tab and sorted applications by memory usage.

| Process | Memory Usage |
|---|---:|
| jetbrains-toolbox.exe | 254,364 KB |
| MsMpEng.exe | 98,296 KB |
| explorer.exe | 79,180 KB |

JetBrains Toolbox was the largest memory consumer among the three processes reviewed.

## 4. Disk Investigation

Navigated to Task Manager → Performance → Disk 0 (C:).

**Observation:**
- Disk active time: 0%

Disk activity was idle at the time of measurement. No unusually high disk utilization was observed during this check.

## 5. Startup Application Investigation

Opened Task Manager → Startup apps.

**Observation:**
- OneDrive showed High startup impact.

Opened OneDrive to review its synchronization status.

**Result:**
- OneDrive status: Backed up and synced.

OneDrive was not reporting an active synchronization problem during the investigation. Its startup impact alone does not establish that it caused the reported slowdown.

## 6. Virtual Memory Investigation

Opened Windows System Properties and navigated to:

Advanced → Performance Settings → Advanced → Virtual Memory.

**Observation:**
- Automatically manage paging file size for all drives: Enabled.

Windows was configured to manage the paging file automatically. No virtual memory settings were changed.

## 7. Troubleshooting Summary

| Component | Finding |
|---|---|
| CPU | 8% utilization |
| Installed RAM | 4 GB |
| Memory utilization | 70% |
| Available memory | 1.5 GB |
| Committed memory | 3.0 / 4.8 GB |
| Disk active time | 0% |
| Largest reviewed memory consumer | JetBrains Toolbox |
| OneDrive startup impact | High |
| OneDrive synchronization | Backed up and synced |
| Paging file | Automatically managed |

## 8. Technician Assessment

The workstation has 4 GB of RAM, which may be a limiting factor when running multiple applications.

JetBrains Toolbox was the largest memory consumer among the three processes reviewed. However, the available evidence does not establish that this application caused the performance problem.

CPU and disk utilization were low during the checks. OneDrive reported that its files were backed up and synced, and Windows was managing virtual memory automatically.

**Conclusion:** Limited RAM capacity is a possible contributing factor, but the root cause of the reported slow performance was not confirmed.

### Recommended Next Actions

1. Monitor memory utilization when the slowdown occurs.
2. Review running applications during periods of poor performance.
3. Check whether memory usage increases significantly when multiple applications are open.
4. Consider a RAM upgrade if supported by the workstation hardware and justified by its workload.

No applications were disabled, no system settings were changed, and no hardware upgrades were performed.

## 9. Skills Practiced

- Windows Task Manager
- CPU and memory utilization analysis
- Disk performance monitoring
- Process identification
- Startup application review
- Windows virtual memory configuration
- Basic performance troubleshooting
- Help desk ticket documentation
- Evidence-based problem investigation

## 10. Knowledge Check

**Question:** A workstation has low CPU utilization, moderate memory utilization, and low disk activity. What should a technician do next?

**Correct Answer: B – Monitor memory usage during the slowdown and identify resource-heavy applications.**

The technician should collect additional evidence before making system changes or recommending hardware replacement.

## 11. What I Learned

This exercise provided practical experience investigating Windows performance issues using Task Manager and System Properties.

I learned to review CPU, memory, disk, startup applications, and virtual memory settings before deciding what might be contributing to a performance problem.

An important part of troubleshooting is distinguishing between an observed condition and a confirmed root cause.
