# Vagrant Ansible Demo

This repository demonstrates the use of Vagrant and Ansible to set up a three-tier application environment on virtual machines. In this demo, we launch an EC2 instance, install Vagrant, and create and configure a three-tier application using Ansible.
![architecture Image](https://github.com/Khushalsarode/Vagrant-Ansible/blob/master/architecture.jpg)

## Setup

### Install Vagrant

To install Vagrant on your machine, follow these steps:

1. Import the HashiCorp GPG key:

   ```bash
   wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
   ```

2. Add the HashiCorp repository:

   ```bash
   echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
   ```

3. Update and install Vagrant:

   ```bash
   sudo apt update && sudo apt install vagrant
   ```

### Launch Vagrant Virtual Machine

To create a Vagrant virtual machine, follow these steps:

1. Initialize Vagrant with an Ubuntu Trusty64 box:

   ```bash
   vagrant init ubuntu/trusty64
   ```

2. Verify that the Vagrantfile is created.

### Three-Tier Application

In this demo, two applications are created on the same server, running on different ports. Ansible is used to configure the three-tier application environment on Vagrant virtual boxes.
- Load Balancer Tier: Implement this layer Nginx as the load balancer.
- Application Tier: Host two separate applications on this layer.
- /db API: This API must retrieve data from the database.
- /non-db API: This API should simply return an HTTP 200 status code.
- Database Tier:
- Create separate databases for each application (db_one, db_two).
  
## Ansible Configuration

The Ansible script includes tasks to:

- Set up and configure the necessary components on the virtual machines.
- Install dependencies and packages required for the applications.
- Launch and configure the two applications, each running on a different port.

## set up and configure server using ansible
- configured nginx and added the reverse proxy to both app urls
- set up mysql db server and configured it for both app database users
- /db route set for db contains
- /non-db for return 200 status code to user

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/vagrant-ansible-demo.git
   ```

2. Navigate to the repository:

   ```bash
   cd vagrant-ansible-demo
   ```

3. Run the Vagrant environment:

   ```bash
   vagrant up
   ```

4. Verify the successful setup by accessing the applications on the virtual machines.

5. To access Application use the nginx ip using route you want to access, it will serve as per request

This demo provides a simple example of using Vagrant and Ansible to orchestrate the deployment of a three-tier application environment. Customize the Ansible script and Vagrant configuration based on your specific requirements.
