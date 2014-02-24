import time
import os

from scapy.all import Ether, ARP, srp, conf

from core.modules.base import BaseModule
from options import *

__module__ = "Arping"

class Arping(BaseModule):
    def initialize(self):
        self.update_info({
                          'name'    :   'Arping',
                          'description' :   'Simple module to send out an ' +
                                            'ARP broadcast packet and print' +
                                            'The responses.',
                          'license'  :  'BSD',
                          'authors'  :  ['ganye',]
                          })
        self.set_options({
                          'network' : IPAddress(True, 'Network to broadcast on.',),
                          })
        
    def run(self):
        conf.verb = 0
        self.console.info("sending arping...")
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/
                         ARP(pdst=self.network.value), timeout=2)
        
        self.console.info("done")
        
        for snd, rcv in ans:
            self.console.writeln(rcv.sprintf("%Ether.src%\t%ARP.psrc%"))