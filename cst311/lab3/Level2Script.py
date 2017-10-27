#!/usr/bin/python
#MODIFIED BY bYRON nORREOD II
from mininet.net import Mininet
from mininet.node import Host, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info
def myNetwork():
	net = Mininet( topo=None,
			build=False,
			ipBase='0.0.0.0')
	info( '*** Adding controller\n' )
	info( '*** Add switches\n')	#leave it.
	router1 = net.addHost('router1', cls=Node, ip='192.168.1.1/24') #200.0.0.1/24' ) #declare
	router1.cmd('sysctl -w net.ipv4.ip_forward=1')   #use ip forwarding

	info( '*** Add hosts\n')
	h1 = net.addHost('h1', ip='192.168.1.100/24', defaultRoute='via=192.168.1.1/24') #200.0.0.1')
	h2 = net.addHost('h2', ip='172.16.0.100/12', defaultRoute='via=172.16.0.1/12')#240.0.0.1')
	
#	h1 = net.addHost('h1', cls=Host, ip='10.0.200.100/8', defaultRoute='via=10.0.2.1/8')
#	h2 = net.addHost('h2', cls=Host, ip='11.0.200.100/8', defaultRoute='via=11.0.2.1/8')
#	net.addLink(router1, h1, intfName2='router1_to_h1', params2={ 'ip' : '10.0.200.100/8'}) 
	#set router link in network 1
#	net.addLink(router1, h2, intfName2='router1_to_h2', arams2={ 'ip' : '11.0.200.100/8'})
	#set router link in network 2
	net.addLink(h1, router1, intfName2='h1_to_router1', params2={ 'ip' : '192.168.1.1/24'})#200.0.0.1/24'}) 
	#set link in net1 to router.params2
	net.addLink(h2, router1, intfName2='h2_to_router1', params2={ 'ip' : '172.16.0.1/12'})#240.0.0.1/24'}) 
	#set link in net2 to router.
	info( '*** Add links\n')
	net.addLink(h1, router1)#, intfName2='h1_to_router1', params2={ 'ip' : '10.0.0.1/8'}) 
	net.addLink(h2, router1)#, intfName2='h1_to_router1', params2={ 'ip' : '10.0.0.1/8'}) 
	
	info( '*** Starting network\n')
	net.build()

	CLI(net)
	net.stop()

if __name__ == '__main__':
	setLogLevel( 'info' )
	myNetwork()
