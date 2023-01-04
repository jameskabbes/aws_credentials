import aws_credentials
import time

if aws_credentials.client.Creds.update_from_clipboard():
    time.sleep( aws_credentials.client.cfg.get_attr('SLEEP_SUCCESS', use_ref=True) )
else:
    time.sleep( aws_credentials.client.cfg.get_attr('SLEEP_FAILURE', use_ref=True) )

