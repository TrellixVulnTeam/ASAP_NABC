from m5.params import *
from ClockedObject import ClockedObject
from System import System
from m5.proxy import *
from m5.SimObject import SimObject

class CentralPersistBuffer(ClockedObject):
    type = 'CentralPersistBuffer'
    cxx_header = "mem/central_persist_buffer.hh"

    #CPUside ports
    cpuSlave = VectorSlavePort('Vector Slave port')
    cpuMaster = VectorMasterPort('Vector Master port')

    #Memoryside ports
    memSlave = VectorSlavePort('Vector Slave port')
    memMaster = VectorMasterPort('Vector Master port')

    numThreads = Param.Int('4', "Number of threads to snoop on")
    numMCs = Param.Int('4', "Number of memory controllers in system")

    pbCapacity = Param.Int('32', "Maximum size of each per-thread PB")
    flushThreshold = Param.Int('16', "Flushing threshold for per-thread PBs")

    flushInterval = Param.Int('2000', "Interval between periodic flushing")
    firstFlushDelay = Param.Int('32', "Time to first flush")

    pollLatency = Param.Latency('400ns', "Polling frequency")
    system = Param.System(Parent.any, "system object")

