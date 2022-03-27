#!/bin/bash

ansible-playbook site.yml -i inventory/my-cluster/hosts.ini --ask-pass --ask-become-pass