# this is temport file for student management system
student=[]
teacher=[]
course = []

def add_stud():
     try:
          print("--------------------------------------")
          print("----------Add Student-------------")
          name=input("Enter Name :- ")
          rn=input("Enter Roll No :- ")
          address=input("Enter Address :- ")
          
          if any(rn in dict.values() for dict in student):
               print(f"{rn} This Roll no aleady exit")
          else:
               student.append({"Name":name,"Roll_no":rn,"Address":address})
               print("Student add succefully")
               print("--------------------------------------")       
     except Exception as e:
          print(e)

def display_stud():
     try:
          if student == []:
               print("--------------------------------------")
               print("Sorry not any Student Records")
          else:
               print("--------------------------------------")
               print("----------Student Details-----------")
               for stu in student:
                    print(f"Name :- {stu['Name']}\nRoll No :- {stu['Roll_no']}\nAddress :- {stu['Address']}")
                    print("--------------------------------------")
     except Exception as e:
          print(e)
     finally:
          print("--------------------------------------")

def update_stud():
     try:
          if student == []:
               print("--------------------------------------")
               print("Sorry not any Student Records")
               print("--------------------------------------")
          else:
               print("--------------------------------------")
               print("------Update student details------")
               rn=input("Enter Roll No :- ")
               for stu in student:
                    if stu['Roll_no']==rn:
                         stu['Name']=input("Enter new Name :- ")
                         stu['Address']=input("Enter new Address :- ")
                         print("Student data is updated")
                         return
               print("Not found student")
               print("--------------------------------------")
     except Exception as e:
          print(e)
     finally:
          print("--------------------------------------")
          
def delete_stud():
     try:
          if student == []:
               print("--------------------------------------")
               print("Sorry not any Student Records")
               print("--------------------------------------")
          else:
               print("--------------------------------------")
               print("-----Delete Student Records------")
               rn=input("Enter Roll No :- ")
               for stu in student:
                    if stu['Roll_no']==rn:
                         student.remove(stu)
                         print("Student Records deleted..!")
                         return
               print("Not found student")
               print("--------------------------------------")
     except Exception as e:
          print(e)

#Teacher
def add_teach():
     try:
          print("--------------------------------------")
          print("----------Add Teacher-------------")
          name=input("Enter Name : ")
          t_id=input("Enter Id : ")
          address=input("Enter Address : ")
          
          if any(t_id in dict.values() for dict in teacher):
               print(f"****{t_id} is exited*****")
          else:
               teacher.append({"Name":name,"t_id":t_id,"address":address})
               print("Teacher add succefully")
               print("--------------------------------------") 
     except Exception as e:
          print(e)
     finally:
          print("--------------------------------------") 
          
def display_teach():
     try:
          if teacher == []:
               print("--------------------------------------")
               print("Sorry not any Teacher Records")
               print("--------------------------------------")
          else:
               print("--------------------------------------")
               print("----Display Teacher Records-----")
               for tea in teacher:
                    print(f"Name : {tea['Name']}\nId : {tea['t_id']}\nAddress : {tea['address']}")
                    print("--------------------------------------")
     except Exception as e:
          print(e)
     finally:
          print("--------------------------------------")
def update_teach():
     try:
          if teacher == []:
               print("Teacher Record's empty")
          else:
               print("--------------------------------------")
               print("------Update Teacher details------")
               t_id=input("Enter Teacher Id : ")
               for tea in teacher:
                    if tea['t_id']==t_id:
                         tea["Name"]=input("Enter New Name : ")
                         tea['address']=input("Enter New Address : ")
                         print("****Updated Record****")
                         return
               print("***Not Found any Record****")
               print("--------------------------------------")
     except Exception as e:
          print(e)
     finally:
          print("--------------------------------------")
def delete_teach():
     try:
          if teacher == []:
               print("--------------------------------------")
               print("Sorry not any Teacher Records")
               print("--------------------------------------")
          else:
               print("--------------------------------------")
               print("-----Delete Teacher Records------")
               tid = input("Enter Teacher ID : ")
               for tea in teacher:
                    if tea['t_id']==tid:
                         teacher.remove(tea)
                         print("Delete Records Succefully")
                         return
               print("***Don't found Records***")
                    
     except Exception as e:
          print(e)
     finally:
          print("--------------------------------------")

