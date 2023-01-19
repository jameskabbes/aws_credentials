import dir_ops as do
import os

_Dir = do.Dir( os.path.abspath( __file__ ) ).ascend()   #Dir that contains the package 

from .AWS_Creds import AWS_Creds
from .Client import Client

client = Client()
