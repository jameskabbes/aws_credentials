import sys
sys_args = sys.argv[1:]

from aws_credentials.aws_credentials import run
run( *sys_args )

