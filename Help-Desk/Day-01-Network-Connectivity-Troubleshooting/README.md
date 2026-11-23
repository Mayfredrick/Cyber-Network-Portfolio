# Day 01: Help Desk Network Connectivity Troubleshooting

## Lab Information

- Ticket ID: HD-1501
- Priority: Normal
- Category: Network Connectivity
- System: Windows 11 Workstation
- Network Environment: VMware Workstation – VMnet8 NAT

## Scenario

A user reported that their computer could not access the internet. The objective was to investigate network connectivity, identify possible causes, and document the findings.

## 1. Network Configuration

Collected network information using ipconfig /all.

| Setting | Observed Value |
|---|---|
| IPv4 Address | 192.168.114.11 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.114.2 |
| DNS Server | 192.168.114.2 |
| DHCP Server | 192.168.114.253 |
| DHCP | Enabled |
| Network Adapter | Intel(R) 82574L Gigabit Network Connection |

The workstation had an active DHCP lease.

- Lease obtained: November 23, 2026, 2:50:29 AM
- Lease expires: November 23, 2026, 3:50:30 AM

## 2. Connectivity Testing

### Default Gateway

Command:

ping 192.168.114.2

Result:
- 4 packets sent
- 4 packets received
- 0% packet loss

The workstation successfully communicated with its default gateway.

### External IP Connectivity

Command:

ping 8.8.8.8

Result:
- 4 packets sent
- 4 packets received
- 0% packet loss
- Average response time: 24 ms

External IP connectivity was successful.

## 3. DNS Investigation

### Test 1 – Default DNS Server

Command:

nslookup google.com

DNS server: 192.168.114.2

Observation:

The query repeatedly reported a two-second DNS request timeout before returning Google's IP addresses.

The same behavior occurred when testing microsoft.com.

### Test 2 – Google Public DNS

Changed the DNS server temporarily within the interactive nslookup session:

server 8.8.8.8

Then queried:

google.com

Result:

Google's DNS server successfully returned IPv4 and IPv6 addresses.

No permanent Windows DNS configuration change was made.

### Test 3 – PowerShell DNS Resolution

Command:

Resolve-DnsName google.com -Server 192.168.114.2

Result:

The command successfully returned DNS records, including A and AAAA records.

A second test was performed:

Resolve-DnsName google.com -Server 192.168.114.2 -DnsOnly -NoHostsFile

Result:

DNS records were successfully returned without an error in the supplied output.

### Test 4 – TCP Port 53

Command:

Test-NetConnection 192.168.114.2 -Port 53

Result:

TcpTestSucceeded: True

The workstation successfully established a TCP connection to port 53.

## 4. VMware Network Investigation

Reviewed the VMware Virtual Network Editor.

| Setting | Observed Value |
|---|---|
| Virtual Network | VMnet8 |
| Network Type | NAT |
| Subnet | 192.168.114.0 |
| Subnet Mask | 255.255.255.0 |
| NAT Gateway | 192.168.114.2 |
| DHCP Range | 192.168.114.1 – 192.168.114.253 |
| Local DHCP Service | Enabled |

The VMware DHCP and NAT services were both running.

A controlled test changed the VMware DNS timeout setting from 2 seconds to 5 seconds. The subsequent nslookup test continued to report a two-second timeout.

The original setting was restored to 2 seconds.

## 5. Additional Troubleshooting

The following checks were performed:

- DHCP server ping: No response; 100% packet loss.
- ARP table: An entry for 192.168.114.253 was present.
- Windows DNS Client service: Running.
- VMware DHCP Service: Running.
- VMware NAT Service: Running.

The failed DHCP server ping does not establish that the DHCP service was unavailable.

## 6. Findings and Conclusion

The workstation successfully communicated with its default gateway and an external IP address.

DNS resolution was successful through both the VMware NAT gateway and Google Public DNS.

However, DNS queries through 192.168.114.2 repeatedly produced a two-second timeout in nslookup before returning results. PowerShell DNS resolution through the same server completed successfully.

Changing the VMware DNS timeout setting did not resolve the nslookup behavior.

Final assessment: Internet connectivity was working during testing. A recurring DNS diagnostic timeout was observed, but its root cause was not confirmed.

No permanent network configuration changes were made.

## 7. Skills Practiced

- Windows IP configuration review
- DHCP lease investigation
- Default gateway connectivity testing
- External network connectivity testing
- DNS troubleshooting
- TCP port testing
- VMware NAT network inspection
- Windows service verification
- Help desk ticket documentation
- Evidence-based troubleshooting

## 8. Lessons Learned

A failed diagnostic test does not automatically mean a service is broken.

Successful connectivity tests, repeated observations, and accurate documentation help narrow down problems without making unnecessary configuration changes.
