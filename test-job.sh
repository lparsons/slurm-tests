#!/bin/bash
#SBATCH --job-name test-job
#SBATCH --time 05:00
#SBATCH --nodes 1
#SBATCH --mail-type ALL
#SBATCH --mail-user lparsons@princeton.edu

echo "The job has begun."
echo "Wait 10 seconds..."
sleep 10 
echo "It's been 10 seconds, wait another 10 seconds..."
sleep 10
echo "It's been 20 seconds, wait another 10 seconds..."
sleep 10
echo "It's been 30 seconds, enough waiting: job completed."

