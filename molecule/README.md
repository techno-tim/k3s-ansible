# Test suites for `k3s-ansible`

This folder contains the [molecule](https://molecule.rtfd.io/)-based test setup for this playbook.

## Scenarios

We have these scenarios:

- **default**:
  A 3 control + 2 worker node cluster based very closely on the [sample inventory](../inventory/sample/).

## How to execute

To test on your local machine, follow these steps:

### System requirements

Make sure that the following software packages are available on your system:

- [Python 3](https://www.python.org/downloads)
- [Vagrant](https://www.vagrantup.com/downloads)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

### Set up VirtualBox networking on Linux and macOS

_You can safely skip this if you are working on Windows._

Furthermore, the test cluster uses the `192.168.30.0/24` subnet which is [not set up by VirtualBox automatically](https://www.virtualbox.org/manual/ch06.html#network_hostonly).
To set the subnet up for use with VirtualBox, please make sure that `/etc/vbox/networks.conf` exists and that it contains this line:

```
* 192.168.30.0/24`
```

### Install Python dependencies

You will get [Molecule, Ansible and a few extra dependencies](../requirements.txt) via [pip](https://pip.pypa.io/).
Usually, it is advisable to work in a [virtual environment](https://docs.python.org/3/tutorial/venv.html) for this:

```bash
cd /path/to/k3s-ansible

# Create a virtualenv at ".env". You only need to do this once.
python3 -m venv .env

# Activate the virtualenv for your current shell session.
# If you start a new session, you will have to repeat this.
source .env/bin/activate

# Install the required packages into the virtualenv.
# These remain installed across shell sessions.
python3 -m pip install -r requirements.txt
```

### Run molecule

With the virtual environment from the previous step active in your shell session, you can now use molecule to test the playbook.
Interesting commands are:

- `molecule create`: Create virtual machines for the test cluster nodes.
- `molecule destroy`: Delete the virtual machines for the test cluster nodes.
- `molecule converge`: Run the `site` playbook on the nodes of the test cluster.
- `molecule side_effect`: Run the `reset` playbook on the nodes of the test cluster.
- `molecule verify`: Verify that the cluster works correctly.
- `molecule test`: The "all-in-one" sequence of steps that is executed in CI.
  This includes the `create`, `converge`, `verify`, `side_effect` and `destroy` steps.
  See [`molecule.yml`](default/molecule.yml) for more details.
