# http://sebastiandahlgren.se/2012/10/11/using-paramiko-to-send-ssh-commands/
import sys
import time
import select
import paramiko

host = 'yardstick'
i = 1

#
# Try to connect to the host.
# Retry a few times if it fails.
#
while True:
    print "Trying to connect to %s (%i/30)" % (host, i)

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host)
        print "Connected to %s" % host
        break
    except paramiko.AuthenticationException:
        print "Authentication failed when connecting to %s" % host
        sys.exit(1)
    except:
        print "Could not SSH to %s, waiting for it to start" % host
        i += 1
        time.sleep(2)

    # If we could not connect within time limit
    if i == 30:
        print "Could not connect to %s. Giving up" % host
        sys.exit(1)

# Send the command (non-blocking)
stdin, stdout, stderr = ssh.exec_command("""
    while true; do
        echo 'hello'
        sleep 1
    done
    """)
stdin, stdout, stderr = ssh.exec_command("""
        export OS_PASSWORD=console
        export OS_TENANT_NAME=admin
        export OS_AUTH_URL=http://172.17.1.222:35357/v2.0
        export OS_USERNAME=admin; export OS_VOLUME_API_VERSION=2; 
        export EXTERNAL_NETWORK=ext-net; 
        yardstick -d task start /home/opnfv/repos/yardstick/samples/ping.yaml  2>&1
    """)

# Wait for the command to terminate
while not stdout.channel.exit_status_ready():
    # Only print data if there is data to read in the channel
    if stdout.channel.recv_ready():
        rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
        if len(rl) > 0:
            # Print data from stdout
            print stdout.channel.recv(1024),

#
# Disconnect from the host
#
print "Command done, closing SSH connection"
ssh.close()
