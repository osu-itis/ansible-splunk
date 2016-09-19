# Apache vhost configuration spec
#
# This is highly tailored to OSU's use case: a 3rd party load balancer and
# mod_auth_cas (which is terrible for LB apps, fyi) running an auth front-
# end on each Splunk search head.  Only used on shcmember host group.

httpd:
  cas_login_url: <url>
  * CAS login URL... if you don't know what this is, you shouldn't be here

  cas_validate_url: <url>

  server_name: <hostname>
  * ServerName variable in the Apache vhost

  * SEE ALSO: web_conf.spec!
