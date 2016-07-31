# -*- coding: utf-8 -*- 
import os
import shutil
###linux
#源码目录
#是否应该设置目录是输入的 
#dir_pre = raw_input("please input the code dir \n for example :/homesec/lbteam/zhouzhenhe/code03/code/ ")
dir_main= "/share/"
dir_sub = "python_learn/learn/"
##注意  需要处理的文件夹或者文件名在这里添加
dir_des = "/share/temp"
savefilename = dir_des + r"/" + "map.mak"

filelist=["test"\
,"a.c"\
,"a.h"];

print filelist
#复制到的目标文件夹，或者移动到的 

#映射关系
file_des_src_map = [];

#拆分filelist 分成filelist_dir  filelist_file
#获取所要删除的文件的路径
dir = dir_main+ dir_sub

#print dir
#
# shutil.copy(sourceDir,  targetDir)
#copy映射关系保存到文件
#先获取所有映射关系表

def getdirfilelist(dir):
    savefilelist = []
    for dirpath,dirnames,filenames in os.walk(dir):  
        for file in filenames:
            if [] != file:
                file_tmp = os.path.join(dirpath,file);
                print "delete:",file_tmp
                savefilelist.append(file_tmp)
    return savefilelist

#python 如何判断是否是一个目录  os.path.isdir(path)
def getfileurlbydir(FList,Dir):
    DesFileList = []
    for dirpath,dirnames,filenames in os.walk(Dir):      
        for ifilenames in filenames:
            for iFList in FList:
                if iFList == ifilenames :
                    desfile = os.path.join(dirpath,ifilenames)
                    print "delete:",desfile
                    DesFileList.append(desfile)
        for idirnames in dirnames:
            for iFList in FList:
                if idirnames == iFList:
                    desdir = os.path.join(dirpath,idirnames)
                    DesFileList.extend(getdirfilelist(desdir))
    return DesFileList

###批量删除列表中的所有文件
#相关函数os.remove(path) 函数用来删除一个文件
#os.path.isfile() 和os.path.isdir()函数分别检验给出的路径是一个文件还是目录
def deleteallfile(FileList):
    for iF in FileList:
        if True == os.path.isfile(iF):
            os.remove(iF)
    return

###批量重命名 以某种后缀名   是否需要先建立某种映射关系
##相关函数 os.path.splitext()  分离文件名与扩展名
#os.path.join(path,name) 连接目录与文件名或目录
#os.path.split(path)  函数返回一个路径的目录名和文件名
#os.path.join(path,name) 连接目录与文件名或目录
#shutil.copy( src, dst)  复制一个文件到一个文件或一个目录
#shutil.copy2( src, dst)  在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
#shutil.copy2( src, dst)  如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
def getdesfliename(filename,exname,flag=0,des=''):
    path_temp , subfilename = os.path.split(filename)
    path = ""
    if flag == 0:
        path = path_temp
    else: 
        path = des      
    return path + r"/" + subfilename + exname

def renameallflie(FileList,exname):
    for iF in FileList:
        desname = getdesfliename(iF,exname)
        print desname
        #shutil.copy( iF, desname)
        #if True == os.path.isfile(desname):
         #   os.remove(desname)
    return


###copy 到指定目录
def copyallfile(SrcFile,DesFile):
###判断DesFile是否为目录
###判断所有源文件
    if os.path.isdir(DesFile) == False:
        return;

    return
###

def setmap(FileList,exname,flag,des):
    map = []
    for iF in FileList:
        desname = getdesfliename(iF,exname,flag,des)
        print [iF,desname]
        map.append([iF,desname])
        #print map
    return map



#保存映射关系到文件
import pickle
def Write(filename,map):
    f = open(filename,"w")
    #print map
    pickle.dump(map,f)
    f.close()
def Read(filename):
    map=[]
    f = open(filename,"r")
    map = pickle.load(f)
    #print map
    f.close()
    return map

def test():
    List = getfileurlbydir(filelist,dir)
    print "###############################"
    for i in List:
        print i
    filemap = []
    filemap = setmap(List,"mak",1,dir_des)
    print filemap

    Write(savefilename,filemap)
    ##
    print "*******************************************"
    testmap = Read(savefilename);

    print testmap
    
    return


if __name__ == '__main__':
    test()





