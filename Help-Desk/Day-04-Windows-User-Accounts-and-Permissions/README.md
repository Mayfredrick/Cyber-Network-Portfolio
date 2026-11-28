# Week 15 – Day 4: Windows User Accounts and Permissions

## Ticket Information

- **Ticket ID:** HD-1504
- **Priority:** Normal
- **Category:** User Account and Access Troubleshooting
- **System:** Windows 11 Pro N for Workstations
- **Computer:** WIN-11-PC1
- **Status:** Diagnostic testing completed

## 1. Issue Reported

A user reported being unable to access a folder needed for work because Windows displayed a permissions error.

The objective was to inspect the Windows account, group memberships, and NTFS folder permissions.

## 2. User Account Inspection

PowerShell commands used:

```powershell
whoami
whoami /groups
```

Findings:

- Logged-in account: `WIN-11-PC1\dogos`
- Member of local Administrators group.
- Member of BUILTIN\Users.
- Member of Authenticated Users.
- High Mandatory Level was displayed.

## 3. Folder Permission Inspection

Created a test folder:

```powershell
New-Item -Path "C:\HelpDesk-Lab" -ItemType Directory
```

Inspected its permissions:

```powershell
Get-Acl "C:\HelpDesk-Lab" | Format-List
```

Additional inspection:

```powershell
(Get-Acl "C:\HelpDesk-Lab").Access |
Format-Table IdentityReference, FileSystemRights, AccessControlType, IsInherited -AutoSize
```

The folder permissions included:

| Account / Group | Permission |
|---|---|
| Administrators | Full Control |
| SYSTEM | Full Control |
| Users | Read and Execute |
| Authenticated Users | Modify |

The permission entries were marked as inherited.

## 4. Permission Verification

Used:

```powershell
icacls C:\HelpDesk-Lab
```

Observed permission flags included:

- `(I)` – Inherited
- `(OI)` – Object inherit
- `(CI)` – Container inherit
- `(IO)` – Inherit only
- `(F)` – Full Control
- `(M)` – Modify
- `(RX)` – Read and Execute

## 5. Access Testing

Created a test file:

```powershell
New-Item -Path "C:\HelpDesk-Lab\permission-test.txt" -ItemType File
```

**Result:** File created successfully.

Deleted the test file:

```powershell
Remove-Item "C:\HelpDesk-Lab\permission-test.txt"
```

**Result:** File deleted successfully.

## 6. Final Assessment

The current account successfully created and deleted a file in the test folder.

The observed permissions and test results confirm that the account had sufficient access for these operations.

The original access-denied issue was not reproduced because the actual work folder was not tested.

No account memberships or NTFS permissions were changed.

## 7. Skills Practiced

- Windows account identification
- Local group membership inspection
- NTFS permissions
- Access Control Lists (ACLs)
- Inherited permissions
- `Get-Acl`
- `icacls`
- PowerShell file operations
- Help Desk troubleshooting and documentation

## 8. Lab Takeaway

Before changing folder permissions, a Help Desk technician should identify the user account, inspect group membership, review the folder's ACL, and test actual access.

Permission changes should only be made when the evidence supports them.
