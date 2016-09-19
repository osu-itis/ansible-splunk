# Splunk firewall settings
#
# put in group_vars/all/splunk_fw.yml (or anywhere in group_vars/all/)

splunk_fw:
  management_allow:
  - <IP or CIDR>
  * IPs that can reach the management ports (8000,22)

  lb_snip:
  - <IP>
  * Subnet IP for load balancer (used on shcmembers only)

  lm_allow:
  - <IP>
  * Which IPs can talk to the license master

  forwarder_allow:
  - <IP or CIDR>
  * Which IPs that can reach the forwarders on any port/proto


