Kind - Kubernets in cluster
----------------------------
"kind" (lowercase) is also a popular command-line tool. It stands for "Kubernetes in Docker." Its purpose is to allow you to run local Kubernetes clusters using Docker containers as "nodes."

You can install kind in your local machine in the following ways:

    - Installing From Release Binaries
    - Installing From Source
    - Installing With A Package Manager
    
Refer to this : https://kind.sigs.k8s.io/docs/user/quick-start/#installing-from-release-binaries


Creating cluster:
-------------------------------------------------
This is the most common command and creates a single-node cluster (the default cluster name is kind).

                kind create cluster

If you have a customised name for your cluster:

                kind create cluster --name your cluster_name
            
If you need to use a special vesion of image for creating cluster you can use:

                kind create cluster --image version  (for example : --image kindest/node:v1.28.0)

You will see output similar to this, indicating the steps:

                Creating cluster "kind" ...
                 ✓ Ensuring node image (kindest/node:v1.28.0) ━━━
                 ✓ Preparing nodes ━━━
                 ✓ Writing configuration ━━━
                 ✓ Starting control-plane ━━━
                 ✓ Installing CNI ━━━
                 ✓ Installing StorageClass ━━━
                 ✓ Joining worker nodes ━━━
                Set kubectl context to "kind-kind"
                You can now use your cluster with:
                
                kubectl cluster-info --context kind-kind
                
                Have fun with your cluster!

Verifying the Cluster
--------------------------------

Once created, you can use kubectl to verify its status.

                    kubectl get nodes
        
Output:

                    NAME                 STATUS   ROLES           AGE   VERSION
                    kind-control-plane   Ready    control-plane   2m    v1.28.0


Get your cluster info
---------------------------

                   kubectl cluster-info

Get your kubernets cluster version info
--------------------------------------

                    kubectl version

setting the kubectl Context
--------------------------------------
kind automatically sets your kubectl context to the newly created cluster.If you have multiple cluster then you can switch it with :

                kubectl config use-context cluster name


deleting a cluster
------------------------------
                
                kind delete cluster
                     or 
                kind delete cluster --name your cluster name

Listing Clusters
-----------------------
If you have multiple kind clusters then you can list them by:

            kind get clusters



                
