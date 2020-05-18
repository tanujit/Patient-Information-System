# PIS
import tkinter
import tkinter.ttk
import tkinter.messagebox
import sqlite3
CLASS Database:
    FUNCTION __init__(self):
         dbConnection <- sqlite3.connect("dbFile.db")
         dbCursor <-  dbConnection.cursor()
    ENDFUNCTION

    FUNCTION __del__(self):
         dbCursor.close()
         dbConnection.close()
    ENDFUNCTION

    FUNCTION Insert(self, id, fName, lName, dob, mob, yob, gender, address, phone, email, bloodGroup, history, doctor):
         dbConnection.commit()
    ENDFUNCTION

    FUNCTION Update(self, fName, lName, dob, mob, yob, gender, address, phone, email, bloodGroup, history, doctor, id):
         dbConnection.commit()
    ENDFUNCTION

    FUNCTION Search(self, id):
        searchResults <-  dbCursor.fetchall()
        RETURN searchResults
    ENDFUNCTION

    FUNCTION Delete(self, id):
         dbConnection.commit()
    ENDFUNCTION

    FUNCTION Display(self):
        records <-  dbCursor.fetchall()
        RETURN records
    ENDFUNCTION

ENDCLASS

CLASS Values:
    FUNCTION Validate(self, id, fName, lName, phone, email, history, doctor):
        IF not (id.isdigit() AND (len(id) = 3)):
            RETURN "id"
        ELSEIF not (fName.isalpha()):
            RETURN "fName"
        ELSEIF not (lName.isalpha()):
            RETURN "lName"
        ELSEIF not (phone.isdigit() AND (len(phone) = 10)):
            RETURN "phone"
        ELSEIF not (email.count("@") = 1 AND email.count(".") > 0):
            RETURN "email"
        ELSEIF not (history.isalpha()):
            RETURN "history"
        ELSEIF not (doctor.isalpha()):
            RETURN "doctor"
        ELSE:
            RETURN "SUCCESS"
        ENDIF
    ENDFUNCTION

ENDCLASS

