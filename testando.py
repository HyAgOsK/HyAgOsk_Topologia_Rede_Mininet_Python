from mininet.topo import Topo

class MyTopo( Topo ):
    "2 host 3 switch 4 host custom topology"

    def init( self ):
        "Create custom topo."

        # Initialize topology
        Topo.init( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        leftHost2 = self.addHost('h2')
        centerHost3 = self.addHost('h3')
        centerHost4 = self.addHost('h4')
        rightHost5 = self.addHost( 'h5' )
        rightHost6 = self.addHost( 'h6' )
        leftSwitch = self.addSwitch( 's1' )
        centerSwitch = self.addSwitch( 's2' )
        rightSwitch = self.addSwitch( 's3' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftHost2, leftSwitch )
        self.addLink( leftSwitch, centerSwitch )
        self.addLink( centerHost3, centerSwitch )
        self.addLink( centerHost4, centerSwitch )
        self.addLink( centerSwitch, rightSwitch )
        self.addLink( rightHost5, rightSwitch )
        self.addLink( rightHost6, rightSwitch )

topos = { 'mytopo': ( lambda: MyTopo() ) }
