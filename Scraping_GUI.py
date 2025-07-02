
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2024.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 420
student_name   = 'Avro Biswas'
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assessment Task 2 Description----------------------------------#
#
#  In this assessment task you will combine your knowledge of Python
#  programming, HTML-style mark-up languages, pattern matching,
#  database management, and Graphical User Interface design to produce
#  a robust, interactive "app" that allows its user to view and save
#  data from multiple online sources.
#
#  See the client's briefings accompanying this file for full
#  details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts,
#  together with some non-Python support files.
#
#--------------------------------------------------------------------#



#-----Set up---------------------------------------------------------#
#
# This section imports standard Python 3 modules sufficient to
# complete this assignment.  Don't change any of the code in this
# section, but you are free to import other Python 3 modules
# to support your solution, provided they are standard ones that
# are already supplied by default as part of a normal Python/IDLE
# installation.
#
# However, you may NOT use any Python modules that need to be
# downloaded and installed separately, such as "Beautiful Soup" or
# "Pillow", because the markers will not have access to such modules
# and will not be able to run your code.  Only modules that are part
# of a standard Python 3 installation may be used.

# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from sys import exit as abort

# A function for opening a web document given its URL.
# [You WILL need to use this function in your solution,
# either directly or via the "download" function below.]
from urllib.request import urlopen

