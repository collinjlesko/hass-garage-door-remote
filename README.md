hass-garage-door-remote

Based on https://github.com/andrewshilliday/garage-door-controller

Installation:

1. Create configuration in configuration.yaml (use commandforswitch.txt)
2. Input your user and host.
3. Copy remotegarage.py to remote garage door controller (remote pi) [adjust pins if necessary]
4. Copy RSA keys created using below to /config (they will probably default to /root/.ssh): 

	ssh-keygen -t rsa # ENTER to every field
	ssh-copy-id myname@somehost

5. Touch ssh_config in /config with this text:

	 /config/ssh_config should contain:
	 
		Host *
			StrictHostKeyChecking no
	
6. CHMOD for execution

	Make sure to chmod 400 your RSA keys for instant ssh auth.
	"chmod 400 /config/ssh_config /config/id_rsa"
	
7. Toggle switch in Hass

Credit: https://community.home-assistant.io/t/error-when-executing-ssh-command-using-command-line-switch/26425

