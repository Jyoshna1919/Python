'''
create a careerpage class inside that we have to create two classes,one classes is for admin, to add jobpost and see the number of applications with details and second class is for user to see number of jobs and apply for job.
'''
class Carrer_page:
    def __init__(self):
        while True:
            print(''' -----------------------------------------Welcome to Marolix Technology--------------------------------------------------
                                                * Admin login press 1
                                                * User-login press 2
        ''')
            n=input()
            if n=='1':
                a=Carrer_page.Admin()
            elif n=='2':
                u=Carrer_page.User()
            else:
                print('----------------------------------------------Invalid key---------------------------------------------------')
                s=input('press any key to continue')

    class Admin:
        job_list=[]
        emp_details=[]
        def __init__(self):
            print('''------------------------------------------------------------Welocome to admin panel------------------------------------------------------------
                                                                1.Add Jobpost
                                                                2.No of applicants
                        To add job press 1, To get Total no of applicants press 2''')
            n=input()
            if n=='1':
                self.add()
            elif n=='2':
                self.total()
            else:
                print('--------------=-------------------Error 505-----------------------------------------')
                s=input('press any key to continue')

                

        code=1
        def add(self):
            job={}
            job['Job-id']=str(Carrer_page.Admin.code)
            job['Role']=input('Enter Designation of job: ')
            job['Domain']=input('Enter domain for that designation: ')
            job['location']=input('Enter location for that job: ')
            job['Experience']=input('Enter experience for that role: ')
            job['CTC']=input('Enter CTC for that role: ')
            Carrer_page.Admin.job_list.append(job)
            Carrer_page.Admin.code+=1
            print('Job post added succesfully')
            s=input('press any key to continue')
        
        def total(self):
            for d in Carrer_page.Admin.emp_details:
                print(d)
            else:
                s=input('press any key to continue')



    class User(Admin):
        def __init__(self):
            for ch in Carrer_page.Admin.job_list:
                print(ch)
            n=input('Enter Job-id to apply, orelse press 0 to exit: ')
            if n=='0':
                print('---------thank you------------------')
                p=input('press any key to continue')
            else:
                for ch in Carrer_page.Admin.job_list:
                    if n==ch.get('Job-id'):
                        d={}
                        d['User-name']=input('Enter your name: ')
                        d['mobile']=input('enter mobile number: ')
                        d['age']=input('Enter your age: ')
                        d['Job-id']=n
                        d['Role']=ch.get('Role')
                        Carrer_page.Admin.emp_details.append(d)
                        print(f"You have succesfully applied for the role of {ch.get('Role')}")
                        s=input('press any key to continue')
                        break
                else:
                    print('-------------------------------Invalid Entry, Try agian-----------------------------')
                    s=input('press any key to continue')


c=Carrer_page()


    
        