# Course Management
def add_course():
     try:
          print("--------------------------------------")
          print("------Add Course Records------")
          c_id=input("Enter Course Id : ")
          c_name=input("Enter Course Name : ")
          
          if any(c_id in dict.values() for dict in course):
               print(f"***{c_id} is Exited***")
          else:
               course.append({"c_id":c_id,"c_name":c_name})
               print("Course add succefully")
               print("--------------------------------------")
               
     except Exception as e:
          print(e)
     
def  display_course():
     try:
          if course == []:
               print("--------------------------------------")
               print("Sorry not any Course Records")
               print("--------------------------------------")
          else:
               print("--------------------------------------")
               print("-----Display course Records-------")
               for cou in course:
                    print(f"Course Id : {cou['c_id']}\nCourse Name : {cou['c_name']}")
                    print("--------------------------------------")
     except Exception as e:
          print(e)
     finally:
          print("--------------------------------------")
def update_course():
     try:
          if course == []:
               print("--------------------------------------")
               print("Sorry not any Course Records")
               print("--------------------------------------")
          else:
               print("--------------------------------------")
               print("------Update Course details------")
               cid=input("Enter Course Id : ")
               for cou in course:
                    if cou['c_id']==cid:
                         cou['c_name']=input("Enter New Course Name : ")
                         print("****Updated Succefully****")
                         return
               print("***Don't found Id***")
               print("--------------------------------------")
                          
     except Exception as e:
          print(e)
def delete_course():
     try:
          if course == []:
               print("--------------------------------------")
               print("Sorry not any Course Records")
               print("--------------------------------------")
          else:
               print("--------------------------------------")
               print("------Delete Course details------")
               cid=input("Enter Course Id : ")
               for cou in course:
                    if cou['c_id']==cid:
                         course.remove(cou)
                         print("****Deleted****")
                         return
               print("Don't found Id ")
               print("--------------------------------------")
                        
     except Exception as e:
          print(e)
     finally:
          print("--------------------------------------")

while True:
     print("\n\t*****School Management System*****")
     print("1. Student Management")
     print("2. Teacher Management")
     print("3. Course Management")
     print("4. Exit")
     ch = input("Enter choise : ")
     if ch == '1':
          while True:
               print("Student Management System")
               print("*******************************")
               print("1. Add Student")
               print("2. Display Student")
               print("3. update Student records")
               print("4. Delete Student recors")
               print("5. Exit")
               ch=input("Enter Choice :- ")
               if ch == "1":
                    add_stud()
               elif ch == "2":
                    display_stud()
               elif ch == "3":
                     update_stud()
               elif ch == "4":
                    delete_stud()
               elif ch == "5":
                    break
               else:
                    print("Invalid options")
     elif ch == '2':
          while True:
               print("Teacher Management System")
               print("*******************************")
               print("1. Add Teacher")
               print("2. Display Teacher")
               print("3. Update Teacher records")
               print("4. Delete Teacher records")
               print("5. Exit")
               ch=input("Enter Choice :- ")
               if ch == '1':
                    add_teach()
               elif ch == '2':
                    display_teach()
               elif ch == '3':
                    update_teach()
               elif ch == '4':
                    delete_teach()
               elif ch == '5':
                    break
               else:
                    print("Invalid options")

     elif ch == '3':
          while True:
               print("Course Management System")
               print("*******************************")
               print("1. Add Course")
               print("2. Display Course")
               print("3. Update Course")
               print("4. Delete Course")
               print("5. Exit")
               ch=input("Enter Your Choise : ")
               if ch == '1':
                    add_course()
               elif ch == '2':
                    display_course()
               elif ch == '3':
                    update_course()
               elif ch == '4':
                    delete_course()
               elif ch == '5':
                    break
               
     elif ch == '4':
          break
     else:
          print("Invalid message")
