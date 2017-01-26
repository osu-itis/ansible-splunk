# Ansible Playbook for Splunk
- **Authors**: OSU-SIG sig@oregonstate.edu
- **Description**:	Ansible Playbook for Splunk, forked from my2ndhead/ansible-playbook-splunk
- **Version**: 		1.0

[![Build Status](https://jenkins.sig.oregonstate.edu/job/lint%20ansible-splunk/badge/icon)](https://jenkins.sig.oregonstate.edu/job/lint%20ansible-splunk/)


# Instructions

* clone group_vars from private repository
```
 - install_splunk.yml
 - configure_licensemaster.yml
 - configure_peernode.yml
 - ansible peernode -i ../inventory/splunk -a "/opt/splunk/bin/splunk start" -u splunk
 - configure_masternode.yml
 - configure_deployer.yml
 - install_shcmember.yml
 - configure_shcmember.yml
 - configure_dmc.yml
 - ansible all -i ../inventory/splunk -a "/opt/splunk/bin/splunk restart" -u splunk
```
# SSL WARNING!

- If you specify sslKeysFilePassword these playbooks WILL NOT create the matching server.pem and THINGS WILL NOT WORK PROPERLY.  You MUST invoke splunk's `createssl server-cert` by hand on each node and feed it the proper password!

# Heavy Forwarder with keepalived

* The configure_hf_ha.yml playbook should be used with configure_heavyforwarder.yml to keep HF configurations in sync.  Playbook does NOT keep app-specific configs in sync, so additional playbooks may need to be applied in order to keep matched heavy forwarders in a failover pair!

## License
- ** The keepalived role is from https://github.com/tcomerma/ansible-keepalived and it is licensed under the Apache license - see LICENSE-keepalived.md for details.
- **This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.** [1]
- **Commercial Use, Excerpt from CC BY-NC-SA 4.0:**
  - "A commercial use is one primarily intended for commercial advantage or monetary compensation."
- **In case of Ansible Playbook for Splunk this translates to:**
  - You may use Ansible Playbook for Splunk in commercial environments for setting up Splunk environments
  - You may use Ansible Playbook for Splunk as part of your consulting or integration work, if you're considered to be working on behalf of your customer. The customer will be the licensee of Ansible Splunk Playbook and must comply according to the license terms
  - You are not allowed to sell Ansible Playbook for Splunk as a standalone product or within an application bundle
  - If you want to use Ansible Playbook for Splunk outside of these license terms, please contact us and we will find a solution

## References
[1] http://creativecommons.org/licenses/by-nc-sa/4.0/

