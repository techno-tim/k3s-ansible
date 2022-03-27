# Build a Kubernetes HA-cluster using k3s & kube-vip & metal-lb via Ansible

Based on <https://github.com/k3s-io/k3s-ansible>

Forked from <https://github.com/212850a/k3s-ansible>

Kube-vip Control Plane is described -> <https://kube-vip.io/control-plane/>

Video here <https://www.youtube.com/watch?v=CbkEWcUZ7zM>

More docs here <https://docs.technotim.live/posts/k3s-etcd-ansible/>

## K3s Ansible Playbook

Build a Kubernetes cluster using Ansible with k3s. The goal is easily install a Kubernetes cluster on machines running:

- [X] Debian
- [X] Ubuntu
- [X] CentOS

on processor architecture:

- [X] x64
- [X] arm64
- [X] armhf

## System requirements

Deployment environment must have Ansible 2.4.0+
Master and nodes must have passwordless SSH access

## Usage

First create a new directory based on the `sample` directory within the `inventory` directory:

```bash
cp -R inventory/sample inventory/my-cluster
```

Second, edit `inventory/my-cluster/hosts.ini` to match the system information gathered above. For example:

```ini
[master]
192.168.30.38
192.168.30.39
192.168.30.40

[node]
192.168.30.41
192.168.30.42

[k3s_cluster:children]
master
node
```

If multiple hosts are in the master group, the playbook will automatically setup k3s in HA mode with etcd.
<https://rancher.com/docs/k3s/latest/en/installation/ha-embedded/>
This requires at least k3s version 1.19.1

If needed, you can also edit `inventory/my-cluster/group_vars/all.yml` to match your environment.

Start provisioning of the cluster using the following command:

```bash
ansible-playbook site.yml -i inventory/my-cluster/hosts.ini
```

After deployment control plane will be accessible via virtual ip-address which is defined in inventory/group_vars/all.yml as apiserver_endpoint

Remove k3s cluster

```bash
ansible-playbook reset.yml -i inventory/my-cluster/hosts.ini
```

**Note: add --ask-pass --ask-become-pass if you are using password logins over ssh**

## Kubeconfig

To get access to your **Kubernetes** cluster just

```bash
scp debian@master_ip:~/.kube/config ~/.kube/config
```

## kube-vip

See <https://kube-vip.chipzoller.dev/>

## MetalLB

see <https://metallb.universe.tf/installation/>