CLASS InsertWindow:
    FUNCTION __init__(self):
         window <- tkinter.Tk()
         window.wm_title("Insert data")
        # Initializing all the variables
         id <- tkinter.StringVar()
         fName <- tkinter.StringVar()
         lName <- tkinter.StringVar()
         address <- tkinter.StringVar()
         phone <- tkinter.StringVar()
         email <- tkinter.StringVar()
         history <- tkinter.StringVar()
         doctor <- tkinter.StringVar()
         genderList <- ["Male", "Female", "Transgender", "Other"]
         dateList <- list(range(1, 32))
         monthList <- ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
         yearList <- list(range(1900, 2020))
         bloodGroupList <- ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
        # Labels
        tkinter.Label( window, text <- "Patient ID",  width <- 25).grid(pady <- 5, column <- 1, row <- 1)
        tkinter.Label( window, text <- "First Name",  width <- 25).grid(pady <- 5, column <- 1, row <- 2)
        tkinter.Label( window, text <- "Last Name",  width <- 25).grid(pady <- 5, column <- 1, row <- 3)
        tkinter.Label( window, text <- "D.O.B",  width <- 25).grid(pady <- 5, column <- 1, row <- 4)
        tkinter.Label( window, text <- "M.O.B",  width <- 25).grid(pady <- 5, column <- 1, row <- 5)
        tkinter.Label( window, text <- "Y.O.B",  width <- 25).grid(pady <- 5, column <- 1, row <- 6)
        tkinter.Label( window, text <- "Gender",  width <- 25).grid(pady <- 5, column <- 1, row <- 7)
        tkinter.Label( window, text <- "Home Address",  width <- 25).grid(pady <- 5, column <- 1, row <- 8)
        tkinter.Label( window, text <- "Phone Number",  width <- 25).grid(pady <- 5, column <- 1, row <- 9)
        tkinter.Label( window, text <- "Email ID",  width <- 25).grid(pady <- 5, column <- 1, row <- 10)
        tkinter.Label( window, text <- "Blood Group",  width <- 25).grid(pady <- 5, column <- 1, row <- 11)
        tkinter.Label( window, text <- "Patient History",  width <- 25).grid(pady <- 5, column <- 1, row <- 12)
        tkinter.Label( window, text <- "Doctor",  width <- 25).grid(pady <- 5, column <- 1, row <- 13)
        # Fields
        # Entry widgets
         idEntry <- tkinter.Entry( window,  width <- 25, textvariable <-  id)
         fNameEntry <- tkinter.Entry( window,  width <- 25, textvariable <-  fName)
         lNameEntry <- tkinter.Entry( window,  width <- 25, textvariable <-  lName)
         addressEntry <- tkinter.Entry( window,  width <- 25, textvariable <-  address)
         phoneEntry <- tkinter.Entry( window,  width <- 25, textvariable <-  phone)
         emailEntry <- tkinter.Entry( window,  width <- 25, textvariable <-  email)
         historyEntry <- tkinter.Entry( window,  width <- 25, textvariable <-  history)
         doctorEntry <- tkinter.Entry( window,  width <- 25, textvariable <-  doctor)
         idEntry.grid(pady <- 5, column <- 3, row <- 1)
         fNameEntry.grid(pady <- 5, column <- 3, row <- 2)
         lNameEntry.grid(pady <- 5, column <- 3, row <- 3)
         addressEntry.grid(pady <- 5, column <- 3, row <- 8)
         phoneEntry.grid(pady <- 5, column <- 3, row <- 9)
         emailEntry.grid(pady <- 5, column <- 3, row <- 10)
         historyEntry.grid(pady <- 5, column <- 3, row <- 12)
         doctorEntry.grid(pady <- 5, column <- 3, row <- 13)
        # Combobox widgets
         dobBox <- tkinter.ttk.Combobox( window, values <-  dateList, width <- 20)
         mobBox <- tkinter.ttk.Combobox( window, values <-  monthList, width <- 20)
         yobBox <- tkinter.ttk.Combobox( window, values <-  yearList, width <- 20)
         genderBox <- tkinter.ttk.Combobox( window, values <-  genderList, width <- 20)
         bloodGroupBox <- tkinter.ttk.Combobox( window, values <-  bloodGroupList, width <- 20)
         dobBox.grid(pady <- 5, column <- 3, row <- 4)
         mobBox.grid(pady <- 5, column <- 3, row <- 5)
         yobBox.grid(pady <- 5, column <- 3, row <- 6)
         genderBox.grid(pady <- 5, column <- 3, row <- 7)
         bloodGroupBox.grid(pady <- 5, column <- 3, row <- 11)
        # Button widgets
        tkinter.Button( window, width <- 20, text <- "Insert", command <-  Insert).grid(pady <- 15, padx <- 5, column <- 1, row <- 14)
        tkinter.Button( window, width <- 20, text <- "Reset", command <-  Reset).grid(pady <- 15, padx <- 5, column <- 2, row <- 14)
        tkinter.Button( window, width <- 20, text <- "Close", command <-  window.destroy).grid(pady <- 15, padx <- 5, column <- 3, row <- 14)
         window.mainloop()
    ENDFUNCTION

    FUNCTION Insert(self):
         values <- Values()
         database <- Database()
         test <-  values.Validate( idEntry.get(),  fNameEntry.get(),  lNameEntry.get(), self.phoneEntry.get(), self.emailEntry.get(), self.historyEntry.get(), self.doctorEntry.get())
        IF ( test = "SUCCESS"):
             database.Insert( idEntry.get(),  fNameEntry.get(),  lNameEntry.get(),  dobBox.get(), self.mobBox.get(), self.yobBox.get(), self.genderBox.get(), self.addressEntry.get(), self.phoneEntry.get(), self.emailEntry.get(), self.bloodGroupBox.get(), self.historyEntry.get(), self.doctorEntry.get())
        ELSE:
             valueErrorMessage <- "Invalid input in field " +  test 
            tkinter.messagebox.showerror("Value Error",  valueErrorMessage)
        ENDIF
    ENDFUNCTION

    FUNCTION Reset(self):
         idEntry.delete(0, tkinter.END)
         fNameEntry.delete(0, tkinter.END)
         lNameEntry.delete(0, tkinter.END)
         dobBox.set("")
         mobBox.set("")
         yobBox.set("")
         genderBox.set("")
         addressEntry.delete(0, tkinter.END)
         phoneEntry.delete(0, tkinter.END)
         emailEntry.delete(0, tkinter.END)
         bloodGroupBox.set("")
         historyEntry.delete(0, tkinter.END)
         doctorEntry.delete(0, tkinter.END)
    ENDFUNCTION

ENDCLASS

