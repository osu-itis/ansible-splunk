# Ansible Playbook for Splunk
- **Authors**: OSU-SIG sig@oregonstate.edu
- **Description**:	Ansible Playbook for Splunk, forked from my2ndhead/ansible-playbook-splunk
- **Version**: 		1.0

[![Build Status](https://jenkins.sig.oregonstate.edu/job/lint%20ansible-splunk/badge/icon)](https://jenkins.sig.oregonstate.edu/job/lint%20ansible-splunk/)


# Instructions

* Clone group_vars from private repository.
* Create a hosts file from one of the provided templates.
* Always run install_splunk.yml playbook first.  download_splunk.yml is unnecessary if package downloaded already.
* Run remaining configure/install playbooks as needed.  Might want to do configure_firewall first.
* Make sure splunkd has been (re)started after configuring nodes.

## License
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

