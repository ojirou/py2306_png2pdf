import os
import img2pdf
from PIL import Image
def main():
    if __name__ == '__main__':
        print('画像を結合したい対象ディレクトリを入力してください')
        img_Folder = input('>> ')
        if(img_Folder[-1:]!="\\"):
            img_Folder=img_Folder + '\\'
        print(img_Folder)
        folder_name=img_Folder.split('\\')[-2]
        up_img_Folder=img_Folder.split(folder_name)[0]
        pdf_FileName = up_img_Folder + folder_name +'.pdf'
        extension  = ".png"
        with open(pdf_FileName,"wb") as f:
            f.write(img2pdf.convert([Image.open(img_Folder+j).filename for j in os.listdir(img_Folder)if j.endswith(extension)]))       
if __name__ == "__main__":
    main()