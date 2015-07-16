#!/usr/bin/env python
from hetzner.robot import Robot
import datetime
import sys

sys.argv
server_ip=str(sys.argv[1])

def main(ip):
    robot = Robot("LOGIN", "PASSWORD")
    server = robot.servers.get(ip)
    now = datetime.datetime.now()
    first_day = now.strftime("%Y-%m-01")
    last_day = now.strftime("%Y-%m-31")
    traffic = server.conn.post('/traffic', {"type":"month", "from": first_day, "to": last_day, "ip": ip})
    print traffic['traffic']['data'][ip]['out']

if __name__ == '__main__':
    main(server_ip)