CLASS UpdateWindow:
    FUNCTION __init__(self, id):
         window <- tkinter.Tk()
         window.wm_title("Update data")
        # Initializing all the variables
         id <- id
         fName <- tkinter.StringVar()
         lName <- tkinter.StringVar()
         address <- tkinter.StringVar()
         phone <- tkinter.StringVar()
         email <- tkinter.StringVar()
         history <- tkinter.StringVar()
         doctor <- tkinter.StringVar()
         genderList <- ["Male", "Female", "Transgender", "Other"]
         dateList <- list(range(1, 32))
         monthList <- ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
         yearList <- list(range(1900, 2020))
         bloodGroupList <- ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
        # Labels
        tkinter.Label( window, text <- "Patient ID",  width <- 25).grid(pady <- 5, column <- 1, row <- 1)
        tkinter.Label( window, text <- id,  width <- 25).grid(pady <- 5, column <- 3, row <- 1)
        tkinter.Label( window, text <- "First Name",  width <- 25).grid(pady <- 5, column <- 1, row <- 2)
        tkinter.Label( window, text <- "Last Name",  width <- 25).grid(pady <- 5, column <- 1, row <- 3)
        tkinter.Label( window, text <- "D.O.B",  width <- 25).grid(pady <- 5, column <- 1, row <- 4)
        tkinter.Label( window, text <- "M.O.B",  width <- 25).grid(pady <- 5, column <- 1, row <- 5)
        tkinter.Label( window, text <- "Y.O.B",  width <- 25).grid(pady <- 5, column <- 1, row <- 6)
        tkinter.Label( window, text <- "Gender",  width <- 25).grid(pady <- 5, column <- 1, row <- 7)
        tkinter.Label( window, text <- "Home Address",  width <- 25).grid(pady <- 5, column <- 1, row <- 8)
        tkinter.Label( window, text <- "Phone Number",  width <- 25).grid(pady <- 5, column <- 1, row <- 9)
        tkinter.Label( window, text <- "Email ID",  width <- 25).grid(pady <- 5, column <- 1, row <- 10)
        tkinter.Label( window, text <- "Blood Group",  width <- 25).grid(pady <- 5, column <- 1, row <- 11)
        tkinter.Label( window, text <- "Patient History",  width <- 25).grid(pady <- 5, column <- 1, row <- 12)
        tkinter.Label( window, text <- "Doctor",  width <- 25).grid(pady <- 5, column <- 1, row <- 13)
        # Set previous values
         database <- Database()
         searchResults <-  database.Search(id)
        tkinter.Label( window, text <-  searchResults[0][1],  width <- 25).grid(pady <- 5, column <- 2, row <- 2)
        tkinter.Label( window, text <-  searchResults[0][2],  width <- 25).grid(pady <- 5, column <- 2, row <- 3)
        tkinter.Label( window, text <-  searchResults[0][3],  width <- 25).grid(pady <- 5, column <- 2, row <- 4)
        tkinter.Label( window, text <-  searchResults[0][4],  width <- 25).grid(pady <- 5, column <- 2, row <- 5)
        tkinter.Label( window, text <-  searchResults[0][5],  width <- 25).grid(pady <- 5, column <- 2, row <- 6)
        tkinter.Label( window, text <-  searchResults[0][6],  width <- 25).grid(pady <- 5, column <- 2, row <- 7)
        tkinter.Label( window, text <-  searchResults[0][7],  width <- 25).grid(pady <- 5, column <- 2, row <- 8)
        tkinter.Label( window, text <-  searchResults[0][8],  width <- 25).grid(pady <- 5, column <- 2, row <- 9)
        tkinter.Label( window, text <-  searchResults[0][9],  width <- 25).grid(pady <- 5, column <- 2, row <- 10)
        tkinter.Label( window, text <-  searchResults[0][10],  width <- 25).grid(pady <- 5, column <- 2, row <- 11)
        tkinter.Label( window, text <-  searchResults[0][11],  width <- 25).grid(pady <- 5, column <- 2, row <- 12)
        tkinter.Label( window, text <-  searchResults[0][12],  width <- 25).grid(pady <- 5, column <- 2, row <- 13)
        # Fields
        # Entry widgets
         fNameEntry <- tkinter.Entry( window,  width <- 25, textvariable <-  fName)
         lNameEntry <- tkinter.Entry( window,  width <- 25, textvariable <-  lName)
         addressEntry <- tkinter.Entry( window,  width <- 25, textvariable <-  address)
         phoneEntry <- tkinter.Entry( window,  width <- 25, textvariable <-  phone)
         emailEntry <- tkinter.Entry( window,  width <- 25, textvariable <-  email)
         historyEntry <- tkinter.Entry( window,  width <- 25, textvariable <-  history)
         doctorEntry <- tkinter.Entry( window,  width <- 25, textvariable <-  doctor)
         fNameEntry.grid(pady <- 5, column <- 3, row <- 2)
         lNameEntry.grid(pady <- 5, column <- 3, row <- 3)
         addressEntry.grid(pady <- 5, column <- 3, row <- 8)
         phoneEntry.grid(pady <- 5, column <- 3, row <- 9)
         emailEntry.grid(pady <- 5, column <- 3, row <- 10)
         historyEntry.grid(pady <- 5, column <- 3, row <- 12)
         doctorEntry.grid(pady <- 5, column <- 3, row <- 13)
        # Combobox widgets
         dobBox <- tkinter.ttk.Combobox( window, values <-  dateList, width <- 20)
         mobBox <- tkinter.ttk.Combobox( window, values <-  monthList, width <- 20)
         yobBox <- tkinter.ttk.Combobox( window, values <-  yearList, width <- 20)
         genderBox <- tkinter.ttk.Combobox( window, values <-  genderList, width <- 20)
         bloodGroupBox <- tkinter.ttk.Combobox( window, values <-  bloodGroupList, width <- 20)
         dobBox.grid(pady <- 5, column <- 3, row <- 4)
         mobBox.grid(pady <- 5, column <- 3, row <- 5)
         yobBox.grid(pady <- 5, column <- 3, row <- 6)
         genderBox.grid(pady <- 5, column <- 3, row <- 7)
         bloodGroupBox.grid(pady <- 5, column <- 3, row <- 11)
        # Button widgets
        tkinter.Button( window, width <- 20, text <- "Update", command <-  Update).grid(pady <- 15, padx <- 5, column <- 1, row <- 14)
        tkinter.Button( window, width <- 20, text <- "Reset", command <-  Reset).grid(pady <- 15, padx <- 5, column <- 2, row <- 14)
        tkinter.Button( window, width <- 20, text <- "Close", command <-  window.destroy).grid(pady <- 15, padx <- 5, column <- 3, row <- 14)
         window.mainloop()
    ENDFUNCTION

    FUNCTION Update(self):
         database <- Database()
         database.Update( fNameEntry.get(),  lNameEntry.get(),  dobBox.get(),  mobBox.get(), self.yobBox.get(), self.genderBox.get(), self.addressEntry.get(), self.phoneEntry.get(), self.emailEntry.get(), self.bloodGroupBox.get(), self.historyEntry.get(), self.doctorEntry.get(), self.id)
    ENDFUNCTION

    FUNCTION Reset(self):
         fNameEntry.delete(0, tkinter.END)
         lNameEntry.delete(0, tkinter.END)
         dobBox.set("")
         mobBox.set("")
         yobBox.set("")
         genderBox.set("")
         addressEntry.delete(0, tkinter.END)
         phoneEntry.delete(0, tkinter.END)
         emailEntry.delete(0, tkinter.END)
         bloodGroupBox.set("")
         historyEntry.delete(0, tkinter.END)
         doctorEntry.delete(0, tkinter.END)
    ENDFUNCTION

