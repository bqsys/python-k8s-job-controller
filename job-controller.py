from kubernetes import client, config
import argparse

def start_job(job_name, namespace):
    # Load the Kubernetes configuration
    config.load_kube_config()

    # Create a Kubernetes API client
    batch_v1 = client.BatchV1Api()

    # Get the job object
    job = batch_v1.read_namespaced_job(name=job_name, namespace=namespace)

    # Update the job object to start the job
    job.spec.completions = 1
    job.spec.parallelism = 1

    batch_v1.patch_namespaced_job(
        name=job_name,
        namespace=namespace,
        body=job
    )

    print("Job %s started" % job_name)

def stop_job(job_name, namespace):
    # Load the Kubernetes configuration
    config.load_kube_config()

    # Create a Kubernetes API client
    batch_v1 = client.BatchV1Api()

    # Get the job object
    job = batch_v1.read_namespaced_job(name=job_name, namespace=namespace)

    # Update the job object to stop the job
    job.spec.completions = 0
    job.spec.parallelism = 0

    batch_v1.patch_namespaced_job(
        name=job_name,
        namespace=namespace,
        body=job
    )

    print("Job %s stopped" % job_name)

def suspend_job(job_name, namespace):
    # Load the Kubernetes configuration
    config.load_kube_config()

    # Create a Kubernetes API client
    batch_v1 = client.BatchV1Api()

    # Get the job object
    job = batch_v1.read_namespaced_job(name=job_name, namespace=namespace)

    # Update the job object to suspend the job
    job.spec.suspend = True

    batch_v1.patch_namespaced_job(
        name=job_name,
        namespace=namespace,
        body=job
    )

    print("Job %s suspended" % job_name)

# function to retrieve the status of the job
def get_job_status():
    # get job details
    job = batch_client.read_namespaced_job(name=job_name, namespace=namespace)

    # check job status
    status = job.status
    if status.failed:
        print("Job failed.")
    elif status.succeeded:
        print("Job succeeded.")
    elif status.active:
        print("Job is still running.")
    elif status.conditions:
        for condition in status.conditions:
            if condition.type == "Failed":
                print("Job failed.")
            elif condition.type == "Complete":
                print("Job succeeded.")
    else:
        print("Job status is unknown.")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Start, stop, suspend or get status of a Kubernetes batch job.')
    parser.add_argument('--job-name', type=str, required=True, help='The name of the job')
    parser.add_argument('--namespace', type=str, required=True, help='The namespace of the job')
    parser.add_argument('--action', type=str, required=True, choices=['start', 'stop', 'suspend', 'status'], help='The action to perform on the job (start, stop, or suspend)')

    # Parse arguments
    args = parser.parse_args()

    # Call the appropriate function based on the action argument
    if args.action == 'start':
        start_job(args.job_name, args.namespace)
    elif args.action == 'stop':
        stop_job(args.job_name, args.namespace)
    elif args.action == 'suspend':
        suspend_job(args.job_name, args.namespace)
    elif args.action == 'status':
        get_job_status(args.job_name, args.namespace)

if __name__ == '__main__':
    main()
