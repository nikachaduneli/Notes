import sqlite3
import simple_encryptor
import datetime
import os, sys

notes = []
width = 80


def clear():
    
    if sys.platform == 'linux':
        os.system('clear')
    elif sys.platform == 'win32':
        os.system('cls')

def print_long_line():

    print('=' * width)

def say_hi():
    print_long_line()

    if width>68:
        place_to_move = (width-30)//2
    else:place_to_move = 0

    print(f"""
 {' '*place_to_move}█   █  █████ █     █     █████
 {' '*place_to_move}█   █  █     █     █     █   █
 {' '*place_to_move}█   █  █     █     █     █   █ 
 {' '*place_to_move}█████  █████ █     █     █   █
 {' '*place_to_move}█   █  █     █     █     █   █
 {' '*place_to_move}█   █  █     █     █     █   █
 {' '*place_to_move}█   █  █     █     █     █   █
 {' '*place_to_move}█   █  █████ █████ █████ █████                              
          """)

def create_tables(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                    username text,
                    password text)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS notes(
                    uid INTEGER PRIMARY KEY AUTOINCREMENT,
                    username text,
                    date text,
                    title text,
                    note text)""")


def insert_user(cursor,connection, username, password):

    password = simple_encryptor.to_code(password)
    cursor.execute("""INSERT INTO users(username, password)
                    VALUES(?,?)""",(username, password))

    connection.commit()



def insert_note(cursor, connection,username,date,title,note):

    cursor.execute("""INSERT INTO notes(username, date, title, note)
                        VALUES(?,?,?,?)""",(username, date, title, note))
    connection.commit()


def check_user(cursor,username, password):

    cursor.execute("""SELECT * FROM users""")
    users = cursor.fetchall()
    password = simple_encryptor.to_code(password)
    for i in users:
        if username == i[0] and password == i[1]:
            return True
    return False



def register(cursor,connection):


    print_menu_name('~~Register~~')

    while True:

        print("="*width)

        username = input('Username\n>>> ')
        password = input('Password\n>>> ')
        safePassword = input('Confirm Password\n>>> ')

        if username != '' and password !='' and safePassword != '':
            if password == safePassword:

                if check_user(cursor, username, password):

                    print('User Already Exists')


                else:
                    insert_user(cursor,connection, username, password)
                    print('User successfully added, \nReturn to Main Menu.')

                    wait()

                    menu(cursor,connection)
                    break
            else:
                print('Passwords don\'t match')

                if back_to_main_menu(cursor, connection):
                    break
                clear()
        else:
            print('Don\'t leave fields empty.')
            if back_to_main_menu(cursor, connection):
                break
            clear()


def  authentication(cursor,connection):


    print_menu_name('~~Log In Menu~~')

    while True:
        print_long_line()

        username = input('Username\n>>> ')
        password = input('Password\n>>> ')

        if username != '' and password !='':


            if check_user(cursor, username, password) == False:

                print('User not found.')

                if back_to_main_menu(cursor, connection):
                    break
            else:
                clear()
                # password = simple_encryptor.to_code(password)
                # cursor.execute('UPDATE users set loged_in = 1 where password = ?, username = ?', (password,username))
                open_user_page(cursor,connection, username)
                break


        else:
            print('Don\'t leave fields empty.')
            if back_to_main_menu(cursor, connection):
                break

def back_to_main_menu(cursor, connection):
    back = input('Type "-1" to return to Main Menu\n>>> ')

    if back == '-1':
        clear()
        menu(cursor, connection)
        return True
    else:return False

def open_user_page(cursor,connection,username):

    print_menu_name(f'~~{username}\'s Main Manu~~')

    option = input("""Choose Number: \n1.Add new note \n2.Existing notes\n""" + \
                    """3.Delete note \n4.Return to Main Menu\n>>>""")

    if option == '1':
        clear()
        add_note(cursor,connection, username)
        wait()

        open_user_page(cursor,connection,username)
    elif option == '2':
        clear()
        show_notes(cursor, username)
        wait()

        open_user_page(cursor,connection,username)
    elif option == '3':
        clear()
        del_note(cursor,connection, username)
        wait()

        open_user_page(cursor,connection,username)
    elif option == '4':
        clear()
        menu(cursor,connection)
    else:
        clear()
        wrong_command()

        open_user_page(cursor,connection,username)

def wait():
    print_long_line()
    a = input('Press enter to continue\n>>> ')
    print_long_line()
    clear()


def add_note(cursor,connection,username):

    print("-" *width)

    date = datetime.datetime.now().strftime('%d-%m-%Y')

    title = input('Title\n>>> ')

    title = '##Untitled##' if (len(title.split()) == 0) else '##'+title+'##'



    note = ''
    stopSign = ''

    print('-'*width+'\nBegin writing,\nType "-1" on new line to stop\n'+'-'*width)

    while True:
        stopSign = input()
        if stopSign == '-1':
            break
        note += '\n'+stopSign


    confirm = input('-'*width+'\n Type "+" to save\n>>> ')
    if confirm == '+':

        insert_note(cursor, connection,username,date,title,note)
        print('-'*width+'\nrecord saved, \nreturn to Main Menu.\n'+'-'*width)


    else:

        print('-'*width+'\nrecord didn\'t save, \nreturn to Main Menu.\n'+'-'*width)





def show_notes(cursor,username):
    global notes
    print_long_line()

    cursor.execute("""SELECT  uid,title,date, note FROM notes WHERE username = :1 """, (username,))

    notes = cursor.fetchall()

    if len(notes) == 0:
        print('No record was found')
        return False

    for i in range(len(notes)):


        print(str(i+1)+'.')

        for j in range(len(notes[i])):

            if j != 0 and j != 3:

                print(notes[i][j])

        print('-'*width)
    note_to_show = input('type number to see whole note\n>>> ')

    if note_to_show.isdigit() and int(note_to_show) <= len(notes):
        note_to_show = int(note_to_show) - 1
        clear()
        print('-'*width)
        print(notes[note_to_show][1])
        print(notes[note_to_show][3])
    elif note_to_show == '':

        return

    else:
        wrong_command()

def wrong_command():
    print_menu_name('Wrong Command!')
    wait()


def del_note(cursor,connection, username):

    if show_notes(cursor, username) == False:
        return
    note_to_del = input('Choose number you want to delete\n>>> ')


    if note_to_del.isdigit() and int(note_to_del) <= len(notes):

        note_to_del = int(note_to_del)-1

        note_to_del = notes[note_to_del][0]


        cursor.execute("""DELETE FROM notes where uid = (?) """, (note_to_del,))
        connection.commit()
        print('Record deleted.')



    else: wrong_command()

def print_menu_name(name):
    print_long_line()
    print(' '*(width//2-len(name)//2)+name)
    print_long_line()

def show_users(cursor,connection):

    cursor.execute("""SELECT * FROM users""")
    users = cursor.fetchall()
    for index, user in enumerate(users,start=1):

        print(f'{index}.{user[0]}')

    wait()
    menu(cursor,connection)

def change_menu_width(cursor,connection):
    global width

    new_width = input('Input nuber to adjust menu width\n>>> ')
    if new_width.isdigit():
        width = int(new_width)
    clear()
    menu(cursor,connection)


def menu(cursor,connection):

    say_hi()

    print_menu_name('~~Main manu~~')


    print_long_line()

    option = input(f"""Choose Number:\n1.Log In\n2.Register\n""" +\
             """3.See other users\n4.Change menu width\n5.Exit \n>>>""")

    if option == '1':
        clear()
        authentication(cursor,connection)

    elif option == '2':

        clear()
        register(cursor,connection)

    elif option == '3':
        clear()
        show_users(cursor,connection)

    elif option == '4':
        clear()
        change_menu_width(cursor,connection)

    elif option == '5':
        return
    else:
        clear()
        wrong_command()

        menu(cursor,connection)


def main():
    clear()

    with sqlite3.connect('notes.db') as connection:

            cursor = connection.cursor()
            create_tables(cursor)

            menu(cursor,connection)
            clear()

if __name__ == '__main__':
    main()


