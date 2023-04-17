

if __name__ == "__main__":
    print("Admin panel open ")
    try:
        import admin_login
    except Exception as e:
        print(e)
    print("Test cases Admin login , deleat button and download button  not working ")

    try:
        import admin_Product
    except Exception as e:
        print(e)
    print("Test cases admin product,order button not working ")
    try:
        import admin_emploaye_list
    except Exception as e :
        print(e)
    print("showing a Date eroor ")
    try :
        import admin_Emp_Click
    except Exception as e:
        print(e)
    print("running on click button ")
    try:
        import admin_Add_CreateP
    except Exception as e:
        print(e)
    print("An uncaught Exception was encountered")
    try:
        import admin_add_employe
    except Exception as e:
        print(e)
    print("Add employe end ")
    print("Every page showing a massege 'invalid crdentials '")
    try :
        import admin_Add_Access
    except Exception as e:
        print(e)
    print ("add access group end ")
    print("every page message showing invalid credentials")

    try :
        import admin_add_client
    except Exception as e:
        print(e)
    print("test cases add client")

    try :
        import admin_report
    except Exception as e:
        print(e)
    print("test cases admin reports ")

    try :
        import admin_attendR
    except Exception as e:
        print(e)
    print("Every thing is properly working")

    try:
        import admin_expenceRE
    except Exception as e :
        print(e)
    print("test cases Expence report")
    try :
        import admin_orderRe
    except Exception as e:
        print(e)
    print("test cases order report")

