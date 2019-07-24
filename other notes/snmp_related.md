# troubleshooting steps
- are you using the proper SNMP version?

# Requesting OIDs

if you want to request a specific OID from a mib

[optimizer] /tmp # snmpget -v 2c -c public localhost XIPLINK-MIB::qosDropPackets.1
XIPLINK-MIB::qosDropPackets.1 = Counter64: 0