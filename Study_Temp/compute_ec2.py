#--coding:utf-8
print ('*'*15+'互联港湾私有云资源计算'+'*'*15)
physical_DiskSize=int(raw_input('单块物理磁盘大小G :')) #物理磁盘大小
physical_DiskNum=int(raw_input('单台物理服务器物理磁盘数量 ：'))   #物理磁盘数量
host_num=int(raw_input('物理主机数量 ：'))
py_Mem=int(raw_input('物理内存总大小G ：'))
CPU_num=int(raw_input('物理服务器逻辑CPU总核数C ：'))
CpuVT_proportion=int(raw_input('CPU虚拟化比例，1:2请输入[2]  : ')) #虚拟化比例
Disk_copy=int(raw_input('Ceph副本数量 ：'))
print '*'*30
def compute_vm_cpu():
    cpu_size=(CPU_num*CpuVT_proportion-physical_DiskNum)*host_num
    return cpu_size
def compute_vm_mem():
    mem_size=(py_Mem-physical_DiskNum)*host_num
    return mem_size
def compite_vm_disk():
    disk_size=physical_DiskNum*physical_DiskSize/Disk_copy/1024*host_num
    return disk_size
vmcpu=compute_vm_cpu()
vmmem=compute_vm_mem()
vmdisk=compite_vm_disk()
print '''虚拟化之后总的计算资源：
        CPU总数：%s 核
        内存总数：%s G
        硬盘总容量：%s TB
     ''' % (vmcpu,vmmem,vmdisk)



