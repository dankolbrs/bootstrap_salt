bootstrap_salt
=========

Role to bootstrap salt install for various Operating systems

Requirements
------------

Tested on FreeBSD, but may require specific additions to work with Ansible from a default install, such as `sudo`

Role Variables
--------------

`salt_master` used to bootstrap salt-master to connect to. Expects further configuration to be complete by salt states


Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: bootstrap_salt, salt_master: 'salt.example.com' }

License
-------

BSD

Author Information
------------------

Dan Kolb    
github@dankolb.net    
2017    