ENDCLASS

CLASS DatabaseView:
    FUNCTION __init__(self, data):
         databaseViewWindow <- tkinter.Tk()
         databaseViewWindow.wm_title("Database View")
        # Label widgets
        tkinter.Label( databaseViewWindow, text <- "Database View Window",  width <- 25).grid(pady <- 5, column <- 1, row <- 1)
         databaseView <- tkinter.ttk.Treeview( databaseViewWindow)
         databaseView.grid(pady <- 5, column <- 1, row <- 2)
         databaseView["show"] <- "headings"
         databaseView["columns"] <- ("id", "fName", "lName", "dob", "mob", "yob", "gender", "address", "phone", "email", "bloodGroup", "history", "doctor")
        # Treeview column headings
         databaseView.heading("id", text <- "ID")
         databaseView.heading("fName", text <- "First Name")
         databaseView.heading("lName", text <- "Last Name")
         databaseView.heading("dob", text <- "D.O.B")
         databaseView.heading("mob", text <- "M.O.B")
         databaseView.heading("yob", text <- "Y.O.B")
         databaseView.heading("gender", text <- "Gender")
         databaseView.heading("address", text <- "Home Address")
         databaseView.heading("phone", text <- "Phone Number")
         databaseView.heading("email", text <- "Email ID")
         databaseView.heading("bloodGroup", text <- "Blood Group")
         databaseView.heading("history", text <- "History")
         databaseView.heading("doctor", text <- "Doctor")
        # Treeview columns
         databaseView.column("id", width <- 40)
         databaseView.column("fName", width <- 100)
         databaseView.column("lName", width <- 100)
         databaseView.column("dob", width <- 60)
         databaseView.column("mob", width <- 60)
         databaseView.column("yob", width <- 60)
         databaseView.column("gender", width <- 60)
         databaseView.column("address", width <- 200)
         databaseView.column("phone", width <- 100)
         databaseView.column("email", width <- 200)
         databaseView.column("bloodGroup", width <- 100)
         databaseView.column("history", width <- 100)
         databaseView.column("doctor", width <- 100)
        for record in data:
             databaseView.insert('', 'end', values=(record))
        ENDFOR
         databaseViewWindow.mainloop()
    ENDFUNCTION

