Title:<u>Vlans Configuration</u>

<u>Overview:</u>

This project showcasing the configuration of vlans and as well as setting the sub interfaces on the router.It will also show the steps taken to set the Ip addresses on the Pcs.

<u>**Tools Used**:</u>

In this lab I used the GNS3 lab simulation.It includes 4pcs , a switch and a router c3725.

<u>**Steps taken:**</u>

1.Designed the topology to use in this lab.

2.Setting 2pcs on the Sales vlan and 2pcs on HR vlan.

3.configure the ip addresses for vlan 1 with 1.1.1.1 and 1.1.1.2 with deefault gateway of 1.1.1.3 all with /24 mask.Then for vlan 2 i used 2.2.2.2 and 2.2.2.3 with default gateway of 2.2.2.1 all with /24 mask.

4.Set up switch to have 2 access ports for pcs and 1 trunk port for a port connected to a router.

5.Configure a router sub interfaces with dot1q and ip addresses so that the pcs from different vlans can be able to communicate.

<u>**Results:**</u>

1.After configure the switch for sales and Hr vlan the 4 pcs where able to ping each other based on their specific vlan.

2.After configuring router on a stick ip addresses, the pcs were able to ping each other regardless of their vlans.That is to say pc1 on vlan sales with ip address 1.1.1.1 could be able to ping pc2 on vlan Hr with ip 2.2.2.2.
