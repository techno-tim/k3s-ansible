# Sample IPv6 configuration for `k3s-ansible`

This scenario contains a cluster configuration which is _IPv6 first_, but still supports dual-stack networking with IPv4 for most things.
This means:

- The API server VIP is an IPv6 address.
- The MetalLB pool consists of both IPv4 and IPv4 addresses.
- Nodes as well as cluster-internal resources (pods and services) are accessible via IPv4 as well as IPv6.

## Network design

All IPv6 addresses used in this scenario share a single `/48` prefix: `fdad:bad:ba55`.
The following subnets are used:

- `fdad:bad:ba55:`**`0`**`::/64` is the subnet which contains the cluster components meant for external access.
  That includes:

  - The VIP for the Kubernetes API server: `fdad:bad:ba55::333`
  - Services load-balanced by MetalLB: `fdad:bad:ba55::1b:0/112`
  - Cluster nodes: `fdad:bad:ba55::de:0/112`
  - The host executing Vagrant: `fdad:bad:ba55::1`

  In a home lab setup, this might be your LAN.

- `fdad:bad:ba55:`**`4200`**`::/56` is used internally by the cluster for pods.

- `fdad:bad:ba55:`**`4300`**`::/108` is used internally by the cluster for services.

IPv4 networking is also available:

- The nodes have addresses inside `192.168.123.0/24`.
  MetalLB also has a bit of address space in this range: `192.168.123.80-192.168.123.90`
- For pods and services, the k3s defaults (`10.42.0.0/16` and `10.43.0.0/16)` are used.

Note that the host running Vagrant is not part any of these IPv4 networks.
