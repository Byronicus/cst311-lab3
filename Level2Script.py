#!/usr/bin/python
#MODIFIED BY bYRON nORREOD II
from mininet.net import Mininet
from mininet.node import Host, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info
def myNetwork():
	net = Mininet( topo=None,
			build=False,
			ipBase='190.0.0.1/24')
	info( '*** Adding controller\n' )
	info( '*** Add switches\n')	
	#leave it.
	
	r1 = net.addHost('r1', cls=Node, ip='190.0.0.1/24') #declare
	r1.cmd('sysctl -w net.ipv4.ip_forward=1')   #use ip forwarding -> makes router forward all traffic to all other nodes. Linux command.

	info( '*** Add hosts\n')
	h1 = net.addHost('h1', cls=Host, ip='190.0.0.2/24', defaultRoute='via 190.0.0.1')
	h2 = net.addHost('h2', cls=Host, ip='140.0.0.2/24', defaultRoute='via 140.0.0.1')
	
#	h1 = net.addHost('h1', cls=Host, ip='200.0.200.100/24', defaultRoute='via=200.0.0.1/8')
#	h2 = net.addHost('h2', cls=Host, ip='11.0.200.100/8', defaultRoute='via=11.0.2.1/8')

	info( '*** Add links\n')
	net.addLink(h1, r1, intfName2='h1-eth0', params2={ 'ip' : '190.0.0.1/24'}) 
	net.addLink(h2, r1, intfName2='h2-eth0', params2={ 'ip' : '140.0.0.1/24'}) 

#	net.addLink(router1, h1, intfName2='router1_to_h1', params2={ 'ip' : '200.0.200.100/24'}) 
	#set router link in network 1
#	net.addLink(router1, h2, intfName2='router1_to_h2', params2={ 'ip' : '240.0.200.100/16'})
	#set router link in network 2

	#original:
#	net.addLink(h1, router1)#, intfName2='h1_to_router1', params2={ 'ip' : '10.0.0.1/8'}) 
#	net.addLink(h2, router1)#, intfName2='h1_to_router1', params2={ 'ip' : '10.0.0.1/8'}) 
	
	info( '*** Starting network\n')
	net.build()

	CLI(net)
	net.stop()

if __name__ == '__main__':
	setLogLevel( 'info' )
	myNetwork()
