#!/bin/bash
#SBATCH --job-name test-mem-per-cpu
#SBATCH --time 05:00
#SBATCH --nodes 1
#SBATCH --ntasks-per-node=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=4G
#SBATCH --mail-type ALL
#SBATCH --mail-user lparsons@princeton.edu

echo "The job has begun."
echo "SLURM_NTASKS: $SLURM_NTASKS"
echo "SLURM_NTASKS_PER_NODE: $SLURM_NTASKS_PER_NODE"
echo "SLURM_CPUS_ON_NODE: $SLURM_CPUS_ON_NODE"
echo "SLURM_MEM_PER_CPU: $SLURM_MEM_PER_CPU"
echo "SLURM_MEM_PER_NODE: $SLURM_MEM_PER_NODE"

echo "Wait 10 seconds..."
sleep 10 
echo "It's been 10 seconds, wait another 10 seconds..."
sleep 10
echo "It's been 20 seconds, wait another 10 seconds..."
sleep 10
echo "It's been 30 seconds, enough waiting: job completed."

