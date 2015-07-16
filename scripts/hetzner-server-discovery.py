#!/usr/bin/env python
from hetzner.robot import Robot
import json

def main():
    robot = Robot("LOGIN", "PASSWORD")
    ip = list(robot.servers)
    data = list()
    for item in ip:
        if item:
            data.append({"{#SERVER}": item.ip, "{#ORDER}": item.number, "{#NAME}": item.name})
    print(json.dumps({"data": data}, indent=4))

if __name__ == '__main__':
    main()
