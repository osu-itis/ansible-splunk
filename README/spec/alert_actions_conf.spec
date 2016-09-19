# alert_actions.conf spec
#
# Useful for making alert emails/messages have proper user-facing URLs in them

splunk_alert_actions:
  default:
    hostname: https://search.splunk.example.com
    * Set to the hostname/base URL that users will use to hit search head(s)
