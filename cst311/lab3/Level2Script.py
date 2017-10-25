#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Host, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info
def myNetwork():
	net = Mininet( topo=None,
			build=False,
			ipBase='192.168.0.0/16')
	info( '*** Adding controller\n' )

	info( '*** Add switches\n')	#leave it.

	r1 = net.addHost('r1', cls=Node, ip='0.0.0.0')#, defaultRoute=None) #0.0.0.0 - wildcard. config it.

	r1.cmd('sysctl -w net.ipv4.ip_forward=1')   #use ip forwarding

	info( '*** Add hosts\n')
	h1 = net.addHost('h1', cls=Host, ip='192.168.0.1', defaultRoute=None)
	h2 = net.addHost('h2', cls=Host, ip='192.168.0.2', defaultRoute=None)

	info( '*** Add links\n')
	net.addLink(h1, r1)	#create links
	net.addLink(h2, r1)	#create links

	info( '*** Starting network\n')
	net.build()
	CLI(net)
	net.stop()
if __name__ == '__main__':
	setLogLevel( 'info' )
	myNetwork()
