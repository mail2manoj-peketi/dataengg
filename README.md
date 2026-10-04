DAY 3 Assignment Scenario : 
============================
**Each server contains : **
Hostname
Environment (PROD/UAT)
Status (UP/DOWN)
CPU usage
Disk usage
============================================================
**Tasks : **  
_Filter records_
1. Find servers with CPU ≥ 80%.
2. Find servers with disk usage ≥ 80%.
3. Find all PROD servers.
4. Find critical PROD servers based on CPU/disk thresholds.
_Calculate values_
a. Total, UP, and DOWN servers.
b. Average CPU usage.
c. Average disk usage.
d. Server with highest CPU usage.
e. Server with highest disk usage.
f. CRITICAL: server DOWN, CPU ≥ 90%, or disk ≥ 90%.
============================================================
**Health check Summary for every server**
DOWN     - Immediate attention   : If server is in down state
CRITICAL - Needs attention       : CPU ≥ 90% or disk ≥ 90%.
WARNING  - Check and take action : CPU ≥ 70% or disk ≥ 80%.
HEALTHY: otherwise.
