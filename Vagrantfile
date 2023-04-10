Vagrant.configure(2) do |config|
    config.vm.define "minikube" do |minikube|
        minikube.vm.provider :virtualbox do |v|
            v.memory = 4096
            v.cpus = 4
        end
        
        minikube.vm.synced_folder "python", "/srv/pyhton-k8s-jobs"
        minikube.vm.box = "ubuntu/jammy64"
        minikube.vm.hostname = "minikube"
        minikube.vm.network "private_network", ip: "192.168.56.101", virtualbox__intnet: true
        minikube.vm.provision "ansible" do |ansible|
            ansible.playbook = "playbook-docker.yaml"
        end
    end
end
