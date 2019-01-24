import argparse
from mcstatus import MinecraftServer
from multiprocessing import Pool
import time
import socket
parser = argparse.ArgumentParser()
parser.add_argument('startip', type=str, help='The IP(s) to begin the search from. Interval with a comma and no spaces.')
parser.add_argument('--pnum', type=int, help='Number of processes', default=None)
parser.add_argument('--depth', type=int, help='Depth of IP scan', default="1")
parser.add_argument('mcversion', type=str, help='The version(s) to search for. Interval with a comma and no spaces.')
parser.add_argument('--minp', type=int, help='Minimum amount of players atm', default="0")
parser.add_argument('--maxp', type=int, help='Maximum amount of players atm', default="1000")
args = parser.parse_args()
if args.depth > 2 or 1 > args.depth:
    raise argparse.ArgumentTypeError('Depth has to be between 1 and 2')
mcversion = args.mcversion.split(",")
def listgenerator(ip, level):
    iplist = []
    ips = ip.split(",")
    for ip in ips:
        ip = socket.gethostbyname(ip)
        split = ip.split(".")
        if level == 1:
            for i in range(255):
                iplist.append(".".join(split[:3])+"."+str(i))
        elif level == 2:
            for i in range(255):
                iplist.append(".".join(split[:2])+"."+str(i)+"."+split[3])
            length = iplist
            for x in length:
                for i in range(255):
                    split = x.split(".")
                    iplist.append(".".join(split[:3])+"."+str(i))
    return iplist
def serverfinder(x):
    server = MinecraftServer.lookup(x)
    try:
        query = server.query()
        status = server.status()
    except:
        return
    if query.software.version in mcversion and query.software.brand == "vanilla" and args.maxp >= query.players.online >= args.minp and "modinfo" not in status.raw:
        print ("Hit! :{}".format(x))
        return x
    
if __name__ == '__main__':
    p = Pool(args.pnum)
    iplist = listgenerator(args.startip, args.depth)
    t1 = time.time()
    print ("Performing scan on IP {} with depth {} on {} processes.".format(args.startip, args.depth, args.pnum))
    results = p.map(serverfinder, iplist)
    p.close()
    p.terminate()
    results = list(filter(None, results))
    with open('results.txt', 'w') as f:
        for item in results:
            f.write("%s\n" % item)
    print("Job done!, took {}".format(time.time()-t1))
