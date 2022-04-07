import sys
sys_args = sys.argv[1:]

from aws_credentials.main import run
run( *sys_args )