# Some standard Tkinter functions.  [You WILL need to use
# SOME of these functions in your solution.]  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.  (NB: Although you can import individual widgets
# from the "tkinter.tkk" module, DON'T import ALL of them
# using a "*" wildcard because the "tkinter.tkk" module
# includes alternative versions of standard widgets
# like "Label" which leads to confusion.  If you want to use
# a widget from the tkinter.ttk module name it explicitly,
# as is done below for the progress bar widget.)
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression.  [You do not necessarily need to
# use these functions in your solution, because the problem
# may be solvable with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.]
from re import *

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).  [You WILL need to use this function
# in your solution.]
from webbrowser import open as urldisplay

# All the standard SQLite database functions.  [You WILL need
# to use some of these in your solution.]
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Validity Check-------------------------------------------------#
#
# This section confirms that the student has declared their
# authorship.  You must NOT change any of the code below.
#

if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

#
#--------------------------------------------------------------------#



#-----Supplied Function----------------------------------------------#
#
# Below is a function you can use in your solution if you find it
# helpful.  You are not required to use this function, but it may
# save you some effort.  Feel free to modify the function or copy
# parts of it into your own code.
#

# A function to download and save a web document.  The function
# returns the downloaded document as a character string and
# optionally saves it as a local file.  If the attempted download
# fails, an error message is written to the shell window and the
# special value None is returned.  However, the root cause of the
# problem is not always easy to diagnose, depending on the quality
# of the response returned by the web server, so the error
# messages generated by the function below are indicative only.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * incognito - If this parameter is True the Python program will
#      try to hide its identity from the web server. This can
#      sometimes be used to prevent the server from blocking access
#      to Python programs. However we discourage using this
#      option as it is both unreliable and unethical to
#      override the wishes of the web document provider!
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception sometimes raised when a web server
    # denies access to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded due to some communication error
    from urllib.error import URLError

    # Open the web document for reading (and make a "best
    # guess" about why if the attempt fails, which may or
    # may not be the correct explanation depending on how
    # well behaved the web server is!)
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (not recommended!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; ' + \
                               'rv:91.0; ADSSO) Gecko/20100101 Firefox/91.0')
            # print("Warning - Request to server does not reveal client's true identity.")
            # print("          Use this option only if absolutely necessary!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError as message: # probably a syntax error
        # print(f"\nCannot find requested document '{url}'")
        # print(f"Error message was: {message}\n")
        return None
    except HTTPError as message: # possibly an authorisation problem
        # print(f"\nAccess denied to document at URL '{url}'")
        # print(f"Error message was: {message}\n")
        return None
    except URLError as message: # probably the wrong server address
        # print(f"\nCannot access web server at URL '{url}'")
        # print(f"Error message was: {message}\n")
        return None
    except Exception as message: # something entirely unexpected
        # print("\nSomething went wrong when trying to download " + \
            #   f"the document at URL '{str(url)}'")
        # print(f"Error message was: {message}\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError as message:
        # print("\nUnable to decode document from URL " + \
            #   f"'{url}' as '{char_set}' characters")
        # print(f"Error message was: {message}\n")
        return None
    except Exception as message:
        # print("\nSomething went wrong when trying to decode " + \
            #   f"the document from URL '{url}'")
        # print(f"Error message was: {message}\n")
        return None

    # Optionally write the contents to a local text file
    # (silently overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(f'{target_filename}.{filename_extension}',
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            pass
            # print(f"\nUnable to write to file '{target_filename}'")
            # print(f"Error message was: {message}\n")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution below.
#

# Create the main window
main_window = Tk()

# Your code goes here
bg_color = 'gray90'
font_face = 'cascadia'
box_heading = ('cascadia', 16)

source_name = {'https://www.news.com.au/': 'News Corp Australia',
                'https://www.abc.net.au/news/justin':'ABC News',
                'https://www.smh.com.au/breaking-news':'The Sydney Morning Herald', 
                'https://www.bbc.com/news/world/australia':'BBC News (Australia)', 
                'https://www.reuters.com/':'Reuters',
                'https://www.cnbc.com/world/':'CNBC News',
                'https://www.theage.com.au/breaking-news':'The Age',
                'https://www.brisbanetimes.com.au/national/queensland':"Birsbane Times"}

headline = None
dateline = None

source_1 = 'https://www.news.com.au/'
# source_2 = 'https://www.abc.net.au/news/justin'
source_2 = 'https://www.smh.com.au/breaking-news'
# source_3 = 'https://www.reuters.com/' #currently not accessable
# source_3 = 'https://www.cnbc.com/world/'
# source_3 = 'https://www.theage.com.au/breaking-news'
source_3 = 'https://www.brisbanetimes.com.au/national/queensland'

main_window.geometry('740x500')
main_window.title("Avro's Fact Checking")
main_window.config(background=bg_color)

def add2db(source, headline, time, rating):
    db = connect('./reliability_ratings.db')
    command = f"INSERT INTO 'ratings' ('news_source', 'headline', 'dateline', 'rating') VALUES ('{source}', '{headline}', '{time}', {rating})"
    db.execute(command)
    db.commit()
    db.close()

def print_noSource_condition():
    global msg
    msg.grid_forget()
    msg = Message(status_frame, width=350, text='Please select a source first !',
                background=bg_color, font=(font_face, 13), fg='#dd0000')
    msg.grid(row=0, column=0)

# all callback function for widgets
def fnc_show_source():
    # print('The message')
    global msg, headline, dateline
    src = source.get()
    news_data = download(src, save_file=False) #put save_file=True to save the html code

    if(news_data == None):
        msg.grid_forget()
        msg = Message(status_frame, width=350, text='ERROR: Cannot access the Selected Source !',
                  background=bg_color, font=(font_face, 13), fg='#ff0000')
        msg.grid(row=0, column=0)
        source.set('No Source Selected')
        return
    
    msg.grid_forget()  # remove all past texts
    msg = Message(status_frame, width=350, text=source_name[src] + ' is selected as source !',
                  background=bg_color, font=(font_face, 13))
    msg.grid(row=0, column=0)

    headline_regex = 'Initial RegEx for Headline'
    dateline_regex = 'Initial RegEx for Timeline'

    if(src == 'https://www.news.com.au/'):
        headline_regex = r'<h4 class="storyblock_title"><a class="storyblock_title_link" href="https://www\.news\.com\.au/.*" data-tgev="event10" data-tgev-metric="npv" data-tgev-order="1" data-tgev-label="promo" data-word-match="" data-tgev-container="tops">([^<>]+)</a></h4>'
        dateline_regex = r'<time class="storyblock_datetime g_font-base-s" datetime="([^<>]*)">[^<>]*</time>'

    elif (src == 'https://www.brisbanetimes.com.au/national/queensland'):
        headline_regex = r'<h3 class="_2XVos" data-testid="article-headline" data-pb-type="hl"><a data-testid="article-link" href="/national/queensland/[^<>]*\.html">([^<>]*)</a></h3>'
        dateline_regex = r'<time class="_2_zR-" data-testid="datetime" dateTime="([^<>]*)">[^<>]+</time>'

    elif(src == 'https://www.smh.com.au/breaking-news'):
        headline_regex = r'<h3 class="_13KNF _2XVos" data-testid="article-headline" data-pb-type="hl"><a data-testid="article-link" href="/[^<>]+\.html">([^<>]+)</a></h3>'
        dateline_regex = r'<time class="_2_zR-" data-testid="datetime" dateTime="([^<>]*)">[^<>]+</time>'

    headline_lst = findall(headline_regex, news_data) #searching for regex match
    dateline_lst = findall(dateline_regex, news_data)

    # print(headline_lst)

    if(len(headline_lst) == 0):
        headline = 'Can not extract headline !'
    else:
        headline = headline_lst[0]

    if(len(dateline_lst) == 0):
        dateline = 'Time data not found !'
    else:
        dateline = dateline_lst[0]


def fnc_show_latest():
    # print('Show Latest Button Pressed !')
    global msg, headline, dateline
    src = source.get()
    if (src == 'No Source Selected'):
        print_noSource_condition()
        return
        
    msg.grid_forget()
    msg = Message(status_frame, width=350, text=headline + '\n\n' + dateline,
                  background=bg_color, font=(font_face, 13))
    msg.grid(row=0, column=0)


def fnc_show_details():
    # print('Show Details Button Pressed !')
    src = source.get()
    if (src == 'No Source Selected'):
        print_noSource_condition()
        return
    
    urldisplay(src)
    global msg
    msg.grid_forget()
    msg = Message(status_frame, width=350, text='Showing Details in the Browser...',
                  background=bg_color, font=(font_face, 13))
    msg.grid(row=0, column=0)


def fnc_show_rating(r):
    global msg
    msg.grid_forget()
    msg = Message(status_frame, width=350, text='Rating '+str(r)+' selected for the current news !',
                  background=bg_color, font=(font_face, 13))
    msg.grid(row=0, column=0)


def fnc_save_rating():
    src = source.get()
    # print('Save Rating Button Pressed !')
    if (src == 'No Source Selected'):
        print_noSource_condition()
        return
    
    global headline, dateline
    news_src = source_name[src]
    selected_rating = rate.get()

    add2db(news_src, headline, dateline, selected_rating)

    global msg
    msg.grid_forget()
    msg = Message(status_frame, width=350, text='Rating '+str(selected_rating)+' is saved for "'+ headline + '"',
                  background=bg_color, font=(font_face, 13))
    msg.grid(row=0, column=0)

# Creating frames
text_frame = Frame(master=main_window, width=400,
                   height=500, padx=10, background=bg_color)
text_frame.grid_propagate(0)
img_frame = Frame(master=main_window, borderwidth=4,
                  border=0, background='red2')

status_frame = LabelFrame(master=text_frame, text='System Status', background=bg_color,
                          font=box_heading, fg='gray', labelanchor='nw', padx=5, pady=5,
                          borderwidth=3, border=4, width=380, height=150)
status_frame.grid_propagate(0)

data_frame = LabelFrame(master=text_frame, text='Data Source', background=bg_color,
                        font=box_heading, fg='gray', labelanchor='nw', padx=5, pady=5,
                        borderwidth=3, border=4, width=250, height=170)
data_frame.grid_propagate(0)

rating_frame = LabelFrame(master=text_frame, text='Data Reliability', background=bg_color,
                          font=box_heading, fg='gray', labelanchor='nw', padx=5, pady=5,
                          borderwidth=3, border=4, width=200, height=150)
rating_frame.grid_propagate(0)

# position of two main frame
text_frame.grid(row=0, column=1)
img_frame.grid(row=0, column=0, padx=5)

# position of subframes
status_frame.grid(row=0, column=0, sticky='w', pady=3)
data_frame.grid(row=1, column=0, sticky='w', pady=3)
rating_frame.grid(row=2, column=0, sticky='w', pady=3)

# initial message
msg = Message(status_frame, width=350, text='Waiting for User Input . . .',
              background=bg_color, font=(font_face, 13), fg='gray')
msg.grid(row=0, column=0)

# options for selecting the source
source = StringVar(value='No Source Selected')
Radiobutton(data_frame, background=bg_color, text=source_name[source_1], font=(font_face, 13),
            variable=source, value=source_1, command=fnc_show_source).grid(
                row=0, column=0, sticky='w', columnspan=3)

Radiobutton(data_frame, background=bg_color, text=source_name[source_2], font=(font_face, 13),
            variable=source, value=source_2, command=fnc_show_source).grid(
                row=1, column=0, sticky='w', columnspan=3)

Radiobutton(data_frame, background=bg_color, text=source_name[source_3], font=(font_face, 13),
            variable=source, value=source_3, command=fnc_show_source).grid(
                row=2, column=0, sticky='w', columnspan=3)

Button(master=data_frame, text='Show Latest', font=(font_face, 11),
       command=fnc_show_latest).grid(row=3, column=0, padx=5)

Button(master=data_frame, text='Show Details', font=(font_face, 11),
       command=fnc_show_details).grid(row=3, column=1, padx=5)

# rating input
rate = IntVar()
rating = Scale(master=rating_frame, background=bg_color, from_=1, to=5, variable=rate,
               label='Rating', font=(font_face, 12), orient='horizontal')

btn = Button(master=rating_frame, text='Save Rating',
             font=(font_face, 11), command=fnc_save_rating)
rating.pack()
btn.pack(padx=5, pady=10)

image = PhotoImage(file='./AIRobot.png')

img_lbl = Label(master=img_frame, image=image, bg='#bbeeff')
img_lbl.grid(row=0, column=0)


menubar = Menu()
main_window.config(menu=menubar)

mymenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Menu', menu=mymenu)
mymenu.add_command(label='Option 1')
mymenu.add_separator()
mymenu.add_command(label='Option 2')

# Start the event loop to detect user inputs
main_window.mainloop()