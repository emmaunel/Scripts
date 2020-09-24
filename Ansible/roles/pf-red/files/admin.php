#!/usr/local/bin/php -f
<?php
        require_once("config.inc");
        require("auth.inc");
        require_once("functions.inc");
        require_once("shaper.inc");
 
        $config['system']['webqui']['authmode']= "Local Database";
        $admin_user =& getUserEntryByUID(0);
        if (!$admin_user) {
                $admin_user = array();
                $admin_user['uid'] = 0;
                if (!is_array($config['system']['user'])){
                        $config['system']['user'] = array();
                }
                $config['system']['user'][] = $admin_user;
        }

        $admin_user['name'] = "admin";
        $admin_user['scope'] = "system";
        $admin_user['priv'] = array("user-shell-access");

        if (isset($admin_user['disabled'])){
                unset($admin_user['disabled']);
        }
 
        local_user_set_password($admin_user, "changeme");
        local_user_set($admin_user);
?>
