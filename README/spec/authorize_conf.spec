# authorize.conf spec
#
#

user_roles:
  <role name>:
    <role key>: <role value>

  * role name will create the [role_<role name>] stanza in authorize.conf,
    with the key/values specified. This is used for restricting what certain
    users/groups can do.  See Splunk documentation on authorize.conf for more
    details:
    http://docs.splunk.com/Documentation/Splunk/latest/Admin/authorizeconf
