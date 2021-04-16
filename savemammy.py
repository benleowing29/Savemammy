# -*- coding: utf-8 -*-
import random
import time
import getpass
import csv

width = 44
login_tried = 0
endProgram = False

account = {}
job ={}
captcha_list = ['heLL0', 'HoW', "R", "YoU?"]


def update():
    with open('mammydata.csv', newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            info = {'pw': row['pw'], 'name': row['name'], 'age': row['age'], 'no_of_children': row['no_of_children'], 'child_age': row['child_age'], 'job1': row['job1'], 'job2': row['job2'], 'job3': row['job3'], 'work_mode': row['work_mode'], 'start_time': row['start_time'], 'end_time': row['end_time'], 'experience': row['experience'], 'duration': row['duration']}
            account[row['email']] = info
    with open('jobdata.csv', newline='') as jobfile:
        rows = csv.DictReader(jobfile)
        a = 0
        for row in rows:
            a = a + 1
            detail = {'company': row['company'], 'job_name': row['job_name'], 'job_t': row['job_t'], 'job_mode': row['job_mode'], 'start_time': row['start_time'], 'end_time': row['end_time'], 'salary': row['salary'], 'vaccancyno': row['vaccancyno'], 'expectation': row['expectation'], 'details': row['details'], 'contactinfo': row['contactinfo']}
            job[str(a)] = detail
def register(account):
    email = input("Please input your email for login: ")
    while True:
        try:
            if email == "":
                raise Exception("This field cannot be empty!")
        except Exception as msg:
            print(msg)
            break
        try:
            if '@' not in email:
                raise Exception("Please enter an email!!")
        except Exception as msg:
            print(msg)
            break
        else:
            pw = getpass.getpass(prompt='Please input your password: ')
            try:
                if pw == "":
                    raise Exception("This field cannot be empty!")
            except Exception as msg:
                print(msg)
                break
            else:
                confirm = getpass.getpass(prompt='Please retype the password: ')
                try:
                    if confirm != pw:
                        raise Exception("Your password and confirmation password do not match!")
                except Exception as msg:
                    print(msg)
                    break
                else:
                    name = input("Please input your full name: ")
                    try:
                        if name == "":
                            raise Exception("This field cannot be empty!")
                    except Exception as msg:
                        print(msg)
                        break
                    else:
                        age_range = ("18-25",'26-30','31-40','41-50','51+')
                        a = 0
                        print("## {} ##".format("#"*width))
                        print("## {} ##".format("".center(width)))
                        for i in age_range:
                            a = a + 1
                            b = str(a) + ". " + i
                            print("## {} ##".format(b.ljust(width)))
                        print("## {} ##".format("".center(width)))
                        print("## {} ##".format("#"*width))
                        print("\n")
                        age = input("Please input your age range (input integer): ")
                        try:
                            if age == "":
                                raise Exception("This field cannot be empty!")
                        except Exception as msg:
                            print(msg)
                            break
                        try:
                            age = int(age)
                        except ValueError:
                            print("Try Again!! Please enter the integer.")
                            break
                        try:
                            if age < 1 or age > a:
                                raise Exception("Please input integer show in the list!")
                        except Exception as msg:
                            print(msg)
                            break
                        else:
                            no_of_children = input("Please input number of children: ")
                            try:
                                if no_of_children == "":
                                    raise Exception("This field cannot be empty!")
                            except Exception as msg:
                                print(msg)
                                break
                            try:
                                no_of_children = int(no_of_children)
                            except ValueError:
                                print("Try Again!! Please enter the integer.")
                                break
                            else:
                                children_age_range = ("0-3","4-6","6+")
                                c = 0
                                print("## {} ##".format("#"*width))
                                print("## {} ##".format("".center(width)))
                                for i in children_age_range:
                                    c = c + 1
                                    d = str(c) + ". " + i
                                    print("## {} ##".format(d.ljust(width)))
                                print("## {} ##".format("".center(width)))
                                print("## {} ##".format("#"*width))
                                print("\n")
                                child_age = input("Please input age range of your youngest child (input integer): ")
                                try:
                                    if child_age == "":
                                        raise Exception("This field cannot be empty")
                                except Exception as msg:
                                    print(msg)
                                    break
                                try:
                                    child_age = int(child_age)
                                except ValueError:
                                    print("Try Again!! Please enter the integer.")
                                    break
                                try:
                                    if child_age < 1 or child_age > c:
                                        raise Exception("Please input integer show in the list!")
                                except Exception as msg:
                                    print(msg)
                                    break
                                else:
                                    job_type = ("Baby Sitting","Nanny","Playgroup Tutor","Postnatal Care/Assist","After-class tutorial","Accounting/Auditing","Baking","Designer","Copywriter","Customized Gift","Promoter")
                                    e=0
                                    print("## {} ##".format("#"*width))
                                    print("## {} ##".format("".center(width)))
                                    for i in job_type:
                                        e = e + 1
                                        f = str(e) + ". " + i
                                        print("## {} ##".format(f.ljust(width)))
                                    print("## {} ##".format("".center(width)))
                                    print("## {} ##".format("#"*width))
                                    print("\n")
                                    job1 = input("Please input first preferred job type (input integer): ")
                                    job2 = input("Please input second preferred job type (input integer): ")
                                    job3 = input("Please input third preferred job type (input integer): ")
                                    try:
                                        if job1 == "" or job2 == "" or job3 =="":
                                            raise Exception("This field cannot be empty")
                                    except Exception as msg:
                                        print(msg)
                                        break
                                    try:
                                        job1 = int(job1)
                                        job2 = int(job2)
                                        job3 = int(job3)
                                    except ValueError:
                                        print("Try Again!! Please enter the integer.")
                                        break
                                    try:
                                        if (job1 < 1 or job1 > e) or (job2 < 1 or job2 > e) or (job3 < 1 or job3 > e):
                                            raise Exception("Please input integer show in the list!")
                                    except Exception as msg:
                                        print(msg)
                                        break
                                    else:
                                        mode = ("Part Time","Full Time","Freelance")
                                        g = 0
                                        print("## {} ##".format("#"*width))
                                        print("## {} ##".format("".center(width)))
                                        for i in mode:
                                            g = g + 1
                                            h = str(g) + ". " + i
                                            print("## {} ##".format(h.ljust(width)))
                                        print("## {} ##".format("".center(width)))
                                        print("## {} ##".format("#"*width))
                                        print("\n")
                                        work_mode = input("Please input your preferred work mode (input integer): ")
                                        try:
                                            if work_mode == "":
                                                raise Exception("This field cannot be empty")
                                        except Exception as msg:
                                            print(msg)
                                            break
                                        try:
                                            work_mode = int(work_mode)
                                        except ValueError:
                                            print("Try Again!! Please enter the integer.")
                                            break
                                        try:
                                            if work_mode < 1 or work_mode > g:
                                                raise Exception("Please input integer show in the list!")
                                        except Exception as msg:
                                            print(msg)
                                            break
                                        else:
                                            print("Please input your available time period in HHMM (e.g.1215)")
                                            start_time = input("From: ")
                                            end_time = input("To: ")
                                            experience = input("Please input number of years of experience in your preferred job field: ")
                                            try:
                                                if experience == "":
                                                    raise Exception("This field cannot be empty")
                                            except Exception as msg:
                                                print(msg)
                                                break
                                            try:
                                                experience = int(experience)
                                            except ValueError:
                                                print("Try Again!! Please enter the integer.")
                                                break
                                            else:
                                                j = 0
                                                print("## {} ##".format("#"*width))
                                                print("## {} ##".format("".center(width)))
                                                for i in ("One-off","Weekly","Monthly"):
                                                    j = j + 1
                                                    k = str(j) + ". " + i
                                                    print("## {} ##".format(k.ljust(width)))
                                                print("## {} ##".format("".center(width)))
                                                print("## {} ##".format("#"*width))
                                                print("\n")
                                                duration = input("Please input duration (input integer): ")
                                                try:
                                                    if duration == "":
                                                        raise Exception("This field cannot be empty")
                                                except Exception as msg:
                                                    print(msg)
                                                    break
                                                try:
                                                    duration = int(duration)
                                                except ValueError:
                                                    print("Try Again!! Please enter the integer.")
                                                    break
                                                try:
                                                    if duration < 1 or duration > j:
                                                        raise Exception("Please input integer show in the list!")
                                                except Exception as msg:
                                                    print(msg)
                                                    break
                                                else:
                                                    with open("mammydata.csv", 'a', newline="") as csvfile:
                                                        fieldnames = ['email','pw','name','age','no_of_children','child_age','job1','job2','job3','work_mode','start_time','end_time','experience','duration']
                                                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                                                        writer.writeheader()
                                                        writer.writerow({'email': email, 'pw': pw, 'name': name, 'age': age, 'no_of_children': no_of_children, 'child_age': child_age, 'job1': job1, 'job2': job2, 'job3': job3, 'work_mode': work_mode, 'start_time': start_time, 'end_time': end_time, 'experience': experience, 'duration': duration})
                                                        update()
                                                    print("## {} ##".format("#"*width))
                                                    print("## {} ##".format("".center(width)))
                                                    print("## {} ##".format("Successful Registration!".center(width)))
                                                    print("## {} ##".format("".center(width)))
                                                    print("## {} ##".format("1. Login".ljust(width)))
                                                    print("## {} ##".format("2. Back to Menu".ljust(width)))
                                                    print("## {} ##".format("3. Exit".ljust(width)))
                                                    print("## {} ##".format("".center(width)))
                                                    print("## {} ##".format("#"*width))
                                                    option = input("Enter the option: ")
                                                    if option == "1":
                                                        login(account, login)
                                                        return False
                                                    elif option == '2':
                                                        return False
                                                    else:
                                                        return True
def login(account, login_tried):
    global login
    a = ""
    ntime=""
    # Use while loop to stop the program after user tries login thrice
    while login_tried <3:
        login = input("Login Email: ")
        # Check the existence of a username
        if login in account.keys():
            pw = getpass.getpass(prompt='Password: ')
            # Check password and hide the input
            if pw == account[login]["pw"]:
                # Draw the captcha from captcha list to verify human 
                captcha=random.choice(captcha_list)
                print("Enter the following captcha to verify you are human: " + captcha)
                a=input("Your answer: ")
                if a == captcha:
                    print("Login Success!")
                    break
                else:
                    # login_tried add up 1 if user inputs data incorrectly
                    login_tried = login_tried + 1
                    print("Please try again!! Input captcha wrongly!")
            else:
                login_tried = login_tried + 1
                print("Please try again!! Wrong password")
                # Use variable ntime to store the current time if user inputs data incorrectly
                ntime = time.localtime()
        else:
            login_tried = login_tried + 1
            print("Please Try Again!! This user does not exist.")
    else:
        # Shutdown the program if users input the data incorrectly thrice
        endProgram = True

def upload():
    company = input("Please input company name: ")
    while True:
        try:
            if company == "":
                raise Exception("This field cannot be empty!")
        except Exception as msg:
            print(msg)
            break
        else:
            job_name = input("Please input job name: ")
            try:
                if job_name == "":
                    raise Exception("This field cannot be empty!")
            except Exception as msg:
                print(msg)
                break
            else:
                job_type = ("Baby Sitting","Nanny","Playgroup Tutor","Postnatal Care/Assist","After-class tutorial","Accounting/Auditing","Baking","Designer","Copywriter","Customized Gift","Promoter")
                e=0
                print("## {} ##".format("#"*width))
                print("## {} ##".format("".center(width)))
                for i in job_type:
                    e = e + 1
                    f = str(e) + ". " + i
                    print("## {} ##".format(f.ljust(width)))
                print("## {} ##".format("".center(width)))
                print("## {} ##".format("#"*width))
                print("\n")
                job_t = input("Please input the related job type (input integer): ")
                try:
                    if job_t == "":
                        raise Exception("This field cannot be empty")
                except Exception as msg:
                    print(msg)
                    break
                try:
                    job_t = int(job_t)
                except ValueError:
                    print("Try Again!! Please enter the integer.")
                    break
                try:
                    if (job_t < 1 or job_t > e):
                        raise Exception("Please input integer show in the list!")
                except Exception as msg:
                    print(msg)
                    break
                else:
                    mode = ("Part Time","Full Time","Freelance")
                    g = 0
                    print("## {} ##".format("#"*width))
                    print("## {} ##".format("".center(width)))
                    for i in mode:
                        g = g + 1
                        h = str(g) + ". " + i
                        print("## {} ##".format(h.ljust(width)))
                    print("## {} ##".format("".center(width)))
                    print("## {} ##".format("#"*width))
                    print("\n")
                    job_mode = input("Please input the work mode (input integer): ")
                    try:
                        if job_mode == "":
                            raise Exception("This field cannot be empty")
                    except Exception as msg:
                        print(msg)
                        break
                    try:
                        job_mode = int(job_mode)
                    except ValueError:
                        print("Try Again!! Please enter the integer.")
                        break
                    try:
                        if job_mode < 1 or job_mode > g:
                            raise Exception("Please input integer show in the list!")
                    except Exception as msg:
                        print(msg)
                        break
                    else:
                        print("Please input the work time period in HHMM (e.g.1215)")
                        start_time = input("From: ")
                        end_time = input("To: ")
                        salary = input("Please input salary (in integer): ")
                        try:
                            if salary == "":
                                raise Exception("This field cannot be empty")
                        except Exception as msg:
                            print(msg)
                            break
                        try:
                            salary = int(salary)
                        except ValueError:
                            print("Try Again!! Please enter the integer.")
                            break
                        else:
                            vaccancyno = input("Please input the number of vaccancy: ")
                            try:
                                if vaccancyno == "":
                                    raise Exception("This field cannot be empty")
                            except Exception as msg:
                                print(msg)
                                break
                            try:
                                vaccancyno = int(vaccancyno)
                            except ValueError:
                                print("Try Again!! Please enter the integer.")
                                break
                            else:
                                expectation = input("Type your expectation (optional): ")
                                details = input("Type the job details: ")
                                try:
                                    if details == "":
                                        raise Exception("This field cannot be empty")
                                except Exception as msg:
                                    print(msg)
                                    break
                                else:
                                    contactinfo = input("Type the contact info: ")
                                    try:
                                        if contactinfo == "":
                                            raise Exception("This field cannot be empty")
                                    except Exception as msg:
                                        print(msg)
                                    else:
                                        with open("jobdata.csv", 'a', newline="") as jobfile:
                                            fieldnames = ['company','job_name','job_t','job_mode','start_time','end_time','salary','vaccancyno','expectation','details','contactinfo']
                                            writer = csv.DictWriter(jobfile, fieldnames=fieldnames)
                                            writer.writeheader()
                                            writer.writerow({'company': company, 'job_name': job_name, 'job_t': job_t, 'job_mode': job_mode, 'start_time': start_time, 'end_time': end_time, 'salary': salary, 'vaccancyno': vaccancyno, 'expectation': expectation, 'details': details, 'contactinfo': contactinfo})
                                            update()
                                        print("## {} ##".format("#"*width))
                                        print("## {} ##".format("".center(width)))
                                        print("## {} ##".format("Successful Registration!".center(width)))
                                        print("## {} ##".format("".center(width)))
                                        print("## {} ##".format("1. Back to Menu".ljust(width)))
                                        print("## {} ##".format("2. Exit".ljust(width)))
                                        print("## {} ##".format("".center(width)))
                                        print("## {} ##".format("#"*width))
                                        option = input("Enter the option: ")
                                        if option == "1":
                                            return False
                                        else:
                                            return True
                                    


def matching(account, job, login):
    a = 0
    job_type = ("Baby Sitting","Nanny","Playgroup Tutor","Postnatal Care/Assist","After-class tutorial","Accounting/Auditing","Baking","Designer","Copywriter","Customized Gift","Promoter")
    mode = ("Part Time","Full Time","Freelance")

    for i,j in job.items():
        if j['job_t'] == account[login]['job1'] or j['job_t'] == account[login]['job2'] or j['job_t'] == account[login]['job3']:
            if j['job_mode'] == account[login]['work_mode']:
                if (int(account[login]['start_time'])<= int(j['start_time']) <= int(account[login]['end_time'])) and (int(account[login]['start_time'])<= int(j['end_time']) <= int(account[login]['end_time'])):
                    a = a + 1
                    print(str(a)+".")
                    print("Company:", j['company'], "\n")
                    print("Job:", j['job_name'], "\n")
                    print("Job Type:", job_type[int(j['job_t'])-1], "\n")
                    print("Job Mode:", mode[int(j['job_mode'])-1], "\n")
                    print("Time:", j["start_time"],"-",j["end_time"],"\n")
                    print("Salary:", j["salary"],"\n")
                    print("Number of Vaccancies:", j["vaccancyno"], "\n")
                    print("Expectation:", j["expectation"], "\n")
                    print("Details:", j["details"], "\n")
                    print("Contact Information:", j["contactinfo"],"\n")
                    
    if a == 0:
        print("Sorry!! We have no jobs which suitable for you.")
    else:
        print("We have sent your information to the company!")
            




while not endProgram:
    # menu page
    menuoption = ""
    update()
    while not menuoption in ["1", "2", "3", "4","5","view"]: 
        
        print("##################################################")
        print("## {} ##".format("".center(width)))
        print("## {} ##".format("Please select service".center(width)))
        print("## {} ##".format("".center(width)))
        print("## {} ##".format("1. Register ".ljust(width)))
        print("## {} ##".format("2. Login".ljust(width)))
        print("## {} ##".format("3. Upload Job".ljust(width)))
        print("## {} ##".format("4. Matching".ljust(width)))
        print("## {} ##".format("5. Exit".ljust(width)))
        print("## {} ##".format("".center(width)))
        print("## {} ##".format("#"*width))
        menuoption = input("Enter the option: ")

    else:
        if menuoption == "1":
            endProgram = register(account)
            input("Press Enter to continue...")
            
        elif menuoption == "2":
            endProgram = login(account, login_tried)
            input("Press Enter to continue...")
            
        elif menuoption == "3":
            endProgram = upload()
            input("Press Enter to continue...")
            
        elif menuoption == "4":
            endProgram = matching(account, job, login)
            input("Press Enter to continue...")
            
        elif menuoption == "5":
            endProgram = True

        elif menuoption == "view":
            endProgram = print(account, "n", job)
            input("Press Enter to continue...")


print("Bye!")
input("Press Enter to end the program...")