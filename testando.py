from mininet.topo import Topo

class MyTopo( Topo ):
    "2 host 3 switch 4 host custom topology"

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        leftHost1a = self.addHost('h1a')
        centerHost2 = self.addHost('h2')
        centerHost2a = self.addHost('h2a')
        rightHost = self.addHost( 'h3' )
        rightHost3a = self.addHost( 'h3a' )
        leftSwitch = self.addSwitch( 's1' )
        centerSwitch = self.addSwitch( 's2' )
        rightSwitch = self.addSwitch( 's3' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftHost1a, leftSwitch )
        self.addLink( leftSwitch, centerSwitch )
        self.addLink( centerHost2, centerSwitch )
        self.addLink( centerHost2a, centerSwitch )
        self.addLink( centerSwitch, rightSwitch )
        self.addLink( rightHost, rightSwitch )
        self.addLink( rightHost3a, rightSwitch )

topos = { 'mytopo': ( lambda: MyTopo() ) }
