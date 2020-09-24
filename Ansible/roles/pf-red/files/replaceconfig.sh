#!/bin/sh
while [ 1 ]; do
	cp /cf/conf/config.bkg /cf/conf/config.xml
	rm /tmp/config.cache
	/etc/rc.reload_all
	/usr/local/sbin/pfSsh.php playback redteam
	sleep 10800
done
