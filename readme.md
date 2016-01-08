STEPS TO SET UP INITIAL RAFT NODE CLUSTER (3 NODES)

 i) In the customize services step, create a separate configuration file for each of the three nodes using “manage configs” option.

 

ii) Create a separate configuration group for each of the three nodes as shown below below.



iii) Assign a node to each of the configuration groups from the right hand side panel.



iv) Once done , select a configuration file from the manage configs  drop down and update the hostname field  to actual hostname/IP address of the node
to which that config is signed.



v)For the first second node configuration file set INFLUXD_OPTS="-join hostname1:port1"



vi) Similarly for the third node configuration file  file set INFLUXD_OPTS="-join hostname1:port1,hostname2:port2” 

vii) click next and deploy.



MORE INFO:
 Refer to Influxdb clustering documentation for more details
 	https://influxdb.com/docs/v0.9/guides/clustering.html


