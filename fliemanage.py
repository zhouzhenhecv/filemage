# -*- coding: utf-8 -*-
#linux

import os
import shutil
import pickle

#set manage dir
dir_main= "/share/"
dir_sub = "python_learn/learn/"
dir = dir_main+ dir_sub

# set copy or move destine dir
dir_des = "/share/temp"
savefilename = dir_des + r"/" + "map.mak"

#set manage sub dir or file 
filelist=["test"\
,"a.c"\
,"a.h"];

#get all file url by the dir
def get_all_files(dir):
    savefilelist = []
    for dirpath,dirnames,filenames in os.walk(dir):  
        for file in filenames:
            if [] != file:
                file_tmp = os.path.join(dirpath,file);
                savefilelist.append(file_tmp)
    return savefilelist

#get  Flist designate file url by Dir 
def get_all_files_by_list_and_dir(FList,Dir):
    DesFileList = []
    for dirpath,dirnames,filenames in os.walk(Dir):      
        for ifilenames in filenames:
            for iFList in FList:
                if iFList == ifilenames :
                    desfile = os.path.join(dirpath,ifilenames)
                    DesFileList.append(desfile)
        #if Flist have sub dir ,speacially deal with  
        for idirnames in dirnames:
            for iFList in FList:
                if idirnames == iFList:
                    desdir = os.path.join(dirpath,idirnames)
                    DesFileList.extend( get_all_files(desdir) )
    return DesFileList

#os.path.join(path,name) connect dir and filename
#os.path.split(path)  return dir and filename

def get_des_fliename(filename,exname,flag=0,des=''):
    path_temp , subfilename = os.path.split(filename)
    path = ""
    if flag == 0:
        path = path_temp
    else: 
        path = des      
    return path + r"/" + subfilename + exname

#set file map
#and the map,[source,destination]
def setmap(FileList,exname,flag,des):
    map = []
    for iF in FileList:
        desname = get_des_fliename(iF,exname,flag,des)
        map.append([iF,desname])
    return map

#save the file map by pickle
def Write(filename,map):
    f = open(filename,"w")
    pickle.dump(map,f)
    f.close()

def Read(filename):
    map=[]
    f = open(filename,"r")
    map = pickle.load(f)
    f.close()
    return map

#deleteallfile(filelist),batch delete all file. and the argv filelist is list ,have many files or a file.
#os.remove(path) delete a flle
#os.path.isfile()  check file exist , os.path.isdir() check dir exist
def del_all_file(FileList):
    for iF in FileList:
        if True == os.path.isfile(iF):
            os.remove(iF)
    return

#copy 
# shutil.copy(sourceDir,  targetDir)
#shutil.copy( src, dst)  复制一个文件到一个文件或一个目录
#shutil.copy2( src, dst)  在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
#shutil.copy2( src, dst)  如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
def copy_all_file(FileMap):
    for [src,des] in FileMap:
        if True == os.path.isfile(src):
            shutil.copy(src,des)
    return
#rename or move
def rename_all_flie(FileMap):
    for [src,des] in FileMap:
        if True == os.path.isfile(src):
            shutil.copy(src,des)
    return

def test():
    print filelist
    print "###############test get_all_files_by_list_and_dir()################"
    List = get_all_files_by_list_and_dir(filelist,dir)
    for i in List:
        print i

    print "###############test setmap()################"
    filemap = []
    filemap = setmap(List,"mak",1,dir_des)
    print filemap
    
    print "############test Write() and Read()################"
    Write(savefilename,filemap)
    print "*******************************************"
    testmap = Read(savefilename);
    print testmap
    
    print "###########test copy_all_file() ###########"
    copy_all_file(filemap)
    #print "###########test rename_all_flie() ###########"
    #rename_all_flie(filemap)
    #print "###########test del_all_file() ###########"
    # del_all_file(List)
    return

if __name__ == '__main__':
    test()





