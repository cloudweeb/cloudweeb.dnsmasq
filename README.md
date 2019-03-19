Ansible Role Dnsmasq
=========

[![Build Status](https://travis-ci.com/cloudweeb/cloudweeb.dnsmasq.svg?branch=master)](https://travis-ci.com/cloudweeb/cloudweeb.dnsmasq)

Ansible role to install and configure Dnsmasq

Requirements
------------

None

Role Variables
--------------

A description of the settable variables for this role should go here, including
any variables that are in defaults/main.yml, vars/main.yml, and any variables
that can/should be set via parameters to the role. Any variables that are read
from other roles and/or the global scope (ie. hostvars, group vars, etc.) should
be mentioned here as well.

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      vars:
        dnsmasq_config:
          - name: global.conf
            content: |
              port=53
              bind-interfaces
              priority: '00'
      roles:
       -  role: cloudweeb.dnsmasq

License
-------

BSD/MIT

Author Information
------------------

Agnesius Santo Naibaho