ENDCLASS

CLASS SearchDeleteWindow:
    FUNCTION __init__(self, task):
        window <- tkinter.Tk()
        window.wm_title(task + " data")
        # Initializing all the variables
         id <- tkinter.StringVar()
         fName <- tkinter.StringVar()
         lName <- tkinter.StringVar()
         heading <- "Please enter Patient ID to " + task
        # Labels
        tkinter.Label(window, text <-  heading, width <- 50).grid(pady <- 20, row <- 1)
        tkinter.Label(window, text <- "Patient ID", width <- 10).grid(pady <- 5, row <- 2)
        # Entry widgets
         idEntry <- tkinter.Entry(window, width <- 5, textvariable <-  id)
         idEntry.grid(pady <- 5, row <- 3)
        # Button widgets
        IF (task = "Search"):
            tkinter.Button(window, width <- 20, text <- task, command <-  Search).grid(pady <- 15, padx <- 5, column <- 1, row <- 14)
        ELSEIF (task = "Delete"):
            tkinter.Button(window, width <- 20, text <- task, command <-  Delete).grid(pady <- 15, padx <- 5, column <- 1, row <- 14)
        ENDIF
    ENDFUNCTION

    FUNCTION Search(self):
         database <- Database()
         data <-  database.Search( idEntry.get())
         databaseView <- DatabaseView( data)
    ENDFUNCTION

    FUNCTION Delete(self):
         database <- Database()
         database.Delete( idEntry.get())
    ENDFUNCTION

ENDCLASS

CLASS HomePage:
    FUNCTION __init__(self):
         homePageWindow <- tkinter.Tk()
         homePageWindow.wm_title("Patient Information System")
                                                ENDFOR
        tkinter.Label( homePageWindow, text <- "Home Page",  width <- 100).grid(pady <- 20, column <- 1, row <- 1)
        tkinter.Button( homePageWindow, width <- 20, text <- "Insert", command <-  Insert).grid(pady <- 15, column <- 1, row <- 2)
        tkinter.Button( homePageWindow, width <- 20, text <- "Update", command <-  Update).grid(pady <- 15, column <- 1, row <- 3)
        tkinter.Button( homePageWindow, width <- 20, text <- "Search", command <-  Search).grid(pady <- 15, column <- 1, row <- 4)
        tkinter.Button( homePageWindow, width <- 20, text <- "Delete", command <-  Delete).grid(pady <- 15, column <- 1, row <- 5)
        tkinter.Button( homePageWindow, width <- 20, text <- "Display", command <-  Display).grid(pady <- 15, column <- 1, row <- 6)
        tkinter.Button( homePageWindow, width <- 20, text <- "Exit", command <-  homePageWindow.destroy).grid(pady <- 15, column <- 1, row <- 7)
        application <- HomePage
         homePageWindow.mainloop()
    ENDFUNCTION

    FUNCTION Insert(self):
         insertWindow <- InsertWindow()
    ENDFUNCTION

    FUNCTION Update(self):
         updateIDWindow <- tkinter.Tk()
         updateIDWindow.wm_title("Update data")
        # Initializing all the variables
         id <- tkinter.StringVar()
        # Label
        tkinter.Label( updateIDWindow, text <- "Enter the ID to update", width <- 50).grid(pady <- 20, row <- 1)
        # Entry widgets
         idEntry <- tkinter.Entry( updateIDWindow, width <- 5, textvariable <-  id)
         idEntry.grid(pady <- 10, row <- 2)
        # Button widgets
        tkinter.Button( updateIDWindow, width <- 20, text <- "Update", command <-  updateID).grid(pady <- 10, row <- 3)
         updateIDWindow.mainloop()
    ENDFUNCTION

    FUNCTION updateID(self):
         updateWindow <- UpdateWindow( idEntry.get())
         updateIDWindow.destroy()
    ENDFUNCTION

    FUNCTION Search(self):
         searchWindow <- SearchDeleteWindow("Search")
    ENDFUNCTION

    FUNCTION Delete(self):
         deleteWindow <- SearchDeleteWindow("Delete")
    ENDFUNCTION

    FUNCTION Display(self):
         database <- Database()
         data <-  database.Display()
         displayWindow <- DatabaseView( data)
    ENDFUNCTION

ENDCLASS

homePage <- HomePage()
