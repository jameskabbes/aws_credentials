import kabbes_client
import aws_credentials

class Client( kabbes_client.Client ):

    _CONFIG = {
        "_Dir": aws_credentials._Dir
    }

    def __init__( self, *args, **kwargs ):
        kabbes_client.Client.__init__( self, *args, **kwargs)

        if not self.cfg.access_keys.Path.exists():
            self.cfg.access_keys.Path.write( string ='{}' )

        self.cfg.print_atts()

        self.Creds = aws_credentials.AWS_Creds( self )

