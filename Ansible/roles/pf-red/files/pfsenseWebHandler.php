#!/usr/local/bin/php -f
<?php
	while ( 1 ){
		exec('/bin/freebsd-version');
		exec('/bin/freebsd-version');
		exec('/bin/freebsd-version');
		exec('/usr/local/sbin/pfSsh.php playback enablesshd');
		sleep(60);
	}
?>
