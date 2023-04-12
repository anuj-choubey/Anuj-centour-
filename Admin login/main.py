

if __name__ == "__main__":
    print("Admin panel open ")
    try:
        import adminlogin
    except Exception as e:
        print(e)
    print("Test cases Admin login ")

    try:
        import adminProduct
    except Exception as e:
        print(e)
    print("Test cases admin product")