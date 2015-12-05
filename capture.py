from time import mktime
import io
from compoundpi.client import CompoundPiClient

with CompoundPiClient() as client:
    client.servers.network = '192.168.43.1/24'
    client.servers.find(1)
    client.framerate(90)
    client.servers.output = "/home/manan/Desktop/captures"
    for cap in xrange(1,16):
    	client.capture()

    try:
        for addr, files in client.list().items():
            for f in files:
                assert f.filetype == 'IMAGE'
                print('Downloading from %s' % addr)
                with io.open('%s-%d-%d.jpg' % (addr, f.index, mktime(f.timestamp.timetuple())), 'wb') as output:
                    client.download(addr, f.index, output)
    finally:
        client.clear()
