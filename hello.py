from mpi4py import MPI
comm = MPI.COMM_WORLD
my_rank=comm.Get_rank()
p=comm.Get_size()
print("Hello:",my_rank)