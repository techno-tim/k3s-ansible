#!/bin/bash

ansible-playbook reset.yml -i inventory/my-cluster/hosts.ini --ask-pass --ask-become-pass
