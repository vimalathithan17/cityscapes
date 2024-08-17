import os
import shutil
def create_sd(newdir,sd_name):
    cwd=os.getcwd()
    os.chdir(newdir)
    #print('curr',os.getcwd())
    print(newdir+f'/{sd_name}')
    os.mkdir(sd_name)
    os.chdir(cwd)
suffix='leftImg8bit.png'
num_images_per_dir=6   
old_base='cityscapes'
new_base='cityscapes2'
print(os.path.isdir(old_base))
if os.path.exists(new_base):
    shutil.rmtree(new_base)
os.mkdir(new_base)
new_base=os.path.abspath(new_base)
old_base=os.path.abspath(old_base)
for sd in os.listdir(old_base):
    sd_path=old_base+'/'+sd
    create_sd(new_base,sd)
    new_sd_path=new_base+'/'+sd
    for ssd in os.listdir(sd_path):
        ssd_path=sd_path+'/'+ssd
        create_sd(new_sd_path,ssd)
        new_ssd_path=new_sd_path+'/'+ssd
        for city in os.listdir(ssd_path):
            city_path=ssd_path+'/'+city
            create_sd(new_ssd_path,city)
            new_city_path=new_ssd_path+'/'+city
o_gt=old_base+'/'+os.listdir(old_base)[0]
n_gt=new_base+'/'+os.listdir(new_base)[0]
o_lft=old_base+'/'+os.listdir(old_base)[1]
n_lft=new_base+'/'+os.listdir(new_base)[1]
for dir_ in os.listdir(o_lft):
    ol_dir=o_lft+f'/{dir_}'
    nl_dir=n_lft+f'/{dir_}'
    og_dir=o_gt+f'/{dir_}'
    ng_dir=n_gt+f'/{dir_}'
    for city in os.listdir(ol_dir):
        for i,image_name in enumerate(os.listdir(ol_dir+'/'+city)):
            if (i==num_images_per_dir):
                break
            print(image_name)
            shutil.copy(ol_dir+'/'+city+'/'+image_name,nl_dir+'/'+city)
            prefix=image_name[:-len(suffix)]
            for image in os.listdir(og_dir+'/'+city):
                if image.startswith(prefix):
                    print(image)
                    shutil.copy(og_dir+'/'+city+'/'+image,ng_dir+'/'+city)