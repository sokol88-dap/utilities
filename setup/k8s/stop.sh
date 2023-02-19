kubectl delete -f job_notify.yaml  -n utility
kubectl delete -f db.yaml -n utility
kubectl delete secret notify-secret -n utility