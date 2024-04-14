# -A flag means all namespaces, get all K8s objects
# -A = --all-namespaces
kubectl get all -A
kubectl get pods -A
kubectl get pods -A --show-labels
kubectl get pods -l key=value # get pods with specific labels
kubectl label pods <pod_name> key=value # add a label to a pod

kubectl get nodes

kubectl cluster-info

# kubectl pod commands, NOTE: these commands hold for all Kubernetes objects, not just pods

kubectl create pod <pod_name> --image=<image_name>


#create and run a pod
kubectl run <pod_name> --image=<image_name>
# --dry-run=client does not actually create pod
# it only validates the command, use it to generate a correct yaml file
# use this command to see syntax for various flags such as port
kubectl run <pod_name> --image=<image_name> --dry-run=client
kubectl run <pod_name> --image=<image_name> --dry-run=client -o yaml
kubectl run <pod_name> --image=<image_name> --port=3000 --restart=Always --dry-run=client -o yaml


kubectl get <pod_name> -o wide
kubectl get pods <pod_name> -o wide


kubectl get pods <pod_name> -o yaml
kubectl get pods -o yaml


kubectl describe <pod_name>
kubectl describe pods <pod_name>


# opens yaml file for editing
kubectl edit pods <pod_name>


kubectl logs <pod_name>
kubectl logs pods <pod_name>


kubectl delete pods <pod_name>
kubectl delete -f <config_yaml_file_used_to_create_object>


# first install kubernetes-sig/metrics-server
kubectl top pods
kubectl top pods -A
kubectl top pods --sort-by cpu
kubectl top pods --sort-by memory
kubectl top pods --all-namespaces --sort-by memory
# get the performance metrics of containers in a pod
kubectl top pod <pod_name> -n <namespace> --containers


# apply yaml file, -f is for file name
kubectl apply -f <path_to_yaml_file>


kubectl rollout status deployment <deployment_name>
# to see the changes made in a previous version
kubectl rollout history deployment <deployment_name> --revision=<revision_number>
# to roll back to a previous revision
kubectl rollout undo deployment <deployment_name> --to-revision=<revision_number>
kubectl rollout history deployment <deployment_name>


# get inside a pod, -c is for container, e.g. in a mutlicontainer setup
kubectl exec -it <pod_name> -c <container_name> bash_or_sh
kubectl exec -it <pod_name> -c <container_name> -- bash_or_sh

# get the IP address on which K8s is running
kubectl proxy


# status of controller manager, etcd, scheduler
kubectl get componentstatus

# scaling, autoscaling out and in using command line
kubectl scale deployment <deployment_name> --replicas=<num_pod_replicas>
# once any pod reaches cpu usage of 60%, a new pod will be created
# autoscaling can also be done by conditioning on memory usage
kubectl autoscale deployment <deployment_name> --min=5 --max=15 --cpu-percent=60


# kubeflow pipeline ui, -n is for namespace
kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80