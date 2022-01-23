from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import test_main_project as TMP


def aft_click_process_detail():
    global process_label, outer_frame,my_canvas,my_scrollbar,second_frame, process_label_title
    try:
        #彈出新視窗-顯示整理結果
        processing_result = Toplevel()
        processing_result.iconbitmap(r'C:\Users\Joshua\Desktop\GUI輔助檔案\555.ico')
        processing_result.geometry('1100x1000')
        processing_result.title('細節條列')
          #Make a frame
        outer_frame=Frame(processing_result)
        outer_frame.pack(fill=BOTH,expand=1)
          #Create a Canvas
        my_canvas=Canvas(outer_frame, bg='#F3F3FA')
        my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
          #Create a scrollbar
        my_scrollbar=ttk.Scrollbar(outer_frame,orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)
          #Configure the Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion = my_canvas.bbox("all")))
          #Create another frame inside the canvas
        second_frame = Frame(my_canvas, bg='#F3F3FA')
          #Add that new frame to the window in the canvas
        my_canvas.create_window((0,0), window=second_frame, anchor="nw")
        # 印標題
        res = TMP.processing_detail(window.filename)
        process_label_title = Label(second_frame, text=" "+res[0], justify='left', bg='yellow', font=('Arial',20))
        process_label_title.grid(column=0, row=1, sticky=W)
        #一行行顯示整理好的事件
        nrow = 1
        while nrow <= len(res)-1:
            process_label = Label(second_frame, text=" "+res[nrow], wraplength=1000, justify='left', font=('Arial', 13), bg='#F3F3FA')
            process_label.grid(column=0, row=nrow+1, sticky=W)
            if nrow % 2 == 1:
                process_label=Label(second_frame, text="\n", bg='#F3F3FA')
                process_label.grid(column=0, row=nrow, sticky=W)
            nrow += 1
    except AttributeError:
        process_label_title = Label(second_frame, text='未選取檔案或找不到檔案', justify='left', bg='yellow', font=('Arial', 20))
        process_label_title.grid(column=0, row=1, sticky=W)

