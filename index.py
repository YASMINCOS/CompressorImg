from tkinter import *
from PIL import Image
from tkinter.filedialog import *
from tkinter import messagebox

co0 = "#000000"  
co1 = "#cc1d4e"  
co2 = "#feffff"  
co3 = "#0074eb"  
co4 = "#435e5a"  
co5 = "#59b356"  
co6 = "#d9d9d9"  


janela=Tk()
janela.geometry("400x250")
janela.title("")
janela.configure(background=co2)

frame=Frame(janela,width=400,height=250,bg=co2,relief='flat')
frame.grid(row=0,column=0,sticky=NSEW)

app_name=Label(frame,text='Compressor de Imagem',width=24,height=1,anchor=CENTER,pady=7,padx=10,relief='flat',font=('Courier 20 bold'),bg=co2,fg=co0)
app_name.grid(row=0,column=0,columnspan=2,sticky=NSEW,pady=1)



#abrindo imagem


def novoArquivo():
    ficheiro= askopenfilename()
    img=Image.open(ficheiro)


    img_altura, img_largura=img.size
    
    def converter():
        altura=int(entry_altura.get())
        largura=int(entry_largura.get())
        print(altura,largura)
        
        novo_valor=(altura,largura)
        nova_imagem=img.resize(novo_valor)
        
        img_salvar=asksaveasfilename()
        nova_imagem.save(img_salvar+".PNG")
        
        messagebox.showinfo("Sucesso","A imagem foi convertida com sucesso!")
        
        tamanho_original.destroy()
        nova_altura.destroy()
        nova_largura.destroy()
        entry_altura.destroy()
        entry_largura.destroy()
        b_converter.destroy()
        
    
    tamanho_original=Label(frame,text='A altura e Largura Original: '+str(img_altura)+ 'x' +str(img_largura),width=24,height=1,anchor=CENTER,pady=7,padx=10,relief='flat',font=('Courier 12 bold'),bg=co2,fg=co3)
    tamanho_original.grid(row=2,column=0,columnspan=2,sticky=NSEW,pady=1)
    
    
    nova_altura=Label(frame,text='Digite nova altura',width=10,height=1,anchor=CENTER,pady=7,padx=10,relief='flat',font=('Courier 10 bold'),bg=co2,fg=co0)
    nova_altura.grid(row=3,column=0,sticky=NSEW,pady=5)
    entry_altura=Entry(frame,width=9,justify="center")
    entry_altura.grid(row=4,column=0,sticky=NSEW,pady=5)


    nova_largura=Label(frame,text='Digite nova largura',width=10,height=1,anchor=CENTER,pady=7,padx=10,relief='flat',font=('Courier 10 bold'),bg=co2,fg=co0)
    nova_largura.grid(row=3,column=1,sticky=NSEW,pady=5)
    entry_largura=Entry(frame,width=9,justify="center")
    entry_largura.grid(row=4,column=1,sticky=NSEW,pady=5)


    b_converter=Button(frame,command=converter,text='Converter',width=10,height=1,anchor=CENTER,font="5",relief=RAISED,bg=co5,fg=co2)
    b_converter.grid(row=5,column=0,columnspan=2,pady=5)




b_img=Button(frame,command=novoArquivo,text=' + Novo',width=10,height=1,anchor=CENTER,font="5",relief=RAISED,bg=co3,fg=co2)
b_img.grid(row=1,column=0,columnspan=2,sticky=NSEW,pady=1)




janela.mainloop()