import os;
#filelist = os.listdir('.')
#filename = 'index.md'
#tmpfile = (not (filename in filelist)) and open(filename,'w+')
tmpfile = open('index.md','w')
tmpfile.write("## Learn - The Little Schemer(LISPer)\n")
map(lambda x:tmpfile.write("### [{0}]({0}/)+\n".format(x)),
    filter(lambda x:os.path.isdir(x),os.listdir('.')) )
tmpfile.close()