def aft_click_process_normal():
    global process_label, outer_frame, my_canvas, my_scrollbar, second_frame, mixy, process_label_title,FileNotFound_Label
    try:
        # 彈出新視窗-顯示整理結果
        processing_result = Toplevel()
        processing_result.iconbitmap(r'C:\Users\Joshua\Desktop\GUI輔助檔案\555.ico')
        processing_result.geometry('1100x1000')
        processing_result.title('一般顯示')
        # Make a frame
        outer_frame = Frame(processing_result)
        outer_frame.pack(fill=BOTH, expand=1)
        # Create a Canvas
        my_canvas = Canvas(outer_frame, bg='#F3F3FA')
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        # Create a scrollbar
        my_scrollbar = ttk.Scrollbar(outer_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        # Configure the Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        # Create another frame inside the canvas
        second_frame = Frame(my_canvas, bg='#F3F3FA')
        # Add that new frame to the window in the canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        # 一行行顯示整理好的事件
        nrow = 2
        mixy = []
        res = TMP.processing_normal(window.filename)
        while nrow <= len(res):
            mixy.append(res[nrow] + '。')
            nrow += 2

        #印標題
        process_label_title = Label(second_frame, text=res[0], justify='left', bg='yellow', font=('Arial', 20))
        process_label_title.grid(column=0, row=1, sticky=W)
        #印內容
        process_label = Label(second_frame, text=mixy, wraplength=1000, justify='left', font=('Arial', 13), bg='#F3F3FA')
        process_label.grid(column=0, row=2, sticky=W)
        assert window.filename != '000' or window.filename == ''
    except AttributeError:
        process_label_title = Label(second_frame, text='未選取檔案', justify='left', bg='yellow', font=('Arial', 20))
        process_label_title.grid(column=0, row=1, sticky=W)


def aft_click_process_timeline():
    try:
        results = TMP.processing_timeline(window.filename)
        TMP.make_timeline(results)
        assert window.filename != '000' or window.filename == ''
    except AttributeError:
        process_label_title = Label(second_frame, text='未選取檔案', justify='left', bg='yellow', font=('Arial', 12))
        process_label_title.grid(column=0, row=1, sticky=W)




def open():
    global show_filename
    show_filename.destroy()
    window.filename = filedialog.askopenfilename(initialdir='',title='請選取檔案',filetypes=(("txt files","*.txt"),("all files","*.*")))
    show_filename = Label(window,text="選取檔案："+window.filename, font=('Arial', 18), bg='azure')
    show_filename.place(x=400, y=300, anchor='n')

def cleaning_file_name():
    window.filename= '000'
    show_filename.destroy()

def example():
    processing_result = Toplevel()
    processing_result.geometry('1100x1000')
    processing_result.title('說明')
    example_contain = '新聞標題\nyyyy-mm-dd tt:tt\n新聞內容(不可空行)\n\n\n範例:\n\n金門珠山火警險波及聚落 初估燃燒面積5000平方公尺\n2021-03-13 17:40\n金門遭遇歷年來最嚴重的旱災，天乾物燥，火燒埔頻頻發生，今天下午珠山靶場突然起火，在東北風的助長下，火勢一發不可收拾，火勢有往珠山村落延燒的趨勢，讓金門縣消防局繃緊神經，出動11輛消防車，27名人員，才將火勢撲滅；初估燃燒面積5000平方公尺，現場確認無人員受傷，現場起火原因由火調科調查中。\n金門縣消防局表示，金防部的珠山靶場在今天下午13時31分許傳出火警，由於周遭都是枯草樹枝，火勢瞬間就相當猛烈，且有往珠山村落延燒的趨勢，濃煙直衝天際，共出動消防車11輛，人員27名(含水頭港1台，人員2名)，在第一大隊大隊長陳國瑋現場指揮下，在14時39分將大部分的火勢控制住，15時07分將火勢撲滅。\n據消防隊員表示，後來連重機具都加入，包括怪手2部支援開闢防火線及協助殘火處理；此外，軍方也支援2車8人。\n這場火警也引起不少搭機民眾的恐慌，有民眾就從空中拍下濃煙直沖天際的情況，看起來相當可怕；詳細起火原因需再進一步調查釐清。\n'

    process_label_title = Label(processing_result, text=example_contain, justify='left', wraplength=1000, font=('Arial', 12))
    process_label_title.grid(column=0, row=1, sticky=W)




window = Tk()
window.title('我的新聞整理程式')
window.geometry('800x500')
window.resizable(False, False)
window.iconbitmap(r'C:\Users\Joshua\Desktop\GUI輔助檔案\555.ico')
window.config(background='lavender')

#空白的檔案名
show_filename = Label(window, text="           ", font=('Arial', 18), bg='azure')
show_filename.place(x=400, y=300, anchor='n')
#做個框框
frame = LabelFrame(window, text='請先按照格式輸入檔案', font=('Arial', 20), padx=5, pady=5, width=700, height=350, bg='#F3F3FA', bd=5)
frame.pack(padx=10, pady=10)

#標籤
#lbl_1 = Label(frame, text='輸入檔案請按照格式', bg='yellow', fg='#263238', font=('Arial', 12))
#lbl_1.place(x=80, y=10, anchor='n')

#按鈕們
#檔案範例鈕
example_button = Button(frame, text='檔案格式請看我', command=example)
example_button.place(x=50, y=10, anchor='n')
#選擇檔案鈕
#click_btn = PhotoImage(file=r'C:\Users\Joshua\Desktop\GUI輔助檔案\open-file-icon.png')
#Let us create a label for button event
#img_label = Label(image=click_btn)
#Let us create a dummy button and pass the image
open_button = Button(window, text="選取檔案", command=open, font=('Arial', 12), padx=50, pady=25)

open_button.place(x=400, y=150, anchor='n')

#整理鈕-細節條列
execute_button_detail = Button(window, text="細節條列鈕", font=('Arial', 10), command=aft_click_process_detail, padx=50, pady=25)
execute_button_detail.place(x=140, y=400, anchor='n')
#整理紐-一般條列
execute_button_normal = Button(window, text='一般顯示鈕', font=('Arial', 10), command=aft_click_process_normal, padx=50, pady=25)
execute_button_normal.place(x=340, y=400, anchor='n')
#整理紐-時間軸
execute_button_timeline = Button(window, text='時間軸呈現', font=('Arial', 10), command=aft_click_process_timeline, padx=50, pady=25)
execute_button_timeline.place(x=540, y=400, anchor='n')
#清除紐-清除原檔名
cleaning_button=Button(window, text='清除選取檔案', command=cleaning_file_name)
cleaning_button.place(x=700, y=400, anchor='n')
#離開鈕
quit_button = Button(window, text='離開程式',command=window.destroy)
quit_button.place(x=700, y=440, anchor='n')

window.mainloop()