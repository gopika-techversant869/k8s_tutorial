Kind installation
-------------------------

You can install kind in following ways:

    - Installing From Release Binaries
    - Installing From Source
    - Installing With A Package Manager

If we use release binaries we can use  this:

      # For Intel Macs
      [ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.29.0/kind-darwin-amd64
      # For M1 / ARM Macs
      [ $(uname -m) = arm64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.29.0/kind-darwin-arm64
      chmod +x ./kind
      mv ./kind /some-dir-in-your-PATH/kind

Refer to this : https://kind.sigs.k8s.io/docs/user/quick-start/#installing-from-release-binaries


Creating cluster:
-------------------------------------------------